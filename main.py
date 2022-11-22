import socket

from flask import Flask


app = Flask(__name__)


COUNTER = 0


@app.route("/")
def counter():
    return f"<h1>Count: {COUNTER}</h1>"


@app.route("/start")
def increment():
    global COUNTER
    current = COUNTER
    COUNTER += 1
    return f"<h1>Count: {current}</h1>"


@app.route("/about")
def about():
    html = "<h3>Hello, {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name="Alex", hostname=socket.gethostname())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
