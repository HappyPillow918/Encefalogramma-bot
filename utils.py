"""
Program: utils.py
Author: HappyPillow918
Recurrent functions used in bot.py.
"""
from yaml import safe_load
from tinydb import TinyDB, Query
from config import DATABASE_PATH, BOT_GROUP_ID, INTERNSHIP_GROUP_ID, INTERNSHIP_STRINGS

db = TinyDB(DATABASE_PATH)


# Create a list given a dictionary [data] and a string [header].
def create_list(data, header) -> str:
    markdown = '' if 'tirocinio' in header else '`'
    if data:
        for elem in data:
            header += '\n> ' + markdown + elem['text'] + markdown
    else:
        header += '\nNessuno'
    return header


# Check if a string [message] follows the format expected by the calling function [case].
def check_format(message) -> dict:
    result = {}
    try:
        temp = safe_load(message)
        if (
            temp.get('text', False)
            and temp.get('url', False)
            and temp.get('type', False)
            and temp.get('semester', False)
            and 'https://' in temp['url']
            and temp['type'] in ['B-generic', 'B-first', 'B-second', 'B-third', 'internship', 'M-generic',
                                 'M-first', 'M-second']
            and temp['semester'] in ['zero', 'one', 'two']
         ):
            result = temp
    except Exception:
        return result

    return result


# Returns True if the user [user_id] is an admin in a particolar group [chat id].
def check_admin(user_id, chat_id, bot) -> bool:
    return bool(user_id in [admin.user.id for admin in bot.get_chat_administrators(chat_id)])


# Send interns' list
def send_list(bot, message, list_interns, list_header) -> None:
    message_text = f"{create_list(list_interns, list_header)}\n{INTERNSHIP_STRINGS['info']}"
    try:
        bot.editMessageText(chat_id=INTERNSHIP_GROUP_ID,
                            message_id=db.all()[0]['id'],
                            text=message_text[:4000],
                            parse_mode='Markdown')
    except Exception:
        msg = message.reply_text(text=message_text[:4000],
                                 quote=False, parse_mode='Markdown')
        db.update({'id': msg.message_id}, Query().id.exists())


# Escape reserved chars in Markdown
def escape_chars(text) -> str:
    if text:
        chars = '_*`[]'
        for c in chars:
            text = text.replace(c, '\\' + c)
    return text


# Backup file
def backup(bot) -> None:
    bot.sendDocument(chat_id=BOT_GROUP_ID, document=open(DATABASE_PATH, 'rb'))
    return
