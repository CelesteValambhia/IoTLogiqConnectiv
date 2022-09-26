"""
Author: Celeste Valambhia
Chatbot Name: IoTLogiqConnectiv
Description: This chatbot is used to interact with underlined IoT system of the building for user engagement.
"""
import os
import telebot
from InputClassifier import *

ILqCtivBot_Key = os.environ.get('ILqCtivBot_KEY')
ILqCtivBot = telebot.TeleBot(ILqCtivBot_Key)


# Greetings
@ILqCtivBot.message_handler(commands=['Greet'])
def Greet(message):
    helper = "Hello, How can I help you?\nThese are the commands you can run for interacting with the IoT " \
             "system:\n\nComfort Queries:\nSet_Room_Temp_Comfortable\nSet_Room_Light_Comfortable" \
             "\nSet_Room_Comfortable\n "
    ILqCtivBot.send_message(message.chat.id, helper)


# Comfort Queries
def InputQuery(message):
    try:
        response = ClassifyInput(message)
        ILqCtivBot.send_message(message.chat.id, response)
    except Exception as e:
        print(e)
        return False


@ILqCtivBot.message_handler(func=InputQuery)
def AnsInputQuery(message):
    ILqCtivBot.send_message(message.chat.id, message)


ILqCtivBot.polling()
