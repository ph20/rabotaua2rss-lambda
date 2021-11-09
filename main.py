
from flask import escape, make_response
from grab import Grab
from feedgen.feed import FeedGenerator
from urllib.parse import urlparse


def feed_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    request_args = request.args
    url = request_args['url']
    g = Grab()
    fg = FeedGenerator()
    g.go(url)

    fg.id(url)
    fg.title('Rabota.UA | rss feed')
    url_parsed = urlparse(g.response.url)
    fg.link(href=url_parsed.scheme + '://' + url_parsed.hostname, rel='alternate')
    fg.description(g.doc('/html/head/title').text())
    count = int(g.doc('//span[@id="ctl00_content_vacancyList_ltCount"]/span').one().text())
    if count == 0:
        itm_list = []
    else:
        articles = g.doc.select('//table[contains(@class, "f-vacancylist-tablewrap")]').one()
        itm_list = articles.select('tr[@id]/td/article/div[contains(@class, "card-body")]')
    for item in itm_list:
        vac_title = item.select('//h2[contains(@class, "card-title")]/a/@title').text().strip()
        vac_url = g.make_url_absolute(item.select('//h2[contains(@class, "card-title")]/a/@href').text())
        vac_description = item.select('//div[contains(@class, "card-description")]').text().strip()
        fe = fg.add_entry()
        print(vac_title)
        fe.id(vac_url)
        fe.link({'href': vac_url})
        fe.source(vac_url)
        fe.title(vac_title)
        fe.description(vac_description)

    response = make_response(fg.atom_str(pretty=True, extensions=False))
    response.headers['Content-Type'] = 'application/rss+xml; charset=UTF-8'
    return response


