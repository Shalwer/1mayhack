import config
import telebot
import static

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def messages_for_start(message):
    bot.send_message(message.chat.id, static.start_text)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, static.default_answer(message.text))


@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/' + file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            # А теперь отправим вслед за файлом его file_id
            bot.send_message(message.chat.id, msg.voice.file_id,
                             reply_to_message_id=msg.message_id)
        time.sleep(3)


if __name__ == '__main__':
    bot.infinity_polling()
