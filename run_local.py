from flask import request as request_
from flask import Flask

from main import feed_http

app = Flask('test')


@app.route('/')
def local_run():
    return feed_http(request_)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
