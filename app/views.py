from app import app

import json

from flask import request

from .api import send_message

from . import message_handler

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/', methods=['POST'])
def proccesing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return app.config['CONFIRMATION_TOKEN']
    elif data['type'] == 'message_new':
        message_handler.create_answer(data['object'])
        return 'ok'