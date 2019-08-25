"""
The goal here is to improve from the first version of the cat API

We will no longer be reffering to any guide online, instead we will look at the 
python-telegram-bot documentation online and thecatapi.com documentation.

Things to keep in mind when using the telegram-bot module
    - The name of our bot is telegram.me/randCatsBot
    - Bots cannot initiate conversations with uses, users, must either add
    them to a group or send them a message first.

The basic functionalities:
1. /start
2. /meow for pictures
3. /meeoww for gifs
4. instead of sending messages, i want to be able to use buttons to send out messages
5. I want to be able to know more about the cat
6. Show them the breed of the cats and then show cats based on breed


We do not need the authentication for the cats
"""
from telegram.ext import Updater, CommandHandler
import requests
import logging
import random

# Enable logging
# Logging is quite standard
logging.basicConfig(format="%(asctime)s - %(name)s -%(levelname)s -%(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


def error(update , context):
    # Log the errors caused by updates
    logger.warning("Update {} caused error {}".format(update, context.error))


def get_chat_id(update):
    print(update.message.chat.id)
    return update.message.chat.id

def start(bot, update):
    # Sends a command when start is issued
    start_message = "Hi,Interact with bot with these commands\n \
        /meow : gets a random cut cat pic\n \
        /meooow : gets a cute cat gif\n \
        /breed : show breeds of cats available\n \
        /meow_<breed> : show pics of cats of a specific breed"
    # Get recipients code with
    bot.send_message(chat_id=get_chat_id(update), text=start_message )



def get_url(file_type, specify_type):
    # Function returns the url of a random cat image
    # Acessing the API to get the json data
    # Type is either mime_types for images , breed_id
    # Let us add a logic, the choice for file type will be
    # breed or image
    # Specific type will have to be provided when get_url is called
    if file_type == "breed":
        file_type = "breed_id"
    elif file_type == "image":
        file_type =  "mime_types"

    parameter= file_type + "=" + specify_type
    cats = requests.get("https://api.thecatapi.com/v1/images/search?"+parameter).json()
    cat_url =  cats[0]["url"]
    return cat_url


def verify_url_image(url):
    # Need to check the url if it contains gif or image
    # To check file extension, we are going to use regex
    extension = url[-3:]
    # We check if the url is a gif, if it is we return False
    # We can do this because there are only 3 different results, gif,jpg,png
    if extension == "gif":
        return False
    # We return True if url is an image
    else:
        return True


def meow_image(bot, update):
    # Function to send a  cat images to a recipient
    # To Send the image
    # We need 2 paramters, the image url and the recipients ID(either a user ID or a group ID)
    # Acess url with get_url
    url = get_url("image" , "jpg,png")
    # Get recipients code with
    chat_id = update.message.chat.id
    while not verify_url_image(url):
        url = get_url("image" , "jpg,png")
        if verify_url_image(url):
            break
        # Time to send the image to the recipient
    bot.send_photo( chat_id=chat_id, photo=url)


def meow_gif(bot , update):
    # Function will send an gif
    # Same sequence as the process of sending image
    url = get_url("image", "gif")
    print(url)
    # Get recipients code again
    chat_id = update.message.chat.id
    # Check if the url sent is a gif, keep getting new url until its a gif
    while verify_url_image(url):
        url = get_url("image", "gif")
        print(url)
        if not verify_url_image(url):
            break
    bot.send_animation(chat_id=chat_id, animation=url)



def show_all_breed():
    request =  requests.get("https://api.thecatapi.com/v1/breeds").json()
    breeds = {}
    for breed in request:
        breeds[breed["id"]]=breed["name"]
    return breeds

def show_some_breed(bot , update):
    # Instead of showing all the breed right away
    # We can show 4 random breeds from the dictionary
    # Will then be executed by the command handler
    # Further improvements, would be to give them a button
    # Button of the 4 different cats to choose from
    breeds = show_all_breed()
    message = "Type 1 of these breed_id and get a cute cat pic of that breed. \nBreed_id : Breed name\n\n"
    for i in range(1,5):
        breed_id , breed = random.choice(list(breeds.items()))
        next_line = str(i) +"." + breed_id + ": " + breed + "\n"
        message+= next_line
    bot.send_message(chat_id=get_chat_id(update), text= message)

def get_breed_id(breed):
    # Will return the breed id from the given message
    # Might have to parse the message
    return None


def show_pic_of_breed(breed):
    # Might have to learn how to parse the message instead of just a command
    # breed_id = get_breed_id()
    # url = get_url("breed" , breed_id)
    # show image
    return None



def main():
    # Read up more on updater and commandHandler
    # The updater class contunuously fetches new updates from telegram
    # This messages are then passed on to the Dispatcher class
    # You can then link the updater and the dispatcher with a queue
    # You can register handlers of diff types in the dispatcher,
    # Which will sort the updates fetched by the updater according to handlers
    # you registered, and deliver them a callback function that you defined
    # user_context=True allows callbacks
    updater = Updater(token="923301358:AAFtgLTdOFhQgxJOW0NBqvZ2rNpeQXn-PaY")
    
    # Get the dispatcher to register handlers
    # To be clear these are objects that we queue together
    # Updater receiveds the message and then passes this to dispatcher
    dp = updater.dispatcher

    # On different commands -answer in telegram
    dp.add_handler(CommandHandler("meow", meow_image))
    dp.add_handler(CommandHandler("meooow", meow_gif))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("breed", show_some_breed))

    # We might have to parse the message that is sent if we want a sepcific breed
    #dp.add_handler(CommandHandler("specific breed", specific))


    # log all errors
    dp.add_error_handler(error)

    # Starts the bot
    updater.start_polling()

    # Runs the bot until you stop the program, 
    # this will help stop the bot gracefully
    updater.idle()


# I do not fully understand this notation
if __name__ == "__main__" :
    main()
"""

print(show_some_breed())
"""