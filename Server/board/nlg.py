from flask import Blueprint
from board.socketio_init import socketio
from flask_socketio import send
import json
bp = Blueprint('nlg', __name__, url_prefix='/nlg')
@bp.route('', methods = ['POST','GET'])
def index():
    return 'Example'

@socketio.on('message')
def handle_message(message):
    body = {
        'message':'Fue una pregunta'
    }
    text = json.dumps(body)
    send(text)