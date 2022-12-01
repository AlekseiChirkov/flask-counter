import socket

from flask import Flask
from flask import request

from db import insert_into, select_from

app = Flask(__name__)


COUNTER = 0


@app.route("/")
def counter():
    data = select_from()
    html = (
        f"<h1>Count: {data[0][1]}</h1>\n"
        f"<h1>User-Agent: {data[0][2]}</h1>"
    )
    return html


@app.route("/start")
def increment():
    global COUNTER
    current = COUNTER
    COUNTER += 1
    user_agent = request.headers.get('User-Agent')
    data = {
        "counter": COUNTER,
        "user_agent": user_agent
    }
    insert_into(data)
    return f"<h1>Count: {current}</h1>"


@app.route("/about")
def about():
    html = "<h3>Hello, {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name="Alex", hostname=socket.gethostname())


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
