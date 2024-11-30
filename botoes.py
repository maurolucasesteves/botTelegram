from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Quem Sou", callback_data="quem_sou")],
        [InlineKeyboardButton("LinkedIn", url="https://www.linkedin.com/in/maurolucasesteves/")],
        [InlineKeyboardButton("WhatsApp", url="https://wa.me/18996861195")],
        [InlineKeyboardButton("Consultar Editais", callback_data="consultar_editais")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Escolha uma opção:", reply_markup=reply_markup)

def button_callback(update, context):
    query = update.callback_query
    query.answer()

    if query.data == "quem_sou":
        query.edit_message_text(text="Sou um Analista de Suporte e Especialista em Infraestrutura de TI...")
    elif query.data == "consultar_editais":
        query.edit_message_text(text="Aqui estão os editais de mestrado mais recentes: [Link para Editais](http://exemplo.com)")

def main():
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button_callback))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
