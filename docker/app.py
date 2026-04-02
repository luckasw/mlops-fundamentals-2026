from flask import Flask, request, jsonify, send_file, send_from_directory
from pymongo import MongoClient
import os

app = Flask(__name__)

# use when starting application locally
# MONGO_URL_LOCAL = "mongodb://admin:password@localhost:27017"

# # use when starting application as docker container
# MONGO_URL_DOCKER = "mongodb://admin:password@mongodb"
MONGO_URL = os.getenv("MONGO_URL", "mongodb://admin:password@mongodb:27017")

DATABASE_NAME = "my-db"

def get_db():
    client = MongoClient(MONGO_URL)
    return client[DATABASE_NAME], client

dummy_user = {
    "userid": 1,
    "name": "Alex Jones",
    "email": "alex.jones@example.com",
    "interests": "coding"
}


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/profile-picture')
def profile_picture():
    return send_file(
        os.path.join(os.path.dirname(__file__), 'images/p1.png'),
        mimetype='image/png'
    )


# @app.route('/get-profile')
# def get_profile():
#     return jsonify(dummy_user)

@app.route('/get-profile')
def get_profile():
    db, client = get_db()
    try:
        result = db['users'].find_one({'userid': 1}, {'_id': 0})
        return jsonify(result if result else {})
    finally:
        client.close()


@app.route('/update-profile', methods=['POST'])
def update_profile():
    user_obj = request.get_json()
    user_obj['userid'] = 1

    # # update dummy data in memory
    # dummy_user.update(user_obj)
    # return jsonify(dummy_user)


    db, client = get_db()
    try:
        db['users'].update_one(
            {'userid': 1},
            {'$set': user_obj},
            upsert=True
        )
        return jsonify(user_obj)
    finally:
        client.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

