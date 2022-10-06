# import operations as oper
# import logger as log
# from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, Bot
# from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
# from settings import TOKEN

# bot = Bot(token=TOKEN)
# updater = Updater(token=TOKEN)
# dispatcher = updater.dispatcher


# def start(update, context):
#     reply_keyboard = [['Сумма', 'Разность'], ['Деление',
#                                               'Умножение'], ['Справка']]
#     markup_key = ReplyKeyboardMarkup(
#         reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
#     context.bot.send_message(
#         update.effective_chat.id, "Добро пожаловать в калькулятор! 🤓\n/info", reply_markup=markup_key)
#     log.log_one_argument('---ЗАПУСК БОТА---')


# def info(update, context):
#     log.log_one_argument('Вызвана справка')
#     context.bot.send_message(
#         update.effective_chat.id, "Доступны следующие команды:\n\n/sum - сумма\n/diff - разность\n/div - деление\n/mult - умножение\n/info - справка\n\nНажми на команду, чтобы узнать подробнее или воспользуйся меню")


# def message(update, context):
#     text = update.message.text
#     if text.lower() == 'справка':
#         log.log_one_argument('Нажата кнопка "Справка"')
#         context.bot.send_message(update.effective_chat.id, 'Введите /info')
#     elif text.lower() == 'сумма':
#         log.log_one_argument('Нажата кнопка "Сумма"')
#         context.bot.send_message(update.effective_chat.id, 'Введите /sum')
#     elif text.lower() == 'разность':
#         log.log_one_argument('Нажата кнопка "Разность"')
#         context.bot.send_message(update.effective_chat.id, 'Введите /diff')
#     elif text.lower() == 'умножение':
#         log.log_one_argument('Нажата кнопка "Умножение"')
#         context.bot.send_message(update.effective_chat.id, 'Введите /mult')
#     elif text.lower() == 'деление':
#         log.log_one_argument('Нажата кнопка "Деление"')
#         context.bot.send_message(update.effective_chat.id, 'Введите /div')
#     else:
#         log.log_two_argument('Я не понял, что он хотел от меня',
#                              f'{update.message.chat.username}: {update.message.text}')
#         context.bot.send_message(update.effective_chat.id, 'Я тебя не понимаю')


# def unknown(update, context):
#     log.log_two_argument('Я не понял, что он хотел от меня',
#                          f'{update.message.chat.username}: {update.message.text}')
#     context.bot.send_message(update.effective_chat.id, 'Шо сказал, не пойму')


# def summ(update, context):
#     arg = context.args
#     if not arg:
#         log.log_one_argument(f'Нет аргументов для {update.message.text}')
#         context.bot.send_message(
#             update.effective_chat.id, 'Введи /sum и 2 числа через пробел. Например, скопируй и отправь мне следующее сообщение:')
#         context.bot.send_message(update.effective_chat.id, '/sum 22 78')
#     else:
#         total = oper.sum(arg)
#         log.log_one_argument(total)
#         context.bot.send_message(update.effective_chat.id, total)


# def difference(update, context):
#     arg = context.args
#     if not arg:
#         log.log_one_argument(f'Нет аргументов для {update.message.text}')
#         context.bot.send_message(
#             update.effective_chat.id, 'Введи /diff и 2 числа через пробел. Например, скопируй и отправь мне следующее сообщение:')
#         context.bot.send_message(update.effective_chat.id, '/diff 39 32')
#     else:
#         total = oper.diff(arg)
#         log.log_one_argument(total)
#         context.bot.send_message(update.effective_chat.id, total)


# def division(update, context):
#     arg = context.args
#     if not arg:
#         log.log_one_argument(f'Нет аргументов для {update.message.text}')
#         context.bot.send_message(
#             update.effective_chat.id, 'Введи /div и 2 числа через пробел. Например, скопируй и отправь мне следующее сообщение:')
#         context.bot.send_message(update.effective_chat.id, '/div 66 4')
#     else:
#         total = oper.div(arg)
#         log.log_one_argument(total)
#         context.bot.send_message(update.effective_chat.id, total)


# def multiplication(update, context):
#     arg = context.args
#     if not arg:
#         log.log_one_argument(f'Нет аргументов для {update.message.text}')
#         context.bot.send_message(
#             update.effective_chat.id, 'Введи /mult и 2 числа через пробел. Например, скопируй и отправь мне следующее сообщение:')
#         context.bot.send_message(update.effective_chat.id, '/mult 25 3')
#     else:
#         total = oper.mult(arg)
#         log.log_one_argument(total)
#         context.bot.send_message(update.effective_chat.id, total)


# start_handler = CommandHandler('start', start)
# info_handler = CommandHandler('info', info)
# sum_handler = CommandHandler('sum', summ)
# dif_handler = CommandHandler('diff', difference)
# div_handler = CommandHandler('div', division)
# mult_handler = CommandHandler('mult', multiplication)


# message_handler = MessageHandler(Filters.text, message)
# unknown_handler = MessageHandler(Filters.command, unknown)

# dispatcher.add_handler(start_handler)
# dispatcher.add_handler(info_handler)
# dispatcher.add_handler(sum_handler)
# dispatcher.add_handler(dif_handler)
# dispatcher.add_handler(div_handler)
# dispatcher.add_handler(mult_handler)
# dispatcher.add_handler(unknown_handler)
# dispatcher.add_handler(message_handler)


# print('server started')

# updater.start_polling()
# updater.idle()