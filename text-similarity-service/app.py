from typing import Text
import bcrypt
import spacy
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
from typing import Text

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://root:secret@mongodb:27017/")
db = client['text_similarity']
users = db['Users']


def user_exists(username: Text) -> bool:
    return users.find({"username": username}).count() > 0


def verify_password(username: Text, password: Text) -> bool:
    if not user_exists(username):
        return False

    hashed_pw = users.find({
        "username": username
    })[0]['password']

    return bcrypt.hashpw(password.encode("utf8"), hashed_pw) == hashed_pw


def count_tokens(username: Text) -> int:
    return users.find({"username": username})[0]['tokens']


class Register(Resource):
    def post(self):
        data = request.get_json()

        user_name = data['username']
        password = data['password']

        if user_exists(user_name):
            return jsonify({
                "status": 301,
                "msg": "Username already exists."
            })

        hashed_pw = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
        users.insert({
            "username": user_name,
            "password": hashed_pw,
            "tokens": 6
        })

        return jsonify({
            "status": 200,
            "msg": "You successfully signed up for the API."
        })


class Detect(Resource):
    def post(self):
        data = request.get_json()

        user_name = data['username']
        password = data['password']
        text1 = data['text1']
        text2 = data['text2']

        if not user_exists(user_name):
            return jsonify({
                "status": 301,
                "msg": "Invalid username."
            })

        correct_pw = verify_password(user_name, password)
        if not correct_pw:
            return jsonify({
                "status": 302,
                "msg": "Invalid password"
            })

        num_tokens = count_tokens(user_name)
        if num_tokens == 0:
            return jsonify({
                "status": 303,
                "msg": "Out of tokens, please refill"
            })

        # check similarity
        model = spacy.load("en_core_web_md")

        parsed_text1 = model(text1)
        parsed_text2 = model(text2)
        sim_ratio = parsed_text1.similarity(parsed_text2)

        users.update(
            {"username": user_name},
            {"$set": {"tokens": num_tokens - 1}}
        )

        return jsonify({
            "status": 200,
            "similarity": sim_ratio,
            "msg": "Similarity ratio calculated successfully."
        })


class Refill(Resource):
    def post(self):
        data = request.get_json()

        user_name = data['username']
        password = data['admin_password']
        refill_amount = data['refill']

        if not user_exists(user_name):
            return jsonify({
                "status": 301,
                "msg": "Invalid username"
            })

        if password != "test123":
            return jsonify({
                "status": 304,
                "msg": "Invalid admin password"
            })

        num_tokens = count_tokens(user_name)
        users.update(
            {"username": user_name},
            {"$set": {
                "tokens": num_tokens + refill_amount
            }}
        )
        return jsonify(
            status=200,
            msg="Refilled successfully."
        )


api.add_resource(Register, "/register")
api.add_resource(Detect, "/detect")
api.add_resource(Refill, "/refill")


if __name__ == '__main__':
    app.run(host="0.0.0.0")
