import telebot
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("❌ TOKEN не найден в .env faylda")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "🤖 Echo botga xush kelibsiz!\nNima yozsangiz, o‘sha narsa qaytadi 😉")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

print("✅ Bot ishga tushdi...")
bot.polling(none_stop=True)
