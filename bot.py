from telebot import types
import telebot

TOKEN = '5035433584:AAHB2MkAJyaiB5H_Gak572zuf9ucyI7UPQE'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду скидывать тебе базы')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_1 = types.KeyboardButton('1 курс')
    markup.add(key_1)
    bot.send_message(message.chat.id, 'Выбери свой курс', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def course_selection(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton("Выбрать курс")
    if message.text == "1 курс":
        btn_fiz = types.KeyboardButton("Физика")
        btn_fizra = types.KeyboardButton("Физкультура")
        btn_softskills = types.KeyboardButton("Soft Skills (open edu)")
        btn_infa = types.KeyboardButton("Информационные сервисы (open edu)")
        btn_bzhd = types.KeyboardButton("БЖД (open edu)")
        btn_inzhir = types.KeyboardButton("Инженерка")
        btn_philos = types.KeyboardButton("Философия")
        btn_chemistry = types.KeyboardButton("Химия")
        markup.add(btn_fiz, btn_inzhir)
        markup.row(btn_infa, btn_softskills)
        markup.row(btn_bzhd, btn_philos)
        markup.row(btn_chemistry)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Выбери предмет', reply_markup=markup)
        bot.register_next_step_handler(message, lesson_selection);


def lesson_selection(message):
    if message.text == "Физика":
        bot.send_message(message.chat.id,
                         "https://drive.google.com/drive/folders/1No92DvFYMPiXT7Ug5OTY5Gvau9N28J6U?usp=sharing")
        bot.register_next_step_handler(message, lesson_selection);
    elif message.text == "БЖД (open edu)":
        bot.send_message(message.chat.id,
                         "https://drive.google.com/drive/folders/1OBm8OwnWlIhCPelbGzEYjrG0xr8mK0XV?usp=sharing")
        bot.register_next_step_handler(message, lesson_selection);
    elif message.text == "Инженерка":
        bot.send_message(message.chat.id,
                         "https://drive.google.com/drive/folders/18kQ1omTON5zh_Iq5-yy3GTj5u4JozcR_?usp=sharing")
        bot.register_next_step_handler(message, lesson_selection);
    elif message.text == "Информационные сервисы (open edu)":
        bot.send_message(message.chat.id,
                         "https://drive.google.com/drive/folders/1B2I2zQrY8EJ4AaGqHToZUZMbdCnrpDiv?usp=sharing")
        bot.register_next_step_handler(message, lesson_selection);
    elif message.text == "Soft Skills (open edu)":
        bot.send_message(message.chat.id,
                         "https://drive.google.com/drive/folders/1AAVuB9_880IJeh9pQDbGiIwLoQveo10F?usp=sharing")
        bot.register_next_step_handler(message, lesson_selection);
    elif message.text == "Философия":
        bot.send_message(message.chat.id,
                         "https://drive.google.com/drive/folders/1y6hXijkMkYEOzQ8NmGofaVcSH4kR-w3o?usp=sharing")
        bot.register_next_step_handler(message, lesson_selection);
    elif message.text == "Химия":
        bot.send_message(message.chat.id,
                         "https://drive.google.com/drive/folders/1OLp6fWm5z3Z6h6dVRltqhmQ-L1MRlLML?usp=sharing")
        bot.register_next_step_handler(message, lesson_selection);
    elif message.text == "Выбрать курс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_1 = types.KeyboardButton('1 курс')
        markup.add(key_1)
        bot.send_message(message.chat.id, 'Выбери свой курс', reply_markup=markup)


bot.polling(none_stop=True)
