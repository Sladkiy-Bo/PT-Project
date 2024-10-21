import telebot
from timetable import *
import telebot
from telebot import types
import random

bot = telebot.TeleBot('8007967743:AAELiSrZWevcnyLowxDzfWw6XoqUOLA90Dw')
tt = TimeTable("timetable.xlsx")
Wait_for_number = False




@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Литература📚")
    btn2 = types.KeyboardButton("Интересные места")
    lit = types.KeyboardButton("Расписание")
    hah = types.KeyboardButton("Расслабиться")
    markup.add(btn1, btn2, lit, hah)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Выбери тот раздел, которым интересуешься:".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(commands=['магазины'])
def bpsh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bts1 = types.KeyboardButton("Spar Express [6 минут]")
    bts2 = types.KeyboardButton("ВкусВилл [6 минут]")
    bts3 = types.KeyboardButton("Spar Express [10 минут]")
    bts4 = types.KeyboardButton("Eurospar [12 минут]")
    bts5 = types.KeyboardButton("Авокадо [12 минут]")
    back = types.KeyboardButton("Не хочу")
    markup.add(bts1, bts2, bts3, bts4, bts5, back)
    bot.send_message(message.chat.id, text="Выбери нужное место:", reply_markup=markup)


@bot.message_handler(commands=['мaгазины'])
def lvst(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lvs1 = types.KeyboardButton("1000 мелочей [10 минут]")
    lvs2 = types.KeyboardButton("Тортила [9 минут]")
    lvs3 = types.KeyboardButton("Южный [9 минут]")
    lvs4 = types.KeyboardButton("Аккумуляторы.рф [5 минут]")
    lvs5 = types.KeyboardButton("Ежик [4 минуты]")
    back = types.KeyboardButton("Давай назад")
    markup.add(lvs1, lvs2, lvs3, lvs4, lvs5, back)
    bot.send_message(message.chat.id, text="Выбери нужное место:", reply_markup=markup)




@bot.message_handler(commands=['кафе'])
def bpkf(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bts1 = types.KeyboardButton("Мускат [2 минуты]")
    bts2 = types.KeyboardButton("Coffee like [4 минуты]")
    bts3 = types.KeyboardButton("Nuga [6 минут]")
    bts4 = types.KeyboardButton("Cofee like [7 минут]")
    bts5 = types.KeyboardButton("Закрома [8 минут]")
    bts6 = types.KeyboardButton("Кунг-фу Панда [10 минут]")
    back = types.KeyboardButton("Не хочу")
    markup.add(bts1, bts2, bts3, bts4, bts5, bts6, back)
    bot.send_message(message.chat.id, text="Выбери нужное место:", reply_markup=markup)

@bot.message_handler(commands=['кaфе'])
def lvkf(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lvs1 = types.KeyboardButton("Шашлык на Львовской [5 минут]")
    lvs2 = types.KeyboardButton("Донар по-турецки [10 минут]")
    lvs3 = types.KeyboardButton("Гермес [12 минут]")
    back = types.KeyboardButton("Давай назад")
    markup.add(lvs1, lvs2, lvs3, back)
    bot.send_message(message.chat.id, text="Выбери нужное место:", reply_markup=markup)



@bot.message_handler(commands=['рестораны'])
def bpre(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bts1 = types.KeyboardButton("Мускат [2 минуты]")
    bts2 = types.KeyboardButton("Печёрка [6 минут]")
    bts3 = types.KeyboardButton("Amo restaurant [6 минут]")
    bts4 = types.KeyboardButton("Vishnevsky Gastronomic Club [6 минут]")
    bts5 = types.KeyboardButton("Колхида [10 минут]")
    back = types.KeyboardButton("Не хочу")
    markup.add(bts1, bts2, bts3, bts4, bts5, back)
    bot.send_message(message.chat.id, text="Выбери нужное место:", reply_markup=markup)

@bot.message_handler(commands=['аптеки'])
def bpap(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bts1 = types.KeyboardButton("Солнечное здоровье [6 минут]")
    bts2 = types.KeyboardButton("Вита [8 минут]")
    bts3 = types.KeyboardButton("Солнечное здоровье [10 минут]")
    bts4 = types.KeyboardButton("Farmani [12 минут]")
    bts5 = types.KeyboardButton("Farmani 2 [12 минут]")
    back = types.KeyboardButton("Не хочу")
    markup.add(bts1, bts2, bts3, bts4, bts5, back)
    bot.send_message(message.chat.id, text="Выбери нужное место:", reply_markup=markup)

@bot.message_handler(commands=['aптеки'])
def lvap(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lvs1 = types.KeyboardButton("Максавит [9 минут]")
    lvs2 = types.KeyboardButton("Эконом [9 минут]")
    lvs3 = types.KeyboardButton("Вита Express [9 минут]")
    back = types.KeyboardButton("Давай назад")
    markup.add(lvs1, lvs2, lvs3, back)
    bot.send_message(message.chat.id, text="Выбери нужное место:", reply_markup=markup)

@bot.message_handler(commands=['канцтовары'])
def bpkn(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bts1 = types.KeyboardButton("Магазин канцтоваров [7 минут]")
    bts2 = types.KeyboardButton("ПалитраНН [7 минут]")
    bts3 = types.KeyboardButton("Канцпарк [9 минут]")
    bts4 = types.KeyboardButton("Дырокол [11 минут]")
    back = types.KeyboardButton("Не хочу")
    markup.add(bts1, bts2, bts3, bts4, back)
    bot.send_message(message.chat.id, text="Выбери нужное место:", reply_markup=markup)

@bot.message_handler(commands=['кaнцтовары'])
def lvkn(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lvs1 = types.KeyboardButton("AF152 [9 минут]")
    back = types.KeyboardButton("Давай назад")
    markup.add(lvs1, back)
    bot.send_message(message.chat.id, text="Выбери нужное место:", reply_markup=markup)

@bot.message_handler(commands=["пункты","выдачи"])
def lvpk(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lvs1 = types.KeyboardButton("Яндекс.Маркет [9 минут]")
    lvs2 = types.KeyboardButton("Wildberries-1 [9 минут]")
    lvs3 = types.KeyboardButton("Wildberries-2 [4 минуты]")
    lvs4 = types.KeyboardButton("Ozon [9 минут]")
    lvs5 = types.KeyboardButton("Аквамарин [9 минут]")
    lvs6 = types.KeyboardButton("Почта России [13 минут]")
    back = types.KeyboardButton("Давай назад")
    markup.add(lvs1,lvs2,lvs3,lvs4,lvs5,lvs6, back)
    bot.send_message(message.chat.id, text="Выбери нужное место:", reply_markup=markup)

@bot.message_handler(commands=["салоны","красоты"])
def lvsk(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lvs1 = types.KeyboardButton("Х@чу стрижку [9 минут]")
    lvs2 = types.KeyboardButton("Триумф [4 минуты]")
    lvs3 = types.KeyboardButton("Пальмира [9 минут]")
    lvs4 = types.KeyboardButton("Алмар [5 минут]")
    lvs5 = types.KeyboardButton("Nogotochki_nnov [10 минут]")
    back = types.KeyboardButton("Давай назад")
    markup.add(lvs1, lvs2, lvs3, lvs4, lvs5, back)
    bot.send_message(message.chat.id, text="Выбери нужное место:", reply_markup=markup)






@bot.message_handler(commands=['Узнать_расписание'])
def text_recieve(message):
    global Wait_for_number
    bot.send_message(message.chat.id, "Введи номер своей группы КНТ")
    Wait_for_number = True






@bot.message_handler(commands=['фразы_преподавателей'])
def frases_of_teachers(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    taletskii = types.KeyboardButton("Дмитрий Талецкий")
    peplin = types.KeyboardButton("Фёдор Пеплин")
    shmelev = types.KeyboardButton("Алексей Шмелёв")
    cap = types.KeyboardButton("Екатерина Цаплина")
    students = types.KeyboardButton("Студенты")
    back = types.KeyboardButton("Вернуться в главное меню")

    markup.add(taletskii, peplin, shmelev, students, cap, back)
    bot.send_message(message.chat.id, text="Выберите ФИО преподавателя:", reply_markup=markup)

@bot.message_handler(commands=['жизненные_мемы'])
def memes_of_shiza(message):
    random_number = random.randint(0, 9)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if random_number == 0:
        photo = open('006ad43d-4324-4f7c-a5c8-39cb027f48c9.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo)
    elif random_number == 1:
        photo = open('2a7e0afa-6456-46ee-9262-0195dae04243.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo)
    elif random_number == 2:
        photo = open('420d84fe-dfdf-4a35-af52-25c4f2353486.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo)
    elif random_number == 3:
        photo = open('7c68da12-1bda-4460-a0b7-a08bda4b95b3.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo)
    elif random_number == 4:
        photo = open('94c7e669-90a1-46db-854b-62ea663be837.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo)
    elif random_number == 5:
        photo = open('9fbcca56-83d3-4ab8-8daf-8025a2047032.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo)
    elif random_number == 6:
        photo = open('e971151c-c3c9-4907-9259-72cbaec3f1ed.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo)
    elif random_number == 7:
        photo = open('ebf40f0a-02af-4854-99bd-67b53c5fab5d.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo)
    elif random_number == 8:
        photo = open('Снимок экрана 2024-10-20 100451.png', 'rb')
        bot.send_photo(message.chat.id, photo=photo)
    elif random_number == 9:
        photo = open('Снимок экрана 2024-10-20 101733.png', 'rb')
        bot.send_photo(message.chat.id, photo=photo)



@bot.message_handler(content_types=['text'])
def func(message):
    global Wait_for_number
    if Wait_for_number:
        bot.send_message(message.chat.id, tt.getclass(message.text))
        Wait_for_number = False
    if (message.text == "Интересные места"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("На Большой Печёрской")
        btn2 = types.KeyboardButton("На Львовской")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Я помогу тебе найти самые классные места в округе! Для этого выбери корпус, в котором ты сейчас находишься :)", reply_markup=markup)
    elif (message.text == "На Большой Печёрской"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/магазины")
        btn2 = types.KeyboardButton("/кафе")
        btn3 = types.KeyboardButton("/рестораны")
        btn4 = types.KeyboardButton("/аптеки")
        btn5 = types.KeyboardButton("/канцтовары")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="Выбери нужную категорию:", reply_markup=markup)
    elif (message.text == "На Львовской"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        lv1 = types.KeyboardButton("/мaгазины")
        lv2 = types.KeyboardButton("/кaфе")
        lv3 = types.KeyboardButton("/aптеки")
        lv4 = types.KeyboardButton("/кaнцтовары")
        lv5 = types.KeyboardButton("/пункты выдачи")
        lv6 = types.KeyboardButton("/салоны красоты")
        baback = types.KeyboardButton("Вернуться в главное меню")
        markup.add(lv1, lv2, lv3, lv4, lv5, lv6, baback)
        bot.send_message(message.chat.id, text="Выбери нужную категорию:", reply_markup=markup)

    elif (message.text == "1000 мелочей [10 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/1jtSEp3KTtAErQ7f9')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Тортила [9 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/CGRKpb9ewYhs5yHo8')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Южный [9 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/WYMKqPfGz3PXgPiJA')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Ежик [4 минуты]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/pMwUXzWhzobLSDzc8')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Аккумуляторы.рф [5 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/YaMxcEZfnyarEtHDA')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Давай назад"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        lv1 = types.KeyboardButton("/мaгазины")
        lv2 = types.KeyboardButton("/кaфе")
        lv3 = types.KeyboardButton("/aптеки")
        lv4 = types.KeyboardButton("/кaнцтовары")
        lv5 = types.KeyboardButton("/пункты выдачи")
        lv6 = types.KeyboardButton("/салоны красоты")
        baback = types.KeyboardButton("Вернуться в главное меню")
        markup.add(lv1, lv2, lv3, lv4, lv5, lv6, baback)
        bot.send_message(message.chat.id, text="Выбери нужную категорию:", reply_markup=markup)
    elif (message.text == "Шашлык на Львовской [5 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/hcigjdC1yDE8ngaw5')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Донар по-турецки [10 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/7EoPMMTMtchnJ1Ys7')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Гермес [12 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/1UWii9kV7ZZaZA2s5')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Максавит [9 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/WYMKqPfGz3PXgPiJA')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Эконом [9 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/WYMKqPfGz3PXgPiJA')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Вита Express [9 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/WYMKqPfGz3PXgPiJA')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Яндекс.Маркет [9 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/WYMKqPfGz3PXgPiJA')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Wildberries-1 [9 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/WYMKqPfGz3PXgPiJA')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Wildberries-2 [4 минуты]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/mSwS3WQ8Z2qhHFTw8')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Ozon [9 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/WYMKqPfGz3PXgPiJA')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Аквамарин [9 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/WYMKqPfGz3PXgPiJA')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Почта России [13 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/GGXkyHRydL6X3HTV8')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
        # КАНЦТОВАРЫ
    elif (message.text == "Магазин канцтоваров [7 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/D5xHA3SzXfiPeMuA6')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "ПалитраНН [7 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/M2X6LSTkGbBQpWJh9')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Канцпарк [9 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/UDzGchKy5MdyKNaGA')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Дырокол [11 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/4jAZTJRsNFGP2naD9')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "AF152 [9 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/mLw4xASfrpLF8zyj9')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Х@чу стрижку [9 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/WYMKqPfGz3PXgPiJA')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Триумф [4 минуты]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/Tr55mCQxtfeyUYoi7')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Пальмира [9 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/HgezsuC5Q2ZdTbTo7')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Алмар [5 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/ARk4VkvmojScFqtRA')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Nogotochki_nnov [10 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/6DpgHTDy68mGcLpq8')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)









    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Литература📚")
        btn2 = types.KeyboardButton("Интересные места")
        lit = types.KeyboardButton("Расписание")
        hah = types.KeyboardButton("Расслабиться")
        markup.add(btn1, btn2, lit, hah)
        bot.send_message(message.chat.id, text="Без проблем, вернёмся обратно. Выбери тот раздел, которым интересуешься:", reply_markup=markup)
    elif (message.text == "Ой, ну ладно..."):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("На Большой Печёрской")
        button2 = types.KeyboardButton("На Львовской")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2, back)
        bot.send_message(message.chat.id, text="Выбери место заново:", reply_markup=markup)
    elif (message.text == "Не хочу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/магазины")
        btn2 = types.KeyboardButton("/кафе")
        btn3 = types.KeyboardButton("/рестораны")
        btn4 = types.KeyboardButton("/аптеки")
        btn5 = types.KeyboardButton("/канцтовары")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="Выбери нужную категорию:", reply_markup=markup)
        #МАГАЗИНЫ
    elif (message.text == "Spar Express [6 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/cQefLHDBE2FZ4Ydf8')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "ВкусВилл [6 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/zq6n2GEKmJjgtGc46')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Eurospar [12 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/fB572xCT5Tf7bovw8')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Spar Express [10 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/xbmycikTjB8BhgcW8')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Авокадо [12 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/AfGu3zRsUKoCuDK77')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
        #КАФЕ
    elif (message.text == "Мускат [2 минуты]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/Xf8gzJLu1kqKzKx38')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Coffee like [4 минуты]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/XzL7uLAk5CQrn9r29')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Nuga [6 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/6KR1J67Ddzh6LwG36')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Cofee like [7 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/Yc3PH9oeVJLsGDLF8')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Закрома [8 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/Gi1EDe5ziSihgY8h9')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Кунг-фу Панда [10 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/abpU8cCWG6rTMTSh9')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
        #РЕСТОРАНЫ
        #Мускат
    elif (message.text == "Печёрка [6 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/8e6Sykm41mgc4fxu7')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Amo restaurant [6 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/2U5DwZeKif9okZX16')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Vishnevsky Gastronomic Club [6 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/2U5DwZeKif9okZX16')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Колхида [10 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/iDG3gnVhyx8hn4XQA')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
        #АПТЕКИ
    elif (message.text == "Солнечное здоровье [6 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/N8TjRncbbMPvqZV68')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Вита [8 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/cbWhvnRNYLpnCLmG7')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Солнечное здоровье [10 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/69vjg1P9kv55JVNt9')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Farmani [12 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/fB572xCT5Tf7bovw8')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Farmani 2 [12 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/PyikTYJP71yCfhyX6')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
        #КАНЦТОВАРЫ
    elif (message.text == "Магазин канцтоваров [7 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/D5xHA3SzXfiPeMuA6')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "ПалитраНН [7 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/M2X6LSTkGbBQpWJh9')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Канцпарк [9 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/UDzGchKy5MdyKNaGA')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)
    elif (message.text == "Дырокол [11 минут]"):
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://maps.app.goo.gl/4jAZTJRsNFGP2naD9')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятно провести время :)', reply_markup=keyboard)





    elif message.text == 'Литература📚':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Дискретная математика🤩",)
        item2 = types.KeyboardButton("Матанализ🥶")
        item3 = types.KeyboardButton("Программирование😎")
        item4 = types.KeyboardButton("Линейная алгебра🤯")
        item5 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(item1, item2, item3, item4, item5)
        bot.send_message(message.chat.id, "Выберите тот предмет, по которому вам интересна литература:", reply_markup=markup)


    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Литература📚")
        btn2 = types.KeyboardButton("Интересные места")
        lit = types.KeyboardButton("Расписание")
        hah = types.KeyboardButton("Смешное")
        markup.add(btn1, btn2, lit, hah)
        bot.send_message(message.chat.id, text="Без проблем, верёмся обратно. Выбери тот раздел, которым интересуешься:", reply_markup=markup)

    elif message.text == 'Дискретная математика🤩':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Алексеев Дискретная математика")
        btn2 = types.KeyboardButton("Сборник задач")
        btn3 = types.KeyboardButton('"Начала теории множеств", Н. Верещагин')
        btn4 = types.KeyboardButton("Вернуться назад")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id,
                         'Выберите номер ту книгу, которая вам интересна:\n1. Учебник "Дискретная математика" В. E. Алексеев.\n2. Сборник задач по дискретной математике.\n3. "Начала теории множеств", Н. Верещагин и А. Шень.',
                         reply_markup=markup)

    elif message.text == 'Вернуться назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Дискретная математика🤩",)
        item2 = types.KeyboardButton("Матанализ🥶")
        item3 = types.KeyboardButton("Программирование😎")
        item4 = types.KeyboardButton("Линейная алгебра🤯")
        item5 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(item1, item2, item3, item4, item5)
        bot.send_message(message.chat.id, "Без проблем. Выберите тот предмет, по которому вам интересна литература (на этот раз повнимательнее😁):", reply_markup=markup)


    elif message.text == 'Алексеев Дискретная математика':
        document = open('Алексеев Дискретная математика.pdf', 'rb')
        bot.send_message(message.chat.id, "Ваша книга/книги:")
        bot.send_document(message.chat.id, document)

        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка', url='https://docviewer.yandex.com/view/2039077367/?*=94RzTaplRbL1hwGdBSES7WyFPxt7InVybCI6InlhLWRpc2s6Ly8vZGlzay%2FQm9C40YLQtdGA0LDRgtGD0YDQsC%2FQkNC70LXQutGB0LXQtdCyINCU0LjRgdC60YDQtdGC0L3QsNGPINC80LDRgtC10LzQsNGC0LjQutCwLnBkZiIsInRpdGxlIjoi0JDQu9C10LrRgdC10LXQsiDQlNC40YHQutGA0LXRgtC90LDRjyDQvNCw0YLQtdC80LDRgtC40LrQsC5wZGYiLCJub2lmcmFtZSI6ZmFsc2UsInVpZCI6IjIwMzkwNzczNjciLCJ0cyI6MTcyOTQ1NDkxODQ2MywieXUiOiI5MzYwMDExMDAxNzIzMTQ2MDYwIn0%3D')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятной учёбы :)', reply_markup=keyboard)

    elif message.text == 'Сборник задач':
        document1 = open("Задачник 1 часть (2019).pdf", 'rb')
        document2 = open("Задачник 2 часть (2023).pdf", 'rb')
        bot.send_message(message.chat.id, "Ваша книга/книги:")
        bot.send_document(message.chat.id, document1)
        bot.send_document(message.chat.id, document2)

        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url1 = telebot.types.InlineKeyboardButton(text='Ссылка',
                                                        url='https://docviewer.yandex.com/view/2039077367/?*=LG3O%2FKAmBnx%2Fl0tMfzjPEjFuigx7InVybCI6InlhLWRpc2s6Ly8vZGlzay%2FQm9C40YLQtdGA0LDRgtGD0YDQsC%2FQl9Cw0LTQsNGH0L3QuNC6IDEg0YfQsNGB0YLRjCAoMjAxOSkucGRmIiwidGl0bGUiOiLQl9Cw0LTQsNGH0L3QuNC6IDEg0YfQsNGB0YLRjCAoMjAxOSkucGRmIiwibm9pZnJhbWUiOmZhbHNlLCJ1aWQiOiIyMDM5MDc3MzY3IiwidHMiOjE3Mjk0NTc1Njc1NTMsInl1IjoiOTM2MDAxMTAwMTcyMzE0NjA2MCJ9')
        button_url2 = telebot.types.InlineKeyboardButton(text ="Ссылка", url = "https://docviewer.yandex.com/view/2039077367/?*=Jpg%2FITQhXe5tHhvvZYYJWJF%2FvtN7InVybCI6InlhLWRpc2s6Ly8vZGlzay%2FQm9C40YLQtdGA0LDRgtGD0YDQsC%2FQl9Cw0LTQsNGH0L3QuNC6IDIg0YfQsNGB0YLRjCAoMjAyMykucGRmIiwidGl0bGUiOiLQl9Cw0LTQsNGH0L3QuNC6IDIg0YfQsNGB0YLRjCAoMjAyMykucGRmIiwibm9pZnJhbWUiOmZhbHNlLCJ1aWQiOiIyMDM5MDc3MzY3IiwidHMiOjE3Mjk0NTc2OTc5NzEsInl1IjoiOTM2MDAxMTAwMTcyMzE0NjA2MCJ9")
        keyboard.add(button_url1)
        keyboard.add(button_url2)
        bot.send_message(message.chat.id, text='Приятной учёбы :)', reply_markup=keyboard)


    elif message.text == '"Начала теории множеств", Н. Верещагин':
        document = open('Начала теории множеств Верещагин.pdf', 'rb')
        bot.send_message(message.chat.id, "Ваша книга/книги:")
        bot.send_document(message.chat.id, document)

        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка',
                                                        url='https://docviewer.yandex.com/view/2039077367/?*=zNELxicF8gC%2F9Ro54vmfYjXILFp7InVybCI6InlhLWRpc2s6Ly8vZGlzay%2FQm9C40YLQtdGA0LDRgtGD0YDQsC%2FQndCw0YfQsNC70LAg0YLQtdC%2B0YDQuNC4INC80L3QvtC20LXRgdGC0LIg0JLQtdGA0LXRidCw0LPQuNC9LnBkZiIsInRpdGxlIjoi0J3QsNGH0LDQu9CwINGC0LXQvtGA0LjQuCDQvNC90L7QttC10YHRgtCyINCS0LXRgNC10YnQsNCz0LjQvS5wZGYiLCJub2lmcmFtZSI6ZmFsc2UsInVpZCI6IjIwMzkwNzczNjciLCJ0cyI6MTcyOTQ1Nzc3MTM4NywieXUiOiI5MzYwMDExMDAxNzIzMTQ2MDYwIn0%3D')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятной учёбы :)', reply_markup=keyboard)



    elif message.text == 'Программирование😎':
        document = open('Kernighan_B_W_,_Ritchie_D_M_The_C_Programming_Language,_2nd_Edition.pdf', 'rb')
        bot.send_message(message.chat.id, "Ваша книга/книги:")
        bot.send_document(message.chat.id, document)

        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка',
                                                        url='https://docviewer.yandex.com/view/2039077367/?*=O2CJ8qBBnsAWFFV38RLNJKv%2BTRl7InVybCI6InlhLWRpc2s6Ly8vZGlzay%2FQm9C40YLQtdGA0LDRgtGD0YDQsC9LZXJuaWdoYW5fQl9XXyxfUml0Y2hpZV9EX01fVGhlX0NfUHJvZ3JhbW1pbmdfTGFuZ3VhZ2UsXzJuZF9FZGl0aW9uLnBkZiIsInRpdGxlIjoiS2VybmlnaGFuX0JfV18sX1JpdGNoaWVfRF9NX1RoZV9DX1Byb2dyYW1taW5nX0xhbmd1YWdlLF8ybmRfRWRpdGlvbi5wZGYiLCJub2lmcmFtZSI6ZmFsc2UsInVpZCI6IjIwMzkwNzczNjciLCJ0cyI6MTcyOTQ1Nzg2MzM5MiwieXUiOiI5MzYwMDExMDAxNzIzMTQ2MDYwIn0%3D')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятной учёбы :)', reply_markup=keyboard)



    elif message.text == "Линейная алгебра🤯":
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка',
                                                        url='https://docviewer.yandex.com/view/2039077367/?*=1XcKFL7Z3F9mJPrIcbGWWxtTXod7InVybCI6InlhLWRpc2s6Ly8vZGlzay%2FQm9C40YLQtdGA0LDRgtGD0YDQsC%2FQu9C40L3QtdC50L3QsNGPLnBkZiIsInRpdGxlIjoi0LvQuNC90LXQudC90LDRjy5wZGYiLCJub2lmcmFtZSI6ZmFsc2UsInVpZCI6IjIwMzkwNzczNjciLCJ0cyI6MTcyOTQ1ODgxNzU2OCwieXUiOiI5MzYwMDExMDAxNzIzMTQ2MDYwIn0%3D')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятной учёбы :)', reply_markup=keyboard)



    elif message.text == "Матанализ🥶":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        key1 = types.KeyboardButton('Зорич "Математический анализ"')
        key2 = types.KeyboardButton('Фихтенгольц "Курс дифференциального и интегрального исчисления"')
        key3 = types.KeyboardButton('Кудрявцев "Сборник задач по математическому анализу"')
        key4 = types.KeyboardButton('Вернуться назад')
        markup.add(key1, key2, key3, key4)
        bot.send_message(message.chat.id,
                         'Выберите номер той книги, которая вам интересна:\n1. Зорич "Математический анализ"   (2 тома).\n2. Фихтенгольц "Курс дифференциального и интегрального исчисления" (2 тома).\n3. Кудрявцев "Сборник задач по математическому анализу".',
                         reply_markup=markup)

    elif message.text == 'Зорич "Математический анализ"':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url1 = telebot.types.InlineKeyboardButton(text='Зорич, том 1',
                                                        url='https://docviewer.yandex.com/view/2039077367/?*=Rt1n552VIIktPb5tdxwU6S6jj4l7InVybCI6InlhLWRpc2s6Ly8vZGlzay%2FQm9C40YLQtdGA0LDRgtGD0YDQsC%2FQl9C%2B0YDQuNGHIDEg0YLQvtC8LnBkZiIsInRpdGxlIjoi0JfQvtGA0LjRhyAxINGC0L7QvC5wZGYiLCJub2lmcmFtZSI6ZmFsc2UsInVpZCI6IjIwMzkwNzczNjciLCJ0cyI6MTcyOTQ1ODAzNjIxNCwieXUiOiI5MzYwMDExMDAxNzIzMTQ2MDYwIn0%3D')
        button_url2 = telebot.types.InlineKeyboardButton(text ="Зорич, том 2", url = "https://docviewer.yandex.com/view/2039077367/?*=j0IjZWdTIthHlAxFLCoVl95InJZ7InVybCI6InlhLWRpc2s6Ly8vZGlzay%2FQm9C40YLQtdGA0LDRgtGD0YDQsC%2FQl9C%2B0YDQuNGHIDIg0YLQvtC8LnBkZiIsInRpdGxlIjoi0JfQvtGA0LjRhyAyINGC0L7QvC5wZGYiLCJub2lmcmFtZSI6ZmFsc2UsInVpZCI6IjIwMzkwNzczNjciLCJ0cyI6MTcyOTQ1ODA2NjAxOSwieXUiOiI5MzYwMDExMDAxNzIzMTQ2MDYwIn0%3D")
        keyboard.add(button_url1)
        keyboard.add(button_url2)
        bot.send_message(message.chat.id, text='Приятной учёбы :)', reply_markup=keyboard)



    elif message.text == 'Фихтенгольц "Курс дифференциального и интегрального исчисления"':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url1 = telebot.types.InlineKeyboardButton(text='Фихтенгольц, том 1',
                                                         url='https://docviewer.yandex.com/view/2039077367/?*=PBFeLc7Q9N%2FVtNVRqXjhZDH%2FsTF7InVybCI6InlhLWRpc2s6Ly8vZGlzay%2FQm9C40YLQtdGA0LDRgtGD0YDQsC%2FQpNC40YXRgtC10L3Qs9C%2B0LvRjNGGINCa0YPRgNGBINC00LjRhNGE0LXRgNC10L3RhtC40LDQu9GM0L3QvtCz0L4g0Lgg0LjQvdGC0LXQs9GA0LDQu9GM0L3QvtCz0L4g0LjRgdGH0LjRgdC70LXQvdC40Y8gMSDRgtC%2B0LwucGRmIiwidGl0bGUiOiLQpNC40YXRgtC10L3Qs9C%2B0LvRjNGGINCa0YPRgNGBINC00LjRhNGE0LXRgNC10L3RhtC40LDQu9GM0L3QvtCz0L4g0Lgg0LjQvdGC0LXQs9GA0LDQu9GM0L3QvtCz0L4g0LjRgdGH0LjRgdC70LXQvdC40Y8gMSDRgtC%2B0LwucGRmIiwibm9pZnJhbWUiOmZhbHNlLCJ1aWQiOiIyMDM5MDc3MzY3IiwidHMiOjE3Mjk0NTg0OTc0NDMsInl1IjoiOTM2MDAxMTAwMTcyMzE0NjA2MCJ9')
        button_url2 = telebot.types.InlineKeyboardButton(text="Фихтенгольц, том 2",
                                                         url="https://docviewer.yandex.com/view/2039077367/?*=ewitj8XuQ4tZ9D5bOof6i1Y9SDN7InVybCI6InlhLWRpc2s6Ly8vZGlzay%2FQm9C40YLQtdGA0LDRgtGD0YDQsC%2FQpNC40YXRgtC10L3Qs9C%2B0LvRjNGGINCa0YPRgNGBINC00LjRhNGE0LXRgNC10L3RhtC40LDQu9GM0L3QvtCz0L4g0Lgg0LjQvdGC0LXQs9GA0LDQu9GM0L3QvtCz0L4g0LjRgdGH0LjRgdC70LXQvdC40Y8gMiDRgtC%2B0LwucGRmIiwidGl0bGUiOiLQpNC40YXRgtC10L3Qs9C%2B0LvRjNGGINCa0YPRgNGBINC00LjRhNGE0LXRgNC10L3RhtC40LDQu9GM0L3QvtCz0L4g0Lgg0LjQvdGC0LXQs9GA0LDQu9GM0L3QvtCz0L4g0LjRgdGH0LjRgdC70LXQvdC40Y8gMiDRgtC%2B0LwucGRmIiwibm9pZnJhbWUiOmZhbHNlLCJ1aWQiOiIyMDM5MDc3MzY3IiwidHMiOjE3Mjk0NTg1NDI1MjgsInl1IjoiOTM2MDAxMTAwMTcyMzE0NjA2MCJ9")
        button_url3 = telebot.types.InlineKeyboardButton(text="Фихтенгольц, том 3",
                                                         url="https://docviewer.yandex.com/view/2039077367/?*=vQmkbhrWSGAD67vff73nU0enJB57InVybCI6InlhLWRpc2s6Ly8vZGlzay%2FQm9C40YLQtdGA0LDRgtGD0YDQsC%2FQpNC40YXRgtC10L3Qs9C%2B0LvRjNGGINCa0YPRgNGBINC00LjRhNGE0LXRgNC10L3RhtC40LDQu9GM0L3QvtCz0L4g0Lgg0LjQvdGC0LXQs9GA0LDQu9GM0L3QvtCz0L4g0LjRgdGH0LjRgdC70LXQvdC40Y8gMyDRgtC%2B0LwucGRmIiwidGl0bGUiOiLQpNC40YXRgtC10L3Qs9C%2B0LvRjNGGINCa0YPRgNGBINC00LjRhNGE0LXRgNC10L3RhtC40LDQu9GM0L3QvtCz0L4g0Lgg0LjQvdGC0LXQs9GA0LDQu9GM0L3QvtCz0L4g0LjRgdGH0LjRgdC70LXQvdC40Y8gMyDRgtC%2B0LwucGRmIiwibm9pZnJhbWUiOmZhbHNlLCJ1aWQiOiIyMDM5MDc3MzY3IiwidHMiOjE3Mjk0NTg1ODU1NjcsInl1IjoiOTM2MDAxMTAwMTcyMzE0NjA2MCJ9")
        keyboard.add(button_url1)
        keyboard.add(button_url2)
        keyboard.add(button_url3)
        bot.send_message(message.chat.id, text='Приятной учёбы :)', reply_markup=keyboard)



    elif message.text == 'Кудрявцев "Сборник задач по математическому анализу"':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_url = telebot.types.InlineKeyboardButton(text='Ссылка',
                                                        url='https://docviewer.yandex.com/view/2039077367/?*=8tqrXCSWDrOw6TPJyl%2FEnTzWqtp7InVybCI6InlhLWRpc2s6Ly8vZGlzay%2FQm9C40YLQtdGA0LDRgtGD0YDQsC%2FQmtGD0LTRgNGP0LLRhtC10LIg0KHQsdC%2B0YDQvdC40Log0LfQsNC00LDRhyDQv9C%2BINC80LDRgtCw0L3QsNC70LjQt9GDLnBkZiIsInRpdGxlIjoi0JrRg9C00YDRj9Cy0YbQtdCyINCh0LHQvtGA0L3QuNC6INC30LDQtNCw0Ycg0L%2FQviDQvNCw0YLQsNC90LDQu9C40LfRgy5wZGYiLCJub2lmcmFtZSI6ZmFsc2UsInVpZCI6IjIwMzkwNzczNjciLCJ0cyI6MTcyOTQ1ODcxMTc1NSwieXUiOiI5MzYwMDExMDAxNzIzMTQ2MDYwIn0%3D')
        keyboard.add(button_url)
        bot.send_message(message.chat.id, text='Приятной учёбы :)', reply_markup=keyboard)




    elif message.text == 'Расписание':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("/Узнать_расписание"), types.KeyboardButton("Вернуться в главное меню"))
        bot.send_message(message.chat.id, "Тут ты можешь узнать, на какую пару тебе следует сегодня поспешить =)", reply_markup=markup)



    elif message.text == 'Расслабиться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        b1 = types.KeyboardButton("/фразы_преподавателей")
        b2 = types.KeyboardButton("/жизненные_мемы")
        b3 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(b1, b2, b3)
        bot.send_message(message.chat.id,
                         text="Тут ты можешь расслабиться и чуток отвлечься от учёбы! Выбери, каким образом (осторожно, раздел делался в нетрезвом виде):".format(
                             message.from_user), reply_markup=markup)

    elif (message.text == "Дмитрий Талецкий"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        random_number1 = random.randint(0, 2)
        if random_number1 == 0:
            bot.send_message(message.chat.id, text="- Все, что не запрещено, то разрешено (с) Талецкий", reply_markup=markup)
        elif random_number1 == 1:
            bot.send_message(message.chat.id, text="- Вы думаете, вам нужен свет? Я так не думаю (с) Талецкий", reply_markup=markup)
        elif random_number1 == 2:
            bot.send_message(message.chat.id, text="- На 0! делить можно - и даже нужно! (с) Талецкий", reply_markup=markup)

    elif (message.text == "Фёдор Пеплин"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        random_number2 = random.randint(0, 12)
        if random_number2 == 0:
            bot.send_message(message.chat.id, text="- Указатели - это боль и страдания (с) Пеплин", reply_markup=markup)
        elif random_number2 == 1:
            bot.send_message(message.chat.id, text="- Это будет уже полное безумие, но я это сделаю (с) Пеплин", reply_markup=markup)
        elif random_number2 == 2:
            bot.send_message(message.chat.id, text="- Массивы мы будем проходить через одну-две лекции, но это не мешает мне его добавить (с) Пеплин", reply_markup=markup)
        elif random_number2 == 3:
            bot.send_message(message.chat.id, text="- Фиг его знает, зачем мы это уже делаем, но мы это сделаем (с) Пеплин", reply_markup=markup)
        elif random_number2 == 4:
            bot.send_message(message.chat.id, text="- Нет, это не Ньютон... Это я так делал (с) Пеплин", reply_markup=markup)
        elif random_number2 == 5:
            bot.send_message(message.chat.id, text="- Да, компилятор это разрешил, но на самом деле это нелегально (с) Пеплин", reply_markup=markup)
        elif random_number2 == 6:
            bot.send_message(message.chat.id, text="- Если не считать рандомный результат ошибкой, то ошибки не будет (с) Пеплин", reply_markup=markup)
        elif random_number2 == 7:
            bot.send_message(message.chat.id, text="- [Про свой пример:] Ни одному психически здоровому человеку такой пример в голову не придет (с) Пеплин", reply_markup=markup)
        elif random_number2 == 8:
            bot.send_message(message.chat.id, text="- Кто тебя так плохо учил С? Ответ: я (с) Пеплин", reply_markup=markup)
        elif random_number2 == 9:
            bot.send_message(message.chat.id, text="- Конспект я вам, правда, не присылал, но я пришлю когда-нибудь (с) Пеплин", reply_markup=markup)
        elif random_number2 == 10:
            bot.send_message(message.chat.id, text="- Присвоить одно другому я не могу. Давайте попробуем это сделать (с) Пеплин", reply_markup=markup)
        elif random_number2 == 11:
            bot.send_message(message.chat.id, text="[В кабинете не запускается демонстрация экрана.] - У нас сегодняшняя лекция похожа на дегустацию вина без вина (с) Пеплин", reply_markup=markup)
        elif random_number2 == 12:
            bot.send_message(message.chat.id, text="- Pascal - это прекрасный язык. Он мертвый, но он прекрасный (с) Пеплин", reply_markup=markup)

    elif (message.text == "Алексей Шмелёв"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        random_number3 = random.randint(0, 5)
        if random_number3 == 0:
            bot.send_message(message.chat.id, text="- Допустим, компьютер у нас такой, нормальный, сто тысяч ядер. Сколько сейчас примерно человек на Земле? Восемь миллиардов? Округлю до десяти. Тогда, если у каждого будет такой компьютер, и все они будут работать над этой задачей, то всего через триста двадцать лет мы получим ответ (с) Шмелев", reply_markup=markup)
        elif random_number3 == 1:
            bot.send_message(message.chat.id, text="- Получается, мы пофиксили ошибку другой ошибкой (с) Шмелев", reply_markup=markup)
        elif random_number3 == 2:
            bot.send_message(message.chat.id, text="- Если вы, допустим, ну хотя бы чемпион мира по программированию, проблем у вас не возникнет (с) Шмелев", reply_markup=markup)
        elif random_number3 == 3:
            bot.send_message(message.chat.id, text="- Представьте, что вы приходите к врачу, чтобы измерить свой рост, а он ломает вам ногу, чтобы на одной ноге вы стояли ровнее. Это, ну, довольно неожиданно, верно? (с) Шмелев", reply_markup=markup)
        elif random_number3 == 4:
            bot.send_message(message.chat.id, text="- Вы уже люди пожилые относительно школьников (с) Шмелев", reply_markup=markup)
        elif random_number3 == 5:
            bot.send_message(message.chat.id, text="- Python вредит вашему здоровью, может вызвать смерть. Шарит кто-нибудь за 'Русы против ящеров'? С++ - язык русов, Python - язык ящеров (с) Шмелев", reply_markup=markup)

    elif (message.text == "Екатерина Цаплина"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="- Натуральные числа перебрать - это как Волгу пешком перейти. Очень интересно, но невозможно (с) Цаплина", reply_markup=markup)


    elif (message.text == "Студенты"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        random_number1 = random.randint(0, 8)
        if random_number1 == 0:
            bot.send_message(message.chat.id, text="- Если Бога нет, то чья коровка по травке бегает?", reply_markup=markup)
        elif random_number1 == 1:
            bot.send_message(message.chat.id, text="- Ты же сказал, что под охотой крепкой матанализ пошёл. - Пошёл. Пошёл вот отсюда!", reply_markup=markup)
        elif random_number1 == 2:
            bot.send_message(message.chat.id, text="- Если Бога нет, то кто на иконах нарисован? Доказательство от обратного", reply_markup=markup)
        elif random_number1 == 3:
            bot.send_message(message.chat.id, text="- Луна ушла на ремонтные работы (с) Кузьмин Никита", reply_markup=markup)
        elif random_number1 == 4:
            bot.send_message(message.chat.id, text="- Дискорд забанили в России. За это надо выпить. Дискорд вернули в России, за это надо выпить!", reply_markup=markup)
        elif random_number1 == 5:
            bot.send_message(message.chat.id, text="- По принципу Архимеда, я щас вообще пиво открою!", reply_markup=markup)
        elif random_number1 == 6:
            bot.send_message(message.chat.id, text="- Нужно избавиться от пуза. - А жена твоя на чём будет спать?", reply_markup=markup)
        elif random_number1 == 7:
            bot.send_message(message.chat.id, text="- Тебе нужно, чтоб бобик гавкал? - Ну, в перспективе...", reply_markup=markup)
        elif random_number1 == 8:
            bot.send_message(message.chat.id, text="- Скоро мы будем вспоминать о тех бедных временах, когда мы зарабатывали всего по 600 тысяч в месяц...", reply_markup=markup)
    else:

        if message.text not in '0123456789':
            bot.send_message(message.chat.id, text="Ой, я тебя не понял :(")


bot.polling(none_stop=True)