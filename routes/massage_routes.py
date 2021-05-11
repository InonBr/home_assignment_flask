from main import app
from flask_pydantic import validate
from flask_cors import cross_origin
from models import NewMassage
from middleware import auth_required
from flask import request


@app.route("/api/createMassage", methods=["POST"])
@cross_origin()
@validate(body=NewMassage)
@auth_required
def create_massage(body: NewMassage):
    massage = body.dict()
    current_user = request.json["current_user"]

    print(massage)
    print(current_user)
    return{"msg": "good"}, 200
