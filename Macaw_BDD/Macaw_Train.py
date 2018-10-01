from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def setup():
    chatbot = ChatBot('Macaw_BDD', storage_adapter='chatterbot.storage.SQLStorageAdapter', trainer='chatterbot.trainers.ListTrainer')
    for file in os.listdir('C:/Users/ash223.SAPIENT/PycharmProjects/Macaw_BDD/data/'):
        convData = open('C:/Users/ash223.SAPIENT/PycharmProjects/Macaw_BDD/data/'+ file, 'r').readlines()
        chatbot.set_trainer(ListTrainer)
        chatbot.train(convData)

setup()


