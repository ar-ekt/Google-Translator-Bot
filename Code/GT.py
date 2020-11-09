from Consts import TOKEN, BOT_ID

import CMD
import Inline

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, InlineQueryHandler

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", CMD.start))
dispatcher.add_handler(CommandHandler("help", CMD.help))
dispatcher.add_handler(CommandHandler("swap", CMD.swap))
dispatcher.add_handler(CommandHandler("src", CMD.src_query))
dispatcher.add_handler(CommandHandler("dest", CMD.dest_query))
dispatcher.add_handler(CommandHandler("langs", CMD.selected_languages))
dispatcher.add_handler(CommandHandler("fav", CMD.favorites_setting_query))
dispatcher.add_handler(CommandHandler("cancel", CMD.cancel))
dispatcher.add_handler(CommandHandler("contact", CMD.contact))

dispatcher.add_handler(MessageHandler(Filters.command, CMD.unrecognized))

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command & ~Filters.via_bot(BOT_ID), CMD.translate))
dispatcher.add_handler(MessageHandler(Filters.document.category("text"), CMD.translate_file))

dispatcher.add_handler(CallbackQueryHandler(CMD.query_handle))

dispatcher.add_handler(InlineQueryHandler(Inline.query))

dispatcher.add_error_handler(CMD.error_callback)

updater.start_polling()
updater.idle()