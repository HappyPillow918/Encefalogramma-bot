"""
Program: utils.py
Author: HappyPillow918
Recurrent functions used in bot.py.
"""
from yaml import safe_load


# Create a list given a dictionary [data] and a string [header].
def create_list(data, header) -> str:
    if data:
        for elem in data:
            header += '\n> `' + elem['text'] + '`'
    else:
        header += '\n`Nessuno`'
    return header


# Check if a string [message] follows the format expected by the calling function [case].
def check_format(message, case) -> dict:
    result = {}
    if case == 'add_intern':
        if len(message) == 4 and message[0:3].isnumeric() and message[-1].upper() in ('F', 'P'):
            result['crt'] = message[0:3]
            time = 'full' if message[-1].upper() == 'F' else 'part'
            result['type'] = time
    elif case == 'add_group':
        try:
            temp = safe_load(message)
            if (
                temp.get('text', False)
                and temp.get('url', False)
                and temp.get('type', False)
                and temp.get('semester', False)
                and 'https://' in temp['url']
                and temp['type'] in ['generic', 'first', 'second', 'third', 'internship', 'master']
                and temp['semester'] in ['zero', 'one', 'two']
            ):
                result = temp
        except Exception:
            return result

    return result


# Returns True if the user [user_id] is an admin in a particolar group [chat id].
def check_admin(user_id, chat_id, bot):
    return bool(user_id in [admin.user.id for admin in bot.get_chat_administrators(chat_id)])
