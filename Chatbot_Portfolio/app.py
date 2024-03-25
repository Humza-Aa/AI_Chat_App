from flask import Flask, request, make_response
from chat_init import chatbot_response
from flask import Flask
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

logging.basicConfig(filename='app.log', level=logging.INFO)


@app.route('/')
def home():
    return "Hello!"


@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    res = chatbot_response(message)
    response = make_response(res)
    logging.info(f"Request: {request}")
    logging.info(f"Message: {message}")
    logging.info(f"Response: {res}")
    response.headers['Content-Type'] = 'text/plain'
    return response

# if __name__ == '__main__':
#     app.run(debug=True)
