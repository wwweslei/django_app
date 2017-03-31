import telepot


def handle(msg):
    bot = telepot.Bot('313706502:AAHJvKb0hRk-U5B6YFzLTuYIByr5EFwHSWQ')
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        command = msg['text']
        #print('Command Received : {}'.format(command))
        if '/oi' == command:
            bot.sendMessage(chat_id, "Hello how are you?")
        if '/1' == command:
            bot.sendMessage(chat_id, 'Ok be working')


