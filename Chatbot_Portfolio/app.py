from flask import Flask, request, make_response
from chat_init import chatbot_response
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello!"

@app.route('/chat', methods=['POST'])
def chat():
    print(request)
    message = request.form['message']
    res = chatbot_response(message)
    response = make_response(res)
    response.headers['Content-Type'] = 'text/plain'
    return response


# if __name__ == '__main__':
#     app.run(debug=True)
