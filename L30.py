import telebot
from my_token import token
from telebot import types


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Э-эй, а зачем тебе управляющий? А? А ты не знал! Управляющая бюро в семьдесят седьмом поколении - Ху Тао! То есть я! Но судя по твоему виду... Свежее лицо, ровная осанка... Ага, это явно не рабочий визит. Да?')

def add_task(message):
    delo = message.text
    with open('spisok_del_2.txt', 'a', encoding='utf-8') as file:
        file.write(delo + '\n')
    bot.send_message(message.chat.id, 'Добавлено!')




@bot.message_handler(content_types='text')
def send_everything(message):
    if message.text == 'Добавить дело':
        msg = bot.send_message(message.chat.id, 'Что добавить?:з' )
        bot.register_next_step_handler(msg, add_task)


    elif message.text == 'Посмотреть список дел':
        bot.send_message(message.chat.id, 'Смотри')

    else:
        buttons = types.ReplyKeyboardMarkup(row_width=1)
        but1 = types.KeyboardButton('Добавить дело')
        but2 = types.KeyboardButton('Посмотреть список дел')
        buttons.add(but1, but2)
        bot.send_message(message.chat.id, 'Выбери: ', reply_markup=buttons)


bot.infinity_polling()

# https://pypi.org/project/pyTelegramBotAPI/

# https://apps.timwhitlock.info/emoji/tables/unicode

