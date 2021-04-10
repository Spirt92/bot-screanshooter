# token1110545386:AAHLY1grQ-asU88iSL5ASJotVY9GOQmppbY
from time import sleep
import telebot
from selenium import webdriver
import config
import validators

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["help"])
def answer(message):
    bot.send_message(
        message.chat.id,
        'Hello I`m the bot that make screenshot of the any site you give me\n"/start"',
    )


@bot.message_handler(commands=["start"])
def keyboard(message):
    bot.send_message(message.chat.id, "Waiting for the link 👋")


@bot.message_handler(content_types=["text"])
def handler_message(*messages):
    for user_message in messages:
        chatid = user_message.chat.id
        text = user_message.text
        if validators.url(user_message):
            # driver = webdriver.Chrome("./chromedriver")
            # driver.get(f'{user_message}')
            # sleep(3)
            # driver.get_screenshot_as_file("screenshot.png")
            # driver.quit()
            bot.send_photo(chatid, photo=open("./screenshot.png", "rb"))
        bot.send_message(chatid, text)


@bot.message_handler(content_types=["text"])
def handler_message(message):
    chatid = message.chat.id
    text = message.text
    bot.send_message(chatid, text)


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)

