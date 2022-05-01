import telebot
import utility
import config
import static

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def messages_for_start(message):
    bot.send_message(message.chat.id, static.start_text)


@bot.message_handler(commands=["maths"])
def messages_for_start(message):
    bot.send_message(message.chat.id, static.maths)


@bot.message_handler(content_types=["text"])
def maths_func(message):
    split_massage = message.text.split()
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Приветствую тебя!')
    elif split_massage[0] in utility.all_math_func:
        if len(split_massage) == 1:
            bot.send_message(message.chat.id, f'{split_massage[0]} чего?')
        else:
            result = utility.math_func(split_massage[0], split_massage[1])
            bot.send_message(message.chat.id,
                                 f'{split_massage[0]} = {result}')
    else:
        bot.send_message(message.chat.id, static.default_answer(message.text))


if __name__ == '__main__':
    bot.infinity_polling()
