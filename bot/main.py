import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(msg: telebot.types.Message):
    resposta = (
        "Bem-vindo ao Mente Segura!\n\n"
        "Como podemos te ajudar hoje?\n"
        "- Selecione uma opção abaixo:"
    )

    markup = InlineKeyboardMarkup(row_width=2)

    btn1 = InlineKeyboardButton("📌 AVALIAÇÃO", callback_data="avaliação")
    btn2 = InlineKeyboardButton("⚙️ PLATAFORMA", callback_data="plataforma")
    btn3 = InlineKeyboardButton("🔝 EMERGÊNCIA", callback_data="emergência")
    btn4 = InlineKeyboardButton("🔗 DATALINK", callback_data="datalink")

    markup.add(btn1, btn2)
    markup.add(btn3, btn4)

    bot.send_message(msg.chat.id, resposta, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    respostas = {
        "avaliação": "Você selecionou ABREVIADO. Aqui estão os detalhes...",
        "plataforma": "Você selecionou PLATAFORMA. Aqui estão os detalhes...",
        "emergência":
            "📞 **Se precisar conversar, o CVV está disponível 24h!**\n\n"
            "💬 **Chat:** [www.cvv.org.br](https://www.cvv.org.br) \n"
            "📞 **Telefone:** 188 (ligação gratuita)\n"
            "📧 **E-mail:** atendimento@cvv.org.br\n\n"
            "_O CVV oferece apoio emocional e prevenção ao suicídio com sigilo e anonimato._",
            "datalink": "Você selecionou DATALINK. Aqui estão os detalhes...",
    }

    resposta = respostas.get(call.data, "Opção inválida.")
    bot.send_message(call.message.chat.id, resposta)

bot.infinity_polling()