from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def get_response(userText):
    bot = ChatBot('Macaw_BDD', storage_adapter='chatterbot.storage.SQLStorageAdapter',  read_only = True, logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.50,
            'default_response': 'I am sorry, but I do not understand'
        }
    ],
        trainer= 'chatterbot.trainers.ListTrainer')
    bot.set_trainer(ListTrainer)
    while True:
        if userText.strip() != 'Bye':
            result = bot.get_response(userText)
            reply = str(result)
            return reply
        if userText.strip() == 'Bye':
            reply = 'Bye!'
            return reply