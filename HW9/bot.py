from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler

# bot = Bot(token='5758988297:AAGIQVU89IKKAKWt2QzcJNTZ2gMJfgiUzUY')
# updater = Updater(token='5758988297:AAGIQVU89IKKAKWt2QzcJNTZ2gMJfgiUzUY')
dispatcher = updater.dispatcher

START = 0
NUMBERFIRST = 1
NUMBERSECOND = 2
OPERATION = 3
RESULT = 4
numberOne = ''
numberTwo = ''
oper = ''

def numbers(number):
    try:
        return int(number)
    except:
        return complex(number.replace(' ', ''))

def result(x, y, z):
    if z == '0':
        return x + y
    elif z == '1':
        return x - y
    elif z == '2':
        return x * y
    return x / y

def start(update, context): # старт 
    context.bot.send_message(update.effective_chat.id, f'Добро пожаловать! Я бот!❤️\n' 
                                                        'Я умею считать комплексные и рациональные числа!\n'
                                                        'Напиши 2 числа\n'
                                                       'Введите первое число: ')
    return NUMBERFIRST

def numberFirst(update, context):
    global numberOne
    numberOne = numbers(update.message.text)
    context.bot.send_message(update.effective_chat.id, 'Отлично!\nВведите второе число: ')
    return NUMBERSECOND


def numberSecond(update, context):
    global numberTwo
    numberTwo = numbers(update.message.text)
    board = [[InlineKeyboardButton('+', callback_data='0'), InlineKeyboardButton('-', callback_data='1')],
             [InlineKeyboardButton('*', callback_data='2'), InlineKeyboardButton(':', callback_data='3')]]
    update.message.reply_text('Выберите:', reply_markup=InlineKeyboardMarkup(board))
    return OPERATION


def operation(update, context):
    global res
    # global oper
    que = update.callback_query
    var = que.data
    que.answer()
    res = result(numberOne, numberTwo, var)
    que.edit_message_text(text=f'Результат операции: {res}')


def cancel(update, context): # выход
    context.bot.send_message(update.effective_chat.id, 'До новых встреч!')
    return ConversationHandler.END

start_handler = CommandHandler('start', start) # команда старт
cancel_handler = CommandHandler('cancel', cancel) # команда выход
numone_handler = MessageHandler(Filters.text, numberFirst) # первое число
numtwo_handler = MessageHandler(Filters.text, numberSecond) # второе число
oper_handler = CallbackQueryHandler(operation) # обработка операции
conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={
                                       NUMBERFIRST: [numone_handler],
                                       NUMBERSECOND: [numtwo_handler],
                                       OPERATION: [oper_handler],
                                   },
                                   fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler) # обработка
updater.start_polling()
updater.idle() #idle - Блокирует до получения одного из сигналов и останавливает программу обновления.