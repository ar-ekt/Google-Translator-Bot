from Languages import languages
from Consts import *

import Translate
import Data

from telegram.ext import CallbackContext
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent

from uuid import uuid4

def extract(query: str, src: str, dest: str) -> tuple:
    splt = query.split()
    len_splt = len(splt)
    
    if len_splt >= 1 and splt[0][0] == DOT and splt[0][1:] in languages:
        if len_splt >= 2 and splt[1][0] == DOT and splt[1][1:] in languages:
            return splt[0][1:], splt[1][1:], " ".join(splt[2:])
        elif len_splt >= 2 and splt[1] == DOT:
            return splt[0][1:], FAV, " ".join(splt[2:])
        else:
            return AUTO, splt[0][1:], " ".join(splt[1:])
    
    elif len_splt >= 1 and splt[0] == DOT:
        if len_splt >= 2 and splt[1][0] == DOT and splt[1][1:] in languages:
            return AUTO, splt[1][1:], " ".join(splt[2:])
        elif len_splt >= 2 and splt[1] == DOT:
            return AUTO, FAV, " ".join(splt[2:])
        else:
            return AUTO, FAV, " ".join(splt[1:])
    
    else:
        return src, dest, query

def single_result(text: str, src: str, dest: str):
    translated = Translate.inline_translate(text, src, dest)
    flag_emoji = "  %s" % languages[dest][1]
    
    return InlineQueryResultArticle(id=uuid4(), title=translated+flag_emoji,
        input_message_content=InputTextMessageContent(translated))

def list_result(query: str, src_0: str, dest_0: str, favs: list) -> list:
    src, dest, text = extract(query, src_0, dest_0)
    if dest == FAV:
        if favs[DEST] == []:
            return [single_result(text, src, dest_0)]
        return [single_result(text, src, lang) for lang in favs[DEST]]
    else:
        return [single_result(text, src, dest)]

def query(update: Update, context: CallbackContext) -> None:
    chat_id = update.inline_query.from_user.id
    chat_data = Data.update(chat_id)
    
    query = update.inline_query.query
    
    results = list_result(query, chat_data[chat_id][SRC], chat_data[chat_id][DEST], chat_data[chat_id][FAV])
    
    update.inline_query.answer(results)