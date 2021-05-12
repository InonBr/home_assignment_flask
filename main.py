from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def test():
    return "test me"


from routes import massage_routes
from routes import user_routes

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
