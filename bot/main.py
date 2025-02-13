import telebot
import os
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(msg: telebot.types.Message):
    resposta = (
        "🌿 Bem-vindo ao Mente Segura! 🌿\n\n"
        "Como podemos te ajudar hoje?\n\n"
        "1️⃣ Dicas para bem-estar emocional 🧘‍♂️\n"
        "2️⃣ Técnicas para reduzir a ansiedade 😌\n"
        "3️⃣ Contato com profissionais de apoio 📞\n"
        "4️⃣ Informações sobre saúde mental 📖\n\n"
        "Digite o número ou a opção desejada."
    )
    bot.reply_to(msg, resposta)

bot.infinity_polling()
