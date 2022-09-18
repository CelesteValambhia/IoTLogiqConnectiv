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
    ILqCtivBot.send_message(message.chat.id, "Hello, How can I help you?")


# Comfort Queries
def InputQuery(message):
    if ClassifyInput(message):
        return True
    else:
        return False


@ILqCtivBot.message_handler(func=InputQuery)
def AnsInputQuery(message):
    msg = getAnswer(message)
    ILqCtivBot.send_message(message.chat.id, msg)


ILqCtivBot.polling()
