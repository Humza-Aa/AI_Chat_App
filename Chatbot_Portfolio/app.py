from flask import Flask, request, make_response
from ..ModelTraining.chat_init import chatbot_response 

app = Flask(__name__)


@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    res = chatbot_response(message)
    response = make_response(res)
    response.headers['Content-Type'] = 'text/plain'
    return response

if __name__ == '__main__':
    app.run(debug=True)