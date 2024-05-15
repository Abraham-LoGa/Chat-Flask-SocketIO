from flask import Flask, Response, request, Blueprint
from flask_cors import CORS
from flask_socketio import emit, send
from board.socketio_init import socketio
from board.nlg import bp as nlg
import json

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret!'
socketio.init_app(app)
app.register_blueprint(nlg)
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5060, debug= True)
    #app.run('0.0.0.0', port=5020, debug=True)