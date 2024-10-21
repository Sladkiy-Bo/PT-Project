import telebot
import random

@bot.message_handler(commands=['фразы преподавателей'])
def frases_of_teachers(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    taletskii = types.KeyboardButton("Дмитрий Талецкий")
    peplin = types.KeyboardButton("Фёдор Пеплин")
    shmelev = types.KeyboardButton("Алексей Шмелёв")
    back = types.KeyboardButton("Не хочу")

    markup.add(taletskii, peplin, shmelev, back)
    bot.send_message(message.chat.id, text="Выберите ФИО преподавателя:", reply_markup=markup)

@bot.message_handler(commands=['жизненные мемы'])
def memes_of_shiza(message):
    random_number = random.randint(0, 9)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if random_number == 0:
        url = 'https://disk.yandex.ru/d/JZSShkKkWzpUyg/006ad43d-4324-4f7c-a5c8-39cb027f48c9.jpg'
        bot.send_photo(message.chat.id, photo=url)
    elif random_number == 1:
        url = 'https://disk.yandex.ru/d/JZSShkKkWzpUyg/2a7e0afa-6456-46ee-9262-0195dae04243.jpg'
        bot.send_photo(message.chat.id, photo=url)
    elif random_number == 2:
        url = 'https://disk.yandex.ru/d/JZSShkKkWzpUyg/420d84fe-dfdf-4a35-af52-25c4f2353486.jpg'
        bot.send_photo(message.chat.id, photo=url)
    elif random_number == 3:
        url = 'https://disk.yandex.ru/d/JZSShkKkWzpUyg/7c68da12-1bda-4460-a0b7-a08bda4b95b3.jpg'
        bot.send_photo(message.chat.id, photo=url)
    elif random_number == 4:
        url = 'https://disk.yandex.ru/d/JZSShkKkWzpUyg/94c7e669-90a1-46db-854b-62ea663be837.jpg'
        bot.send_photo(message.chat.id, photo=url)
    elif random_number == 5:
        url = 'https://disk.yandex.ru/d/JZSShkKkWzpUyg/9fbcca56-83d3-4ab8-8daf-8025a2047032.jpg'
        bot.send_photo(message.chat.id, photo=url)
    elif random_number == 6:
        url = 'https://disk.yandex.ru/d/JZSShkKkWzpUyg/e971151c-c3c9-4907-9259-72cbaec3f1ed.jpg'
        bot.send_photo(message.chat.id, photo=url)
    elif random_number == 7:
        url = 'https://disk.yandex.ru/d/JZSShkKkWzpUyg/ebf40f0a-02af-4854-99bd-67b53c5fab5d.jpg'
        bot.send_photo(message.chat.id, photo=url)
    elif random_number == 8:
        url = 'https://disk.yandex.ru/d/JZSShkKkWzpUyg/Снимок экрана 2024-10-20 100451.png'
        bot.send_photo(message.chat.id, photo=url)
    elif random_number == 9:
        url = 'https://disk.yandex.ru/d/JZSShkKkWzpUyg/Снимок экрана 2024-10-20 101733.png'
        bot.send_photo(message.chat.id, photo=url)

def func(message):
    random_number = random.randint(0, 10)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if (message.text == "Дмитрий Талецкий"):
        if random_number == 0:
            bot.send_message(message.chat.id, text="- Все, что не запрещено, то разрешено (с) Талецкий", reply_markup=markup)
        elif random_number == 1:
            bot.send_message(message.chat.id, text="- Вы думаете, вам нужен свет? Я так не думаю (с) Талецкий", reply_markup=markup)
        elif random_number == 2:
            bot.send_message(message.chat.id, text="- На 0! делить можно - и даже нужно! (с) Талецкий", reply_markup=markup)

    elif (message.text == "Фёдор Пеплин"):
        if random_number == 0:
            bot.send_message(message.chat.id, text="- Указатели - это боль и страдания (с) Пеплин", reply_markup=markup)
        elif random_number == 1:
            bot.send_message(message.chat.id, text="- Это будет уже полное безумие, но я это сделаю (с) Пеплин", reply_markup=markup)
        elif random_number == 2:
            bot.send_message(message.chat.id, text="- Массивы мы будем проходить через одну-две лекции, но это не мешает мне его добавить (с) Пеплин", reply_markup=markup)
        elif random_number == 3:
            bot.send_message(message.chat.id, text="- Фиг его знает, зачем мы это уже делаем, но мы это сделаем (с) Пеплин", reply_markup=markup)
        elif random_number == 4:
            bot.send_message(message.chat.id, text="- Нет, это не Ньютон... Это я так делал (с) Пеплин", reply_markup=markup)
        elif random_number == 5:
            bot.send_message(message.chat.id, text="- Да, компилятор это разрешил, но на самом деле это нелегально (с) Пеплин", reply_markup=markup)
        elif random_number == 6:
            bot.send_message(message.chat.id, text="- Если не считать рандомный результат ошибкой, то ошибки не будет (с) Пеплин", reply_markup=markup)
        elif random_number == 7:
            bot.send_message(message.chat.id, text="- [Про свой пример:] Ни одному психически здоровому человеку такой пример в голову не придет (с) Пеплин", reply_markup=markup)
        elif random_number == 8:
            bot.send_message(message.chat.id, text="- Кто тебя так плохо учил С? Ответ: я (с) Пеплин", reply_markup=markup)
        elif random_number == 9:
            bot.send_message(message.chat.id, text="- Конспект я вам, правда, не присылал, но я пришлю когда-нибудь (с) Пеплин", reply_markup=markup)
        elif random_number == 10:
            bot.send_message(message.chat.id, text="- Присвоить одно другому я не могу. Давайте попробуем это сделать (с) Пеплин", reply_markup=markup)

    elif (message.text == "Алексей Шмелёв"):
        if random_number == 0:
            bot.send_message(message.chat.id, text="- Допустим, компьютер у нас такой, нормальный, сто тысяч ядер. Сколько сейчас примерно человек на Земле? Восемь миллиардов? Округлю до десяти. Тогда, если у каждого будет такой компьютер, и все они будут работать над этой задачей, то всего через триста двадцать лет мы получим ответ (с) Шмелев", reply_markup=markup)
        elif random_number == 1:
            bot.send_message(message.chat.id, text="- Получается, мы пофиксили ошибку другой ошибкой (с) Шмелев", reply_markup=markup)
        elif random_number == 2:
            bot.send_message(message.chat.id, text="- Если вы, допустим, ну хотя бы чемпион мира по программированию, проблем у вас не возникнет (с) Шмелев", reply_markup=markup)
        elif random_number == 3:
            bot.send_message(message.chat.id, text="- Представьте, что вы приходите к врачу, чтобы измерить свой рост, а он ломает вам ногу, чтобы на одной ноге вы стояли ровнее. Это, ну, довольно неожиданно, верно? (с) Шмелев", reply_markup=markup)
        elif random_number == 4:
            bot.send_message(message.chat.id, text="- Вы уже люди пожилые относительно школьников (с) Шмелев", reply_markup=markup)
        elif random_number == 5:
            bot.send_message(message.chat.id, text="- Python вредит вашему здоровью, может вызвать смерть. Шарит кто-нибудь за 'Русы против ящеров'? С++ - язык русов, Python - язык ящеров (с) Шмелев", reply_markup=markup)


