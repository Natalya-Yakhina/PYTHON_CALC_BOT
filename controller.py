import operation as oper
import logger as log
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler

bot = Bot(token='5758988297:AAGIQVU89IKKAKWt2QzcJNTZ2gMJfgiUzUY')
updater = Updater(token='5758988297:AAGIQVU89IKKAKWt2QzcJNTZ2gMJfgiUzUY')
dispatcher = updater.dispatcher

def start(update, context): # функция старт
    reply_keyboard = [['Сумма', 'Разность'], ['Деление', 'Умножение'], ['Справка']]
    # markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True) # выдает в виде кнопок панель задач калькулятора
    context.bot.send_message(update.effective_chat.id, 'Добро пожаловать в калькулятор!\n'
                                                        'Я бот! 🤓\n'
                                                        'Я умею считать комплексные и рациональные числа!\n'
                                                        '/info')
                                                        # '/info', reply_markup = markup_key) # показывает в виде кнопок
                                                        
    log.log_one_argument('---ЗАПУСК БОТА---')


def info(update, context): # функция вызова справки
    log.log_one_argument('Вызвана справка') # записывает в логирование
    context.bot.send_message(update.effective_chat.id, f'Доступны следующие команды:\n'
                                                        '/sum - сумма\n'
                                                        '/diff - разность\n'
                                                        '/div - деление\n'
                                                        '/mult - умножение\n'
                                                        '/info - справка\n'
                                                        '\nНажми на команду, чтобы узнать подробнее')

def message(update, context): # записывает сообщения в файл логирования
    text = update.message.text
    if text.lower() == 'Справка':
        log.log_one_argument('Вызвано: "Справка"')
        context.bot.send_message(update.effective_chat.id, 'Введите /info')
    elif text.lower() == 'Сумма':
        log.log_one_argument('Вызвано: "Сумма"')
        context.bot.send_message(update.effective_chat.id, 'Введите /sum')
    elif text.lower() == 'Разность':
        log.log_one_argument('Вызвано: "Разность"')
        context.bot.send_message(update.effective_chat.id, 'Введите /diff')
    elif text.lower() == 'Умножение':
        log.log_one_argument('Вызвано: "Умножение"')
        context.bot.send_message(update.effective_chat.id, 'Введите /mult')
    elif text.lower() == 'Деление':
        log.log_one_argument('Вызвано: "Деление"')
        context.bot.send_message(update.effective_chat.id, 'Введите /div')
    else:
        log.log_two_argument('Я не понял, что от меня хотят(',
                             f'{update.message.chat.username}: {update.message.text}')
        context.bot.send_message(update.effective_chat.id, 'Я ничего не понимаю!')

def unknown(update, context):
    log.log_two_argument('Я ничего не понимаю!',
                         f'{update.message.chat.username}: {update.message.text}')
    context.bot.send_message(update.effective_chat.id, 'что говорите, я ничего не понимаю!')


def summ(update, context): # функция сложение
    arg = context.args
    if not arg:
        log.log_one_argument(f'Нет аргументов для {update.message.text}')
        context.bot.send_message(
            update.effective_chat.id, 'Введите /sum и 2 числа через пробел. Например: /sum 22 78')
    else:
        total = oper.sum(arg)
        log.log_one_argument(total)
        context.bot.send_message(update.effective_chat.id, total)

def difference(update, context): # функция вычитание
    arg = context.args
    if not arg:
        log.log_one_argument(f'Нет аргументов для {update.message.text}')
        context.bot.send_message(
            update.effective_chat.id, 'Введите /diff и 2 числа через пробел. Например: /diff 39 32')
    else:
        total = oper.diff(arg)
        log.log_one_argument(total)
        context.bot.send_message(update.effective_chat.id, total)


def division(update, context): # функция деление
    arg = context.args
    if not arg:
        log.log_one_argument(f'Нет аргументов для {update.message.text}')
        context.bot.send_message(
            update.effective_chat.id, 'Введите /div и 2 числа через пробел. Например: /div 66 4')
    else:
        total = oper.div(arg)
        log.log_one_argument(total)
        context.bot.send_message(update.effective_chat.id, total)


def multiplication(update, context): # функция умножение
    arg = context.args
    if not arg:
        log.log_one_argument(f'Нет аргументов для {update.message.text}')
        context.bot.send_message(
            update.effective_chat.id, 'Введите /mult и 2 числа через пробел. Например: /mult 25 3')
    else:
        total = oper.mult(arg)
        log.log_one_argument(total)
        context.bot.send_message(update.effective_chat.id, total)

start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
sum_handler = CommandHandler('sum', summ)
dif_handler = CommandHandler('diff', difference)
div_handler = CommandHandler('div', division)
mult_handler = CommandHandler('mult', multiplication)

message_handler = MessageHandler(Filters.text, message) # обработка сообщений
unknown_handler = MessageHandler(Filters.command, unknown) # обработка неизвестного

dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(sum_handler)
dispatcher.add_handler(dif_handler)
dispatcher.add_handler(div_handler)
dispatcher.add_handler(mult_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)

print('server started')

updater.start_polling()
updater.idle() # idle - блокирует до получения одного из сигналов и останавливает программу обновления