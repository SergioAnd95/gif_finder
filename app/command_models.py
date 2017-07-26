from .command import Command, command_list
from .api import find_random_gif

from app import mongo


# Command for start search
start_search_command = Command('поиск', 'Поиск гифок')
start_search_command.keys = ['start', 'search']


def start_search(obj):
    user_id = str(obj['user_id'])
    mongo.db.bot_session.update(
        {'_id': user_id},
        {'$set': {'in_command': 'in_search', 'stop_command': 'меню'}}
    )
    return ('Введите название гифки и вы ее получите 😊', '')

start_search_command.process = start_search

# Command to search
in_search_command = Command('in_search', in_help=False)


def search(obj):
    q = obj['body']
    attachment = find_random_gif(q)
    if not attachment:
        return 'Извините, но по вашему запросу "%s", ничего не было найдено😒😢' % q, ''

    return (
        'Вот ваша гифка👍, наслаждайтесь😊\nДля выхода из поиска воспользуйтесь командой: "меню"',
        attachment
    )

in_search_command.process = search


# Command to get help
help_command = Command('помощь' , in_help=False)
help_command.keys = ['help', 'помогите', 'sos']


def generate_help(obj):
    title = 'Список достуных команд:'
    lst_command = ['%s - %s' %
                   (i.name, i.description) for i in command_list if i.in_help]

    return '%s\n%s' % (title, '\n\t'.join(lst_command)), ''

help_command.process = generate_help

menu_command = Command('меню', in_help=False)


# Command for stop search and back to menu
def stop_search(obj):
    mongo.db.bot_session.update(
        {'_id': str(obj['user_id'])},
        {'$set': {'in_command': '', 'stop_command':''}}
    )
    return help_command.process(obj)

menu_command.process = stop_search
