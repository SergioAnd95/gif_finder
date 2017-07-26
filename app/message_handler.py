from .command_models import *
from .command import command_list

from app import mongo

from pymongo.errors import DuplicateKeyError

from .api import send_message


def create_answer(obj):
    """
    generate answer that base command
    :param obj: dict
    :return: None
    """
    try:
        mongo.db.bot_session.insert({'_id':str(obj['user_id']), 'in_command': '', 'stop_command':''}, True)
    except DuplicateKeyError:
        pass

    session = mongo.db.bot_session.find_one({'_id':str(obj['user_id'])})
    message = obj['body']
    msg = ''
    attachment = ''
    for c in command_list:

        if session['in_command'] in c.keys and not message == session['stop_command']:
            msg, attachment = c.process(obj)
            break

        elif message in c.keys:
            msg, attachment = c.process(obj)
            break

    if not msg:
        msg, attachment = 'Извините, но данной команды не существует, ' \
                          'для получения инфориации по командам, воспользуйтесь командой "помощь"', ''

    send_message(user_id=obj['user_id'], message=msg, attachment=attachment)