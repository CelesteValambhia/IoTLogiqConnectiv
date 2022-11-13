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
@ILqCtivBot.message_handler(commands=['start'])
def start(message):
    helper = "Hello, How can I help you?\nThese are the commands you can run for interacting with the IoT " \
             "system:\n\nComfort Queries:\nSet_Room_Temp_Comfortable\nSet_Room_Light_Comfortable" \
             "\nSet_Room_Comfortable\n\nInstructions:\nGet_Room_Brightness\nGet_Room_Temperature" \
             "\nGet_Season\nSet_Lamp_Luminance <value>\nGet_Lamp_Luminance\nSet_Thermostat_Temperature " \
             "<value>\nGet_Thermostat_Temperature\nSet_AC_Temperature " \
             "<value>\nGet_AC_Temperature\nSet_Thermostat_Status <On/Off>\nSet_AC_Status " \
             "<On/Off>\nGet_Thermostat_Status\nGet_AC_Status\n\nEnergy Optimiser Queries:\nOptimise_Room\n "
    ILqCtivBot.send_message(message.chat.id, helper)


# Comfort Queries
def InputQuery(message):
    try:
        response = ClassifyInput(message)
        ILqCtivBot.send_message(message.chat.id, response)
    except Exception as e:
        print(e)
        ILqCtivBot.send_message(message.chat.id, "Error occurred. Logs sent to administrator.")
        # return False


@ILqCtivBot.message_handler(func=InputQuery)
def AnsInputQuery(message):
    ILqCtivBot.send_message(message.chat.id, message)

# Continuous polling is required to get the latest queries from the user.
ILqCtivBot.polling()
