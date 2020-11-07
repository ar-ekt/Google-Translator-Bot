from Emojies import *


# T O K E N
# Keep your TOKEN secure and store it safely
TOKEN = "TOKEN"
BOT_ID = int(TOKEN[:TOKEN.index(":")])


# S I Z E S
MAX_FILE_SIZE = 51200
LEN_LANGUAGES = 100


# F I L E S
TEMP_FILE = "temp.txt"
CHAT_DATA_FILE = "chat_data.txt"


# O T H E R
EN = "en"
FA = "fa"
SRC = "src"
DEST = "dest"
COMPLETE_SRC_DEST = {SRC: "Source", DEST: "Destination"}

FAV_VIEW = "<b>Favorites:</b>\n"
UNRECOGNIZED = "unrecognized"
INLINE_MODE = "inline mode"
FAV_SETTING = "fav_set"
QUERIES = "queries"
POINTER = "pointer"
REMOVE = "remove"
RECENT = "recent"
FAV = "favorites"
OTHER = "others"
VIEW = "view"
AUTO = "auto"
LAST = "last"
MENU = "menu"
ADD = "add"
DOT = "."
ID = "id"


# M E S S A G E S
SELECTED_LANGUAGES_MESSAGE = "<b>%s</b> %s to <b>%s</b> %s"

FILE_TRANSLATE_FAILURE = "I can not translate this file %s" % SAD_EMOJI
TEXT_TRANSLATE_FAILURE = "I can not translate this text %s" % SAD_EMOJI

SRC_COMMAND_MESSAGE = "Source language:"
DEST_COMMAND_MESSAGE = "Destination language:"
SRC_DEST_QUERY_MESSAGE = {SRC: SRC_COMMAND_MESSAGE,
                          DEST: DEST_COMMAND_MESSAGE}

FAV_SETTING_COMMAND_MESSAGE = "Favorites setting:"
FAV_REMOVED_MEASSAGE = "<b>%s</b> %s removed from <b>%s</b> favorites"
FAV_ADD_MEASSAGE = "<b>%s</b> %s added to <b>%s</b> favorites"

NO_FAVORITES_COMMAND_MESSAGE = "You currently have no <b>%s</b> favorites"
NO_RECENTLY_COMMAND_MESSAGE = "You currently have no <b>%s</b> recents"

CANCEL_COMMAND_MESSAGE = "The /%s command has been cancelled"
NO_CANCEL_COMMAND_MESSAGE = "No active command to cancel %s" % SLEEP_EMOJI

UNRECOGNIZED_MESSAGES = ["Unrecognized command. Use /help",
                         "It's not a correct command! Use /help",
                         "WTF! %s" % NEUTRAL_FACE_EMOJI,
                         "What do you want?!",
                         "Maybe you are a bot too! %s" % COUPLE_EMOJI,
                         "/contact me %s" % CALL_ME_EMOJI,
                         "It's the end. Use /help",
                         "Are youuuuu kidding me?!!!! No more"]
UNRECOGNIZED_LEN = len(UNRECOGNIZED_MESSAGES)

FILE_SIZE_ERROR = "I do not support files larger than %d KB" % (MAX_FILE_SIZE // 1024)

START_MESSAGE = "%s Use /help for help\n\n" \
                "%s /contact\n\n" \
                "%s Send a message or a .txt file to get the translation back\n\n" \
                "%s Also you can use inline mode" % (GLOBE_EMOJI, SLOTH_EMOJI, GLOBE_EMOJI, GLOBE_EMOJI)

CONTACT_MESSAGE = "Contact with admin:\n" \
                  "Telegram: t.me/Ar_ekt\n" \
                  "Github: github.com/ar-ekt\n" \
                  "Twitter: twitter.com/ar__ekt"

HELP_MESSAGE = "- /start:  Start\n" \
               "- /swap:  Swap source and destination languages\n" \
               "- /src:  Change source language (auto for detect language)\n" \
               "- /dest:  Change destination language\n" \
               "- /langs:  Show selected languages\n" \
               "- /fav:  Favorites setting (add or remove languages from favorites lists)\n" \
               "- /cancel:  Cancel the current operation\n" \
               "- /contact:  Contact with admin %s" % SLOTH_EMOJI

INLINE_QUERY = ["Your selected languages",
                "Auto to destination",
                "Auto to favorites",
                "Source to destination",
                "Source to favorites"]

LANGUAGES_MENU = {AUTO: AUTO_EMOJI,
                  OTHER: WHITE_FLAG_EMOJI,
                  FAV: STAR_EMOJI,
                  RECENT: CLOCK_EMOJI}

DEFAULT_USER_DATA = {SRC: EN,
                     DEST: FA,
                     FAV: {SRC: [], DEST: []},
                     RECENT: {SRC: [], DEST: []},
                     UNRECOGNIZED: [0, "", 0],
                     QUERIES: {SRC: -1, DEST: -1, FAV_SETTING: -1, LAST: {ID: -1, POINTER: ""}}}