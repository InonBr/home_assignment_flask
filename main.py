from flask import Flask

app = Flask(__name__)

from routes import user_routes


@app.route("/")
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
