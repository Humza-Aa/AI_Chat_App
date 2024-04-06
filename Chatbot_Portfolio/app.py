from flask import Flask, request, make_response
from chat_init import chatbot_response
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.get_database()
collection = db.logs
SiteCollection = db.SiteTracker

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "Hello!"


@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    if message == "Site Opened":
        SiteCollection.update_one(
            {}, {'$inc': {'Site Opened': 1}}, upsert=True)
        count = SiteCollection.find_one({}, {'Site Opened': 1})
        response = {'Site Opened': count['Site Opened']}
    else:
        res = chatbot_response(message)
        response = make_response(res)

        request_response = {
            'request': message,
            'response': res
        }
        collection.insert_one(request_response)
        collection.delete_many({'request': "bot"})
        response.headers['Content-Type'] = 'text/plain'
    return response
# if __name__ == '__main__':
#     app.run(debug=True)
