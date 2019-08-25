1# We will build our first telegram bot in this script
# https://www.freecodecamp.org/news/learn-to-build-your-first-bot-in-telegram-with-python-4c99526765e4/
# This script will send you a random cute cat image wherever you want
# We are gonna be using python-telegram-bot and a the thecatapi.com

# First , go to telegram, search for botFather, create new bot with /newbot
# Follow the steps until you get your username and token for this bot
# Username : randCatsBot
# token : 923301358:AAFtgLTdOFhQgxJOW0NBqvZ2rNpeQXn-PaY

# Here is the logic for our cat Bot
# 1. Access the API of the cat website
# 2. Get the image URL
# 3. Send the image
# When a user sends the /meow command, this should return a cute cat image
 
# Other fucntionalities
# For this we have to check the limitations of the catapi

# Earlier errors:
# 1. Cat server sends gifs to which the site does not allow
#   thi, we need to allow gif sending to be allow on the bot too

# Importing all the libraries we will need
from telegram.ext import Updater , CommandHandler
# For handling http and https requests
import requests
# For logging and investigate why things work and dont work as expected
import logging

# Function returns the url of a random cat
def get_url():
    # Acessing the API to get the json data
    cats = requests.get("https://api.thecatapi.com/v1/images/search").json()
    cat_url =  cats[0]["url"]
    print(cats)
    return cat_url

# Need to check the url if it contains gif or image
# To check file extension, we are going to use regex
def check_image_url(url):
    extension = url[-3:]
    # We check if the url is a gif, if it is we return False
    if extension == "gif":
        return False
    # We return True if url is an image
    else:
        return False


# Function to send a  cat images to a recipient
def meow(bot, update):
    # To Send the image
    # We need 2 paramters, the image url and the recipients ID(either a user ID or a group ID)
    # Acess url with get_url
    url = get_url()
    print(url)
    # Get recipients code with
    chat_id = update.message.chat_id
    if check_image_url(url):
        # time to send the image to the recipient
        bot.send_photo( chat_id=chat_id, photo=url)
    else:
        bot.send_animation(chat_id= chat_id , animation= url)

def main():
    # Read up more on updater and commandHandler
    updater = Updater("923301358:AAFtgLTdOFhQgxJOW0NBqvZ2rNpeQXn-PaY")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("meow", meow))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__" :
    main()

