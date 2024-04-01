# '''
# pip3 install pytelegrambotapi
# '''

# import telebot 

# token = '6515485267:AAFOZVeerxLuFI2VOpO50DApDZVMcNL4czo'        #always need to secure

# bot = telebot.TeleBot(token)

# keyboard = telebot.types.ReplyKeyboardMarkup()
# button1 = telebot.types.KeyboardButton('Да')
# button2 = telebot.types.KeyboardButton('Нет')
# keyboard.add(button1, button2)


# @bot.message_handler(commands=['start', 'hello', 'test'])
# def start_message(message):
#     print(message)
#     print(message.chat.id)
#     bot.send_message(message.chat.id, f'ПРИВЕТ, {message.from_user.first_name}', reply_markup=keyboard)
#     bot.register_next_step_handler(message, reply_to_button)

# def reply_to_button(message):
#     # print(message) 
#     if message.text == 'Да':
#         bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEK9H1leUN_VKIl6OSp65N05JB7riBiJwACfToAAgPtEUlGO1m9gtDmrTME')
#     elif message.text == 'Нет':
#         bot.send_message(message.chat.id, 'Пока')
#     else:
#         bot.send_message(message.chat.id, 'Нажмите на кнопку', reply_markup=keyboard)
#         bot.register_next_step_handler(message, reply_to_button)


# keyboard = telebot.types.InlineKeyboardMarkup()
# button1 = telebot.types.InlineKeyboardButton('Да', callback_data='Yes')
# button2 = telebot.types.InlineKeyboardButton('Нет', callback_data='No')

# keyboard.row(button1, button2)

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=keyboard)

# @bot.callback_query_handler(func = lambda call: True)
# def handler_callback(call):
#     print(call)
#     if call.data == 'yes':
#         bot.send_message(call.message.chat.id, 'Продолжим')
#     elif call.data == 'no':
#         pass


# @bot.message_handler(content_types=['sticker', 'text'], func=lambda message: True)
# def start_message(message):
#     # print(message)
#     bot.send_message(message.chat.id, 'Привет')
#     if message.sticker:
#         bot.send_sticker(message.chat.id, message.sticker.file_id)
#     elif message.text:
#         bot.send.text(message.chat.id, message, 'OK')

# bot.polling()  # держит код запущенным(polling)


















# # import telebot
# # import webbrowser


# # token = '6515485267:AAFOZVeerxLuFI2VOpO50DApDZVMcNL4czo'
# # bot = telebot.TeleBot(token)

# # keyboard = telebot.types.ReplyKeyboardMarkup()
# # button1 = telebot.types.InlineKeyboardButton('start')
# # button2 = telebot.types.InlineKeyboardButton('quit')


# # @bot.message_handler(commands=['start', 'quit'])
# # def start_message(message):
# #     print(message)
# #     print(message.chat.id)
# #     bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}, нажмите на <b>старт</b>, чтобы почитать новости', parse_mode='html')
# #     bot.register_next_step_handler(message, reply_to_button)


# # def reply_to_button(message):
# #     if message.text == 'start':
# #         bot.send_message(message, reply_to_button)
# #     elif message.text =='quit':
# #         bot.send_message(message.chat.id, 'До свидания')
# #     else:
# #         bot.send_message(message.chat.id, 'Нажмите на кнопку', reply_markup=keyboard)
# #         bot.register_next_step_handler(message, reply_to_button)


    


# # # @bot.message_handler(content_types=['photo'])
# # # def get_file(message):
# # #     markup = telebot.types.InlineKeyboardMarkup()
# # #     markup.add(telebot.types.InlineKeyboardButton('Перейти на сайт', url = 'https://kaktus.media/?lable=8&date=2023-12-14&order=time'))
# # #     markup.add(telebot.types.InlineKeyboardButton('Перейти на сайт', url = 'https://kaktus.media/?lable=8&date=2023-12-14&order=time'))

# # #     bot.reply_to(message, 'здесь должен выйти файл', reply_markup=markup)


# # # @bot.message_handler(commands=['site'])
# # # def web_site(message):
# # #     webbrowser.open('https://kaktus.media/?lable=8&date=2023-12-14&order=time')


# # bot.polling()


