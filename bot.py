import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

# Token do bot carregado diretamente da variável de ambiente
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Verificação do token
if not TOKEN:
    raise ValueError("Erro: Token do bot não encontrado. Certifique-se de configurá-lo no Railway.")

# Função para exibir o menu principal
async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Quem Sou", callback_data="quem_sou")],
        [InlineKeyboardButton("LinkedIn", url="https://www.linkedin.com/in/maurolucasesteves/")],
        [InlineKeyboardButton("WhatsApp", url="https://api.whatsapp.com/send/?phone=5518996861195&text=Mauro%20Lucas%20Esteves,%20(*L*)%20Seja%20Bem%20Vindo!&type=phone_number&app_absent=0")],
        [InlineKeyboardButton("Como posso te Ajudar", callback_data="como_ajudar")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Escolha uma opção:", reply_markup=reply_markup)

# Função para lidar com os botões do menu
async def button_callback(update, context):
    query = update.callback_query
    await query.answer()

    if query.data == "quem_sou":
        keyboard = [[InlineKeyboardButton("Voltar ao menu principal", callback_data="menu_principal")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="Consultor de Tecnologias de Informação e Analista de Suporte. Saiba mais em: [Meu Site](https://www.maurolucasesteves.com.br)",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
    elif query.data == "como_ajudar":
        keyboard = [[InlineKeyboardButton("Voltar ao menu principal", callback_data="menu_principal")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="Pode enviar para meu email: contato@maurolucasesteves.com.br",
            reply_markup=reply_markup
        )
    elif query.data == "menu_principal":
        await start(update.callback_query, context)

def main():
    # Cria a aplicação
    application = Application.builder().token(TOKEN).build()

    # Adiciona os handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))

    # Executa o bot
    application.run_polling()

if __name__ == "__main__":
    main()
