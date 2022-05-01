import telebot

import config
import static

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def messages_for_start(message):
    bot.send_message(message.chat.id, static.start_text)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, static.default_answer(message.text))


if __name__ == '__main__':
    bot.infinity_polling()
