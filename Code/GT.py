from Consts import TOKEN, BOT_ID

import CMD
import Inline

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, InlineQueryHandler

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler(command="start", callback=CMD.start, filters=Filters.chat_type.private))
dispatcher.add_handler(CommandHandler(command="help", callback=CMD.help, filters=Filters.chat_type.private))
dispatcher.add_handler(CommandHandler(command="swap", callback=CMD.swap, filters=Filters.chat_type.private))
dispatcher.add_handler(CommandHandler(command="src", callback=CMD.src_query, filters=Filters.chat_type.private))
dispatcher.add_handler(CommandHandler(command="dest", callback=CMD.dest_query, filters=Filters.chat_type.private))
dispatcher.add_handler(CommandHandler(command="langs", callback=CMD.selected_languages, filters=Filters.chat_type.private))
dispatcher.add_handler(CommandHandler(command="fav", callback=CMD.favorites_setting_query, filters=Filters.chat_type.private))
dispatcher.add_handler(CommandHandler(command="cancel", callback=CMD.cancel, filters=Filters.chat_type.private))

dispatcher.add_handler(CommandHandler("contact", CMD.contact))

dispatcher.add_handler(CommandHandler(command="tr", callback=CMD.translate_inGroup, filters=Filters.chat_type.groups))
dispatcher.add_handler(MessageHandler(Filters.command & Filters.chat_type.private, CMD.unrecognized))

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command & ~Filters.via_bot(BOT_ID) & Filters.chat_type.private, CMD.translate))
dispatcher.add_handler(MessageHandler(Filters.document.category("text") & Filters.chat_type.private, CMD.translate_file))

dispatcher.add_handler(CallbackQueryHandler(CMD.query_handle))

dispatcher.add_handler(InlineQueryHandler(Inline.query))

dispatcher.add_error_handler(CMD.error_callback)

updater.start_polling()
updater.idle()
