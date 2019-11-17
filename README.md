Simple example implementation cloud function on google cloud

**Description**

This one cloud function realise converting job search ads (rabota.ua site) to rss feed

**Deploying**

```gcloud functions deploy rabtaua2rss --runtime python37 --entry-point feed_http --trigger-http```

**Usage**
Put the url with search result to url option in url
For example this one show ads for Python developers on all Ukraine

[https://rabota.ua/zapros/python/украина](http://127.0.0.1:5000/?url=https://rabota.ua/zapros/python/%D1%83%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0)
