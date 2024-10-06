import telebot
from telebot import types

token = '7928469956:AAGmWSoXunceWLw29iE7RVCmse3rwfgmC40'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    mess = f'Привет, {message.from_user.first_name}!'
    bot.send_message(message.chat.id, mess)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    main = types.KeyboardButton("Литература📚")
    markup.add(main)
    bot.send_message(message.chat.id, "Выберите то, что вас интересует:", reply_markup=markup)







@bot.message_handler(content_types=['text'])
def literature(message):
    if message.text == 'Литература📚':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Дискретная математика🤩",)
        item2 = types.KeyboardButton("Матанализ🥶")
        item3 = types.KeyboardButton("Программирование😎")
        item4 = types.KeyboardButton("Линейная алгебра🤯")
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, "Выберите тот предмет, по которому вам интересна литература:", reply_markup=markup)


    if message.text == 'Дискретная математика🤩':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Алексеев Дискретная математика")
        btn2 = types.KeyboardButton("Сборник задач")
        btn3 = types.KeyboardButton('"Начала теории множеств", Н. Верещагин')
        btn4 = types.KeyboardButton("Вернуться назад")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Выберите номер ту книгу, которая вам интересна:\n1. Учебник "Дискретная математика" В. E. Алексеев.\n2. Сборник задач по дискретной математике.\n3. "Начала теории множеств", Н. Верещагин и А. Шень.',reply_markup=markup)


    if message.text == 'Алексеев Дискретная математика':
        document = open('Алексеев Дискретная математика.pdf', 'rb')
        bot.send_message(message.chat.id, "Ваша книга/книги:")
        bot.send_document(message.chat.id, document=document)
        document.close()
        start_message(message)


    if message.text == 'Сборник задач':
        document1 = open("Задачник 1 часть (2019).pdf", 'rb')
        document2 = open("Задачник 2 часть (2023).pdf", 'rb')
        bot.send_message(message.chat.id, "Ваша книга/книги:")
        bot.send_document(message.chat.id, document=document1)
        bot.send_document(message.chat.id, document=document2)
        document1.close()
        document2.close()
        start_message(message)


    if message.text == '"Начала теории множеств", Н. Верещагин':
        document = open('Начала теории множеств Верещагин.pdf', 'rb')
        bot.send_message(message.chat.id, "Ваша книга/книги:")
        bot.send_document(message.chat.id, document=document)
        document.close()
        start_message(message)


    if message.text == 'Программирование😎':
        document = open('Kernighan_B_W_,_Ritchie_D_M_The_C_Programming_Language,_2nd_Edition.pdf', 'rb')
        bot.send_message(message.chat.id, "Ваша книга/книги:")
        bot.send_document(message.chat.id, document=document)
        document.close()
        start_message(message)


    if message.text == "Линейная алгебра🤯":
        document = open("линейная.pdf", 'rb')
        bot.send_message(message.chat.id, "Ваша книга/книги:")
        bot.send_document(message.chat.id, document=document)
        document.close()
        start_message(message)


    if message.text == "Матанализ🥶":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        key1 = types.KeyboardButton('Зорич "Математический анализ"')
        key2 = types.KeyboardButton('Фихтенгольц "Курс дифференциального и интегрального исчисления"')
        key3 = types.KeyboardButton('Кудрявцев "Сборник задач по математическому анализу"')
        markup.add(key1, key2, key3)
        bot.send_message(message.chat.id, 'Выберите номер той книги, которая вам интересна:\n1. Зорич "Математический анализ"   (2 тома).\n2. Фихтенгольц "Курс дифференциального и интегрального исчисления" (2 тома).\n3. Кудрявцев "Сборник задач по математическому анализу".', reply_markup=markup)


    if message.text == 'Зорич "Математический анализ"':
        document1 = open('Зорич 1 том.pdf', 'rb')
        document2 = open("Зорич 2 том.pdf", 'rb')
        bot.send_message(message.chat.id, "Ваша книга/книги:")
        bot.send_document(message.chat.id, document=document1)
        bot.send_document(message.chat.id, document=document2)
        document1.close()
        document2.close()
        start_message(message)


    if message.text == 'Фихтенгольц "Курс дифференциального и интегрального исчисления"':
        document1 = open('Фихтенгольц Курс дифференциального и интегрального исчисления 1 том.pdf', 'rb')
        document2 = open("Фихтенгольц Курс дифференциального и интегрального исчисления 2 том.pdf", 'rb')
        bot.send_message(message.chat.id, "Ваша книга/книги:")
        bot.send_document(message.chat.id, document=document1)
        bot.send_document(message.chat.id, document=document2)
        document1.close()
        document2.close()
        start_message(message)


    if message.text == 'Кудрявцев "Сборник задач по математическому анализу"':
        document = open("Кудрявцев Сборник задач по матанализу.pdf", 'rb')
        bot.send_message(message.chat.id, "Ваша книга/книги:")
        bot.send_document(message.chat.id, document=document)
        document.close()
        start_message(message)

bot.infinity_polling()

