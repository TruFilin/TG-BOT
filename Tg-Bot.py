from config import bot
import telebot
import requests
from telebot import types
bot = telebot.TeleBot(bot)
@bot.message_handler(commands=['start'])
def start(message):
    if message.text.lower() == '/start':
        file = open('pic.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name},'
                                          f' вас привествует Бот для конвертации валюты.💵\n'
                                          f'Я конвертирую выбранную вами валюту в нужный эквивалент. Выбирите нужную вам валюту ниже.')
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Юани💴')
        btn2 = types.KeyboardButton('Евро💶')
        btn3 = types.KeyboardButton('Доллары💵')
        btn4 = types.KeyboardButton('Bitcoin💱')
        btn5 = types.KeyboardButton('Фунты💷')
        btn6 = types.KeyboardButton('Рубли💰')
        markup.add( btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, 'Выберите пункт меню:', reply_markup=markup)
        bot.register_next_step_handler(message, on_click)
def on_click(message):
    if message.text == 'Юани💴':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)
        bot.send_message(message.chat.id, f'Введите конечную валюту конвертации и сумму. Пример: USD 100*', reply_markup=markup)
        bot.register_next_step_handler(message, convert_cny)
        bot.register_next_step_handler(message, on_back_button_click)

    elif message.text == 'Евро💶':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)
        bot.send_message(message.chat.id, f'Введите конечную валюту конвертации и сумму. Пример: USD 100*', reply_markup=markup)
        bot.register_next_step_handler(message, convert_eur)
        bot.register_next_step_handler(message, on_back_button_click)

    elif message.text == 'Доллары💵':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)
        bot.send_message(message.chat.id, f'Введите конечную валюту конвертации и сумму. Пример: USD 100*', reply_markup=markup)
        bot.register_next_step_handler(message, convert_usd)
        bot.register_next_step_handler(message, on_back_button_click)
    elif message.text == '/help':
        bot.send_message(message.chat.id, f'Данный бот конвертирует валюту в рубли.\n'
                                          f'Выберите нужную валюту нажав соответствующую кнопку ниже.'
                                          f'Далее введите нужную вам валюту для конвертации и сумму.\n'
                                          f'Пример: "EUR 1000"')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Bitcoin💱':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)
        bot.send_message(message.chat.id, f'Введите конечную валюту конвертации и сумму. Пример: USD 100*',
                         reply_markup=markup)
        bot.register_next_step_handler(message, convert_btc)
        bot.register_next_step_handler(message, on_back_button_click)
    elif message.text == 'Фунты💷':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)
        bot.send_message(message.chat.id, f'Введите конечную валюту конвертации и сумму. Пример: USD 100*',
                         reply_markup=markup)
        bot.register_next_step_handler(message, convert_gbp)
        bot.register_next_step_handler(message, on_back_button_click)
    elif message.text == 'Рубли💰':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)
        bot.send_message(message.chat.id, f'Введите конечную валюту конвертации и сумму. Пример: USD 100*',
                         reply_markup=markup)
        bot.register_next_step_handler(message, convert_rub)
        bot.register_next_step_handler(message, on_back_button_click)



    else:
        bot.send_message(message.chat.id, 'К сожалению, ваш ввод не распознан. Пожалуйста, выберите пункт меню.')
        bot.register_next_step_handler(message, on_click)
@bot.message_handler()
def on_back_button_click(message):
    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Юани💴')
        btn2 = types.KeyboardButton('Евро💶')
        btn3 = types.KeyboardButton('Доллары💵')
        btn4 = types.KeyboardButton('Bitcoin💱')
        btn5 = types.KeyboardButton('Фунты💷')
        btn6 = types.KeyboardButton('Рубли💰')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, 'Выберите пункт меню:', reply_markup=markup)
        bot.register_next_step_handler(message, on_click)

@bot.message_handler()
def convert_usd(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)
    try:
        base, amount = message.text.split(' ')
        response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms={base}')
        exchange_rate = response.json()[base]
        amount_rub = float(amount) * exchange_rate
        bot.send_message(message.chat.id, f'Сумма в {base}: {amount_rub}')
        bot.register_next_step_handler(message, on_back_button_click)
    except ValueError:
            bot.send_message(message.chat.id, 'Некорректный ввод, повторите попытку')
            bot.register_next_step_handler(message, convert_usd)
def convert_eur(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)
    try:
        base, amount = message.text.split(' ')
        response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=EUR&tsyms={base}')
        exchange_rate = response.json()[base]
        amount_rub = float(amount) * exchange_rate
        bot.send_message(message.chat.id, f'Сумма в {base}: {amount_rub}')
        bot.register_next_step_handler(message, on_back_button_click)
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректный ввод, повторите попытку')
        bot.register_next_step_handler(message, convert_eur)
def convert_cny(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Назад')
    markup.add()
    try:
        base, amount = message.text.split(' ')
        response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=CNY&tsyms={base}')
        exchange_rate = response.json()[base]
        amount_rub = float(amount) * exchange_rate
        bot.send_message(message.chat.id, f'Сумма в {base}: {amount_rub}')
        bot.register_next_step_handler(message, on_back_button_click)
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректный ввод, повторите попытку')
        bot.register_next_step_handler(message, convert_cny)

def convert_btc(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)
    try:
        base, amount = message.text.split(' ')
        response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms={base}')
        exchange_rate = response.json()[base]
        amount_rub = float(amount) * exchange_rate
        bot.send_message(message.chat.id, f'Сумма в {base}: {amount_rub}')
        bot.register_next_step_handler(message, on_back_button_click)
    except ValueError:
            bot.send_message(message.chat.id, 'Некорректный ввод, повторите попытку')
            bot.register_next_step_handler(message, convert_usd)

def convert_gbp(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)
    try:
        base, amount = message.text.split(' ')
        response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=GBP&tsyms={base}')
        exchange_rate = response.json()[base]
        amount_rub = float(amount) * exchange_rate
        bot.send_message(message.chat.id, f'Сумма в {base}: {amount_rub}')
        bot.register_next_step_handler(message, on_back_button_click)
    except ValueError:
            bot.send_message(message.chat.id, 'Некорректный ввод, повторите попытку')
            bot.register_next_step_handler(message, convert_usd)
def convert_rub(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)
    try:
        base, amount = message.text.split(' ')
        response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=RUB&tsyms={base}')
        exchange_rate = response.json()[base]
        amount_rub = float(amount) * exchange_rate
        bot.send_message(message.chat.id, f'Сумма в {base}: {amount_rub}')
        bot.register_next_step_handler(message, on_back_button_click)
    except ValueError:
            bot.send_message(message.chat.id, 'Некорректный ввод, повторите попытку')
            bot.register_next_step_handler(message, convert_usd)

bot.polling(none_stop=True)