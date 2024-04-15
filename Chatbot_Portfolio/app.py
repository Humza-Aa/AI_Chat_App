from flask import Flask, request, make_response, jsonify
from chat_init import chatbot_response
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os
import requests


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


@app.route('/test', methods=['Post'])
def iptest():
    client_ip = request.headers.get(
        'X-Forwarded-For', request.headers.get('True-Client-Ip', request.remote_addr))
    return f"Your IP address is: {client_ip}"


def get_user_ip():
    if request.headers.getlist("X-Forwarded-For"):
        user_ip = request.headers.get(
            'X-Forwarded-For', request.headers.get('True-Client-Ip', request.remote_addr))
    else:
        user_ip = request.remote_addr
    return user_ip


@app.route('/loc', methods=['Post'])
def location():
    SiteCollection.update_one(
        {}, {'$inc': {'Site Opened': 1}}, upsert=True)
    count = SiteCollection.find_one({}, {'Site Opened': 1})
    user_ip = get_user_ip()
    api_url = f'http://ip-api.com/json/{user_ip}'
    response = requests.get(api_url)
    if response.status_code != 200:
        return 'Error: Failed to call API', 500
    response_data = response.json()
    if response_data.get('status') != 'success':
        query = response_data.get('query')
        SiteCollection.insert_one(
            {'query': query, 'message': 'IP is not Supported'})
        return 'Success', 200
    keys_to_extract = ['status', 'message', 'country', 'countryCode', 'region',
                       'regionName', 'city', 'zip', 'lat', 'lon', 'timezone', 'isp', 'org', 'as', 'query']
    response_data = response.json()
    extracted_data = {key: response_data.get(key) for key in keys_to_extract}
    SiteCollection.insert_one(extracted_data)
    return 'Success', 200


@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    res = chatbot_response(message)
    response = make_response(res)

    request_response = {
        'request': message,
        'response': res,
        'Time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    collection.insert_one(request_response)
    collection.delete_many({'request': "bot"})
    response.headers['Content-Type'] = 'text/plain'
    return response
# if __name__ == '__main__':
#     app.run(debug=True)
