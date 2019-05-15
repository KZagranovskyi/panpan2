import flask
from flask import Flask

import Payment

app = Flask(__name__, static_url_path='/static')


# @app.route('/')
# def hello_world():
#     return 'Hello World!'


@app.route('/js/<path:path>')
def send_js(path):
    return flask.send_from_directory('static/js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return flask.send_from_directory('static/css', path)


@app.route('/images/<path:path>')
def send_images(path):
    return flask.send_from_directory('static/images', path)


@app.route('/fonts/<path:path>')
def send_fonts(path):
    return flask.send_from_directory('static/fonts', path)


@app.route('/<path:path>')
def send_html(path):
    return flask.send_from_directory('static', path)


@app.route("/")
def hello():
    return flask.send_from_directory('static', "index.html")

@app.route("/payment")
def pay():
    return Payment.send_peyment()


if __name__ == '__main__':
    app.run()
