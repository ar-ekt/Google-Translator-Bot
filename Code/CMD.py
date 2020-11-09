from Languages import languages
from Consts import *

import Translate
import Data

from os import remove as os_remove
from time import time as time_time

from telegram.ext import CallbackContext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram import InlineQueryResultArticle, InputTextMessageContent

def unrecognized_zero(chat_id: int) -> None:
    chat_data = Data.update(chat_id)
    chat_data[chat_id][UNRECOGNIZED][0] = 0
    Data.write(chat_data)

def unrecognized(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    chat_data = Data.update(chat_id)
    
    time = int(time_time())
    command = update.message.text
    
    if time - chat_data[chat_id][UNRECOGNIZED][2] > 20 or command != chat_data[chat_id][UNRECOGNIZED][1]:
        chat_data[chat_id][UNRECOGNIZED][0] = 0
        chat_data[chat_id][UNRECOGNIZED][1] = command
        chat_data[chat_id][UNRECOGNIZED][2] = time
    else:
        if chat_data[chat_id][UNRECOGNIZED][0] == UNRECOGNIZED_LEN:
            chat_data[chat_id][UNRECOGNIZED][0] = 1
        else:
            chat_data[chat_id][UNRECOGNIZED][0] += 1
        update.message.reply_text(UNRECOGNIZED_MESSAGES[chat_data[chat_id][UNRECOGNIZED][0]-1])
    
    Data.write(chat_data)

# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #

def translate(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    chat_data = Data.update(chat_id)
    
    translated = Translate.translate(update.message.text, chat_data[chat_id][SRC], chat_data[chat_id][DEST])
    if translated == False:
        update.message.reply_text(TEXT_TRANSLATE_FAILURE)
    else:
        update.message.reply_text(translated.text)
    
    unrecognized_zero(chat_id)

def translate_file(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    chat_data = Data.update(chat_id)
    
    file_size = update.message.document.file_size
    file_name = update.message.document.file_name
    
    if file_size > MAX_FILE_SIZE:
        file = update.message.document.get_file()
        file.download(TEMP_FILE)
        
        with open(TEMP_FILE, encoding = "utf-8") as temp_file:
            text = temp_file.read()
            src = chat_data[chat_id][SRC]
            dest = chat_data[chat_id][DEST]
            translated = Translate.translate(text, src, dest)
        
        if translated == False:
            update.message.reply_text(FILE_TRANSLATE_FAILURE)
        else:
            with open(TEMP_FILE, "w", encoding = "utf-8") as temp_file:
                temp_file.write(translated.text)
            
            with open(TEMP_FILE, "rb") as temp_file:
                update.message.bot.send_document(chat_id, document=temp_file, filename=file_name)
        
        os_remove(TEMP_FILE)
    
    else:
        update.message.reply_text(DOCUMENT_SIZE_ERROR)
    
    unrecognized_zero(chat_id)

# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #

def selected_languages_message(chat_data: dict, chat_id: int) -> str:
    src = chat_data[chat_id][SRC]
    dest = chat_data[chat_id][DEST]
    src_emoji = AUTO_EMOJI if src == AUTO else languages[src][1]
    dest_emoji = languages[dest][1]
    
    text = SELECTED_LANGUAGES_MESSAGE % (src, src_emoji, dest, dest_emoji)
    return text

def selected_languages(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    chat_data = Data.update(chat_id)
    
    text = selected_languages_message(chat_data, chat_id)
    update.message.reply_text(text, parse_mode=ParseMode.HTML)
    
    unrecognized_zero(chat_id)

# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #

def src_dest_menu_markup(mode: str, chat_id: int):
    buttons = []
    for key, val in LANGUAGES_MENU.items():
        text = "%s %s" % (key, val)
        callback_data = "%s %s %s" % (MENU, mode, key)
        buttons += [InlineKeyboardButton(text=text , callback_data=callback_data)]
    
    if mode == SRC:
        pattern = [[buttons[0], buttons[1]], [buttons[2], buttons[3]]]
    else:
        pattern = [[buttons[1]], [buttons[2], buttons[3]]]
    
    markup = InlineKeyboardMarkup(pattern)
    return markup

def src_dest_query(update: Update, context: CallbackContext, mode: str) -> None:
    chat_id = update.message.chat_id
    chat_data = Data.update(chat_id)
    
    if chat_data[chat_id][QUERIES][mode] != -1:
        try:
            update.message.bot.deleteMessage(chat_id=chat_id, message_id=chat_data[chat_id][QUERIES][mode])
        except:
            pass
    
    markup = src_dest_menu_markup(mode, chat_id)
    query = update.message.reply_text(SRC_DEST_QUERY_MESSAGE[mode], reply_markup=markup)
    query_id = query.message_id
    
    chat_data[chat_id][QUERIES][mode] = query_id
    chat_data[chat_id][QUERIES][LAST][ID] = query_id
    chat_data[chat_id][QUERIES][LAST][POINTER] = mode
    Data.write(chat_data)
    
    unrecognized_zero(chat_id)
    
def src_query(update: Update, context: CallbackContext) -> None:
    src_dest_query(update, context, SRC)

def dest_query(update: Update, context: CallbackContext) -> None:
    src_dest_query(update, context, DEST)

# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #

def other_markup(mode: str):
    buttons = []
    for key, val in languages.items():
        text = "%s:  %s %s" % (key, val[0], val[1])
        callback_data = "%s %s %s" % (OTHER, mode, key)
        buttons += [InlineKeyboardButton(text=text , callback_data=callback_data)]
    
    pattern = []
    for i in range(len(buttons)):
        if i % 2 == 0:  pattern += [[buttons[i]]]
        else:           pattern[-1] += [buttons[i]]
        
    markup = InlineKeyboardMarkup(pattern)
    return markup

def other_query(update: Update, context: CallbackContext, mode: str) -> None:
    markup = other_markup(mode)
    update.callback_query.message.edit_text(SRC_DEST_QUERY_MESSAGE[mode], reply_markup=markup)

# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #

def favorites_markup(mode: str, chat_id: int):
    chat_data = Data.update(chat_id)
    
    favs = chat_data[chat_id][FAV][mode]
    len_favs = len(favs)
    if len_favs == 0:
        return False
    
    buttons = []
    for key in favs:
        val = languages[key]
        text = "%s:  %s %s" % (key, val[0], val[1])
        callback_data = "%s %s %s" % (FAV, mode, key)
        buttons += [InlineKeyboardButton(text=text , callback_data=callback_data)]
    
    pattern = []
    for i in range(len(buttons)):
        if i % 2 == 0:  pattern += [[buttons[i]]]
        else:           pattern[-1] += [buttons[i]]
        
    markup = InlineKeyboardMarkup(pattern)
    return markup

def favorites_query(update: Update, context: CallbackContext, mode: str) -> bool:
    chat_id = update.callback_query.from_user.id
    markup = favorites_markup(mode, chat_id)
    if markup == False:
        text = NO_FAVORITES_COMMAND_MESSAGE % COMPLETE_SRC_DEST[mode]
        update.callback_query.message.edit_text(text, parse_mode=ParseMode.HTML)
        return False
    else:
        update.callback_query.message.edit_text(SRC_DEST_QUERY_MESSAGE[mode], reply_markup=markup)
        return True

# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #

def recents_markup(mode: str, chat_id: int):
    chat_data = Data.update(chat_id)
    
    recently = chat_data[chat_id][RECENT][mode]
    len_recently = len(recently)
    if len_recently == 0:
        return False
    
    buttons = []
    for key in recently:
        val = languages[key]
        text = "%s:  %s %s" % (key, val[0], val[1])
        callback_data = "%s %s %s" % (RECENT, mode, key)
        buttons += [InlineKeyboardButton(text=text , callback_data=callback_data)]
    
    pattern = []
    for i in range(len(buttons)):
        if i % 2 == 0:  pattern += [[buttons[i]]]
        else:           pattern[-1] += [buttons[i]]
        
    keyboard = InlineKeyboardMarkup(pattern)
    return keyboard

def recents_query(update: Update, context: CallbackContext, chat_id: int, mode: str) -> bool:
    keyboard = recents_markup(mode, chat_id)
    if keyboard == False:
        text = NO_RECENT_COMMAND_MESSAGE % COMPLETE_SRC_DEST[mode]
        update.callback_query.message.edit_text(text, parse_mode=ParseMode.HTML)
        return False
    else:
        update.callback_query.message.edit_text(SRC_DEST_QUERY_MESSAGE[mode], reply_markup=keyboard)
        return True

# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #

def favorites_setting_query(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    chat_data = Data.update(chat_id)
    
    last_fav_set = chat_data[chat_id][QUERIES][FAV_SETTING]
    
    if last_fav_set != -1:
        try:
            update.message.bot.deleteMessage(chat_id=chat_id, message_id=last_fav_set)
        except:
            pass
    
    buttons = [InlineKeyboardButton(text=COMPLETE_SRC_DEST[mode] , callback_data="%s 0 %s" % (FAV_SETTING, mode)) for mode in [SRC, DEST]]
    markup = InlineKeyboardMarkup([buttons])
    query = update.message.reply_text(FAV_SETTING_COMMAND_MESSAGE, reply_markup=markup)
    query_id = query.message_id
    
    chat_data[chat_id][QUERIES][FAV_SETTING] = query_id
    chat_data[chat_id][QUERIES][LAST][ID] = query_id
    chat_data[chat_id][QUERIES][LAST][POINTER] = FAV_SETTING
    Data.write(chat_data)
    
    unrecognized_zero(chat_id)

def favorite_setting_operation_query(update: Update, context: CallbackContext, mode: str, chat_id: int) -> None:
    buttons = [InlineKeyboardButton(text="%s %s"%(VIEW, VIEW_EMOJI) , callback_data="%s 1 %s %s" % (FAV_SETTING, mode, VIEW)),
               InlineKeyboardButton(text="%s %s"%(ADD, ADD_EMOJI) , callback_data="%s 1 %s %s" % (FAV_SETTING, mode, ADD)),
               InlineKeyboardButton(text="%s %s"%(REMOVE, REMOVE_EMOJI) , callback_data="%s 1 %s %s" % (FAV_SETTING, mode, REMOVE))]
    
    pattern = [[buttons[0]], [buttons[1], buttons[2]]]
    
    keyboard = InlineKeyboardMarkup(pattern)
    update.callback_query.message.edit_text(FAV_SETTING_COMMAND_MESSAGE, reply_markup=keyboard)

def favorites_add_remove_markup(mode: str, operation: str, chat_id: int):
    chat_data = Data.update(chat_id)
    favs = chat_data[chat_id][FAV][mode]
    
    buttons = []
    
    if operation == ADD:
        for key, val in languages.items():
            if key not in favs:
                text = "%s:  %s %s" % (key, val[0], val[1])
                callback_data = "%s 2 %s %s %s" % (FAV_SETTING, mode, operation, key)
                buttons += [InlineKeyboardButton(text=text , callback_data=callback_data)]
    
    elif operation == REMOVE:
        len_favs = len(favs)
        if len_favs == 0:
            return False
        
        for key in favs:
            val = languages[key]
            text = "%s:  %s %s" % (key, val[0], val[1])
            callback_data = "%s 2 %s %s %s" % (FAV_SETTING, mode, operation, key)
            buttons += [InlineKeyboardButton(text=text , callback_data=callback_data)]
    
    pattern = []
    for i in range(len(buttons)):
        if i % 2 == 0:
            pattern += [[buttons[i]]]
        else:
            pattern[-1] += [buttons[i]]
    
    markup = InlineKeyboardMarkup(pattern)
    return markup

def favorites_add_query(update: Update, context: CallbackContext, mode: str, chat_id: int) -> None:
    markup = favorites_add_remove_markup(mode, ADD, chat_id)
    update.callback_query.message.edit_text(FAV_SETTING_COMMAND_MESSAGE, reply_markup=markup)

def favorites_remove_query(update: Update, context: CallbackContext, mode: str, chat_id: int) -> bool:
    markup = favorites_add_remove_markup(mode, REMOVE, chat_id)
    if markup == False:
        text = NO_FAVORITES_COMMAND_MESSAGE % COMPLETE_SRC_DEST[mode]
        update.callback_query.message.edit_text(text=text, parse_mode=ParseMode.HTML)
        return False
    else:
        update.callback_query.message.edit_text(FAV_SETTING_COMMAND_MESSAGE, reply_markup=markup)
        return True

# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #

def query_handle(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    chat_id = query.from_user.id
    chat_data = Data.update(chat_id)
    
    selection = query.data.split()
    query_name = selection[0]
    
    if query.data == INLINE_MODE:
        src_language = chat_data[chat_id][SRC]
        dest_language = chat_data[chat_id][DEST]
        buttons = [[InlineKeyboardButton(INLINE_QUERY[0], switch_inline_query_current_chat = " ")],
                   [InlineKeyboardButton(INLINE_QUERY[1], switch_inline_query_current_chat = ". .%s " % dest_language)],
                   [InlineKeyboardButton(INLINE_QUERY[2], switch_inline_query_current_chat = ". . ")],
                   [InlineKeyboardButton(INLINE_QUERY[3], switch_inline_query_current_chat = ".%s .%s " % (src_language, dest_language))],
                   [InlineKeyboardButton(INLINE_QUERY[4], switch_inline_query_current_chat = ".%s . " % src_language)]]
        
        markup = InlineKeyboardMarkup(buttons)
        update.callback_query.message.edit_text(START_MESSAGE, reply_markup=markup)
    
    elif query_name == MENU:
        mode = selection[1]
        case = selection[2]
        if case == AUTO:
            chat_data[chat_id][mode] = case
            if chat_data[chat_id][QUERIES][LAST][ID] == chat_data[chat_id][QUERIES][mode]:
                chat_data[chat_id][QUERIES][LAST][ID] = -1
            chat_data[chat_id][QUERIES][mode] = -1
            
            text = selected_languages_message(chat_data, chat_id)
            query.edit_message_text(text=text, parse_mode=ParseMode.HTML)
            Data.write(chat_data)
        
        elif case == OTHER:
            other_query(update, context, mode)

        elif case == FAV:
            if not favorites_query(update, context, mode):
                if chat_data[chat_id][QUERIES][LAST][ID] == chat_data[chat_id][QUERIES][mode]:
                    chat_data[chat_id][QUERIES][LAST][ID] = -1
                chat_data[chat_id][QUERIES][mode] = -1
                Data.write(chat_data)
        
        elif case == RECENT:
            if not recents_query(update, context, chat_id, mode):
                if chat_data[chat_id][QUERIES][LAST][ID] == chat_data[chat_id][QUERIES][mode]:
                    chat_data[chat_id][QUERIES][LAST][ID] = -1
                chat_data[chat_id][QUERIES][mode] = -1
                Data.write(chat_data)
    
    elif query_name in [OTHER, FAV, RECENT]:
        mode = selection[1]
        lang = selection[2]
        chat_data[chat_id][mode] = lang
        if chat_data[chat_id][QUERIES][LAST][ID] == chat_data[chat_id][QUERIES][mode]:
            chat_data[chat_id][QUERIES][LAST][ID] = -1
        chat_data[chat_id][QUERIES][mode] = -1
        
        if lang in chat_data[chat_id][RECENT][mode]:
            chat_data[chat_id][RECENT][mode].remove(lang)
        chat_data[chat_id][RECENT][mode].insert(0, lang)
        chat_data[chat_id][RECENT][mode] = chat_data[chat_id][RECENT][mode][:10]
        
        text = selected_languages_message(chat_data, chat_id)
        query.edit_message_text(text=text, parse_mode=ParseMode.HTML)
        
        Data.write(chat_data)
    
    elif query_name == FAV_SETTING:
        step = selection[1]
        mode = selection[2]
        if step == "0":
            favorite_setting_operation_query(update, context, mode, chat_id)
        
        elif step == "1":
            case = selection[3]
            if case == VIEW:
                chat_data = Data.update(chat_id)
                favs = chat_data[chat_id][FAV][mode]
                if len(favs) == 0:
                    text = NO_FAVORITES_COMMAND_MESSAGE % COMPLETE_SRC_DEST[mode]
                else:
                    text = FAV_VIEW
                    for key in favs:
                        val = languages[key]
                        text += "%s:  %s %s\n" % (key, val[0], val[1])
                query.edit_message_text(text=text, parse_mode=ParseMode.HTML)
                if chat_data[chat_id][QUERIES][LAST][ID] == chat_data[chat_id][QUERIES][FAV_SETTING]:
                    chat_data[chat_id][QUERIES][LAST][ID] = -1
                chat_data[chat_id][QUERIES][FAV_SETTING] = -1
                Data.write(chat_data)
            
            elif case == ADD:
                favorites_add_query(update, context, mode, chat_id)
            
            elif not favorites_remove_query(update, context, mode, chat_id):
                if chat_data[chat_id][QUERIES][LAST][ID] == chat_data[chat_id][QUERIES][FAV_SETTING]:
                    chat_data[chat_id][QUERIES][LAST][ID] = -1
                chat_data[chat_id][QUERIES][FAV_SETTING] = -1
                Data.write(chat_data)
        
        elif step == "2":
            case = selection[3]
            lang = selection[4]
            if case == ADD:
                chat_data[chat_id][FAV][mode].insert(0, lang)
                chat_data[chat_id][FAV][mode] = chat_data[chat_id][FAV][mode][:10]
                text = FAV_ADD_MEASSAGE % (lang, languages[lang][1], COMPLETE_SRC_DEST[mode])
                
            elif case == REMOVE:
                chat_data[chat_id][FAV][mode].remove(lang)
                text = FAV_REMOVED_MEASSAGE % (lang, languages[lang][1], COMPLETE_SRC_DEST[mode])
            
            query.edit_message_text(text=text, parse_mode=ParseMode.HTML)
            
            if chat_data[chat_id][QUERIES][LAST][ID] == chat_data[chat_id][QUERIES][FAV_SETTING]:
                chat_data[chat_id][QUERIES][LAST][ID] = -1
            chat_data[chat_id][QUERIES][FAV_SETTING] = -1
            Data.write(chat_data)

# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #

def start(update: Update, context: CallbackContext) -> None:
    button = InlineKeyboardButton(INLINE_MODE, callback_data = INLINE_MODE)
    markup = InlineKeyboardMarkup([[button]])
    update.message.reply_text(START_MESSAGE, reply_markup=markup)

def swap(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    chat_data = Data.update(chat_id)
    
    if chat_data[chat_id][SRC] != AUTO:
        chat_data[chat_id][SRC], chat_data[chat_id][DEST] = chat_data[chat_id][DEST], chat_data[chat_id][SRC]
    
    text = selected_languages_message(chat_data, chat_id)
    update.message.reply_text(text, parse_mode=ParseMode.HTML)
    
    Data.write(chat_data)
    unrecognized_zero(chat_id)

def cancel(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    
    chat_data = Data.update(chat_id)
    last = chat_data[chat_id][QUERIES][LAST]
    if last[ID] != -1:
        try:
            update.message.bot.deleteMessage(chat_id=chat_id,message_id=last[ID])
        except:
            pass
        chat_data[chat_id][QUERIES][LAST][ID] = -1
        chat_data[chat_id][QUERIES][last[POINTER]] = -1
        Data.write(chat_data)
        text = CANCEL_COMMAND_MESSAGE % (FAV[:2] if last[POINTER] == FAV_SETTING else last[POINTER])
        update.message.reply_text(text, parse_mode=ParseMode.HTML)
    else:
        update.message.reply_text(NO_CANCEL_COMMAND_MESSAGE, parse_mode=ParseMode.HTML)
    
    unrecognized_zero(chat_id)

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(HELP_MESSAGE)
    
    chat_id = update.message.chat_id
    unrecognized_zero(chat_id)

def contact(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(CONTACT_MESSAGE)
    
    chat_id = update.message.chat_id
    unrecognized_zero(chat_id)

def error_callback(update: Update, context: CallbackContext) -> None:
    pass