from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot('Colo-n coace')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.romanian")

# Get a response to an input statement
name = input("Introdu numele tău: ")
while True:
    request = input(name + ': ')
    if request == 'Pa':
        print('Bot: Pa, pa...')
        break
    else:
        response = chatbot.get_response(request)
        print('Bot:', response)
