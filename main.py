from flask import Flask, Response, request, Blueprint
from flask_cors import CORS
from flask_socketio import emit, send
from board.socketio_init import socketio
from board.nlg import bp as nlg
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio.init_app(app)
app.register_blueprint(nlg)
# @app.route('/')
# def index():
#     return 'Hola'

# @socketio.on('message')
# def handle_message(message2):
#     print(message2)
#     #emit('my response', {'data': 'got it!'})



if __name__ == '__main__':
    socketio.run(app, debug=True)