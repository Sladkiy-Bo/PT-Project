from telebot import *
from timetable import *

bot = TeleBot("8007967743:AAELiSrZWevcnyLowxDzfWw6XoqUOLA90Dw")
tt = TimeTable("timetable.xlsx")
Wait_for_number = False


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Текущая пара"))
    bot.send_message(message.chat.id, "Привет!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_recieve(message):
    global Wait_for_number
    if Wait_for_number:
        bot.send_message(message.chat.id, tt.getclass(message.text))
        Wait_for_number = False
    elif message.text == "Текущая пара":
        bot.send_message(message.chat.id, "Введи номер своей группы КНТ")
        Wait_for_number = True

    print('here')


bot.polling(none_stop=True)