import telegram
import os
from datetime import datetime

#token that can be generated talking with @BotFather on telegram
#my_token = '1878582425:AAGbKaaR_R9gEdJiFDAtWiBJNaT92bdwFUs'
#attachment = open("test.png", "r")
#now = datetime.now()
#msg=f"Test_message"


##


def send(msg, chat_id, token):
	"""
	Send a mensage to a telegram user specified on chatId
	chat_id must be a number!
	"""
	#msg=f'{now}: {msg}'
	bot = telegram.Bot(token=token)
	bot.sendMessage(chat_id=chat_id, text=msg)


