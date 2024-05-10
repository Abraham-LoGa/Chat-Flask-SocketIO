from flask import Flask, Response, request, Blueprint
from flask_cors import CORS

app = Flask(__name__)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5060, debug=True)