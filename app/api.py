from app import app

import vk

import random

session = vk.Session()
api = vk.API(session=session)


def send_message(user_id, message, attachment=''):

    api.messages.send(
        access_token=app.config['TOKEN'],
        user_id=str(user_id),
        message=message,
        attachment=attachment
    )


def find_random_gif(gif_name):
    """
    search random gif by gif_name
    :param gif_name: str
    :return: str
    """
    gif_q = '%s gif' % gif_name
    gifs = api.docs.search(access_token=app.config['TOKEN'], q=gif_q, count=999, offset=1)[1:]

    if gifs:
        max_random = 999 if len(gifs)-1 > 999 else len(gifs)-1
        offset = random.randint(0, max_random)
        gif = gifs[offset]
        return 'doc%s_%s'%(str(gif['owner_id']), str(gif['did']))
    return ''