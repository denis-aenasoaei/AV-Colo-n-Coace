import os
import aiml
from autocorrect import spell

# import sys
# sys.path.insert(0, '../info_system')

from info_system import main

BRAIN_FILE = "../dialog_system/aiml/aiml_pretrained_model.dump"

k = aiml.Kernel()

if os.path.exists(BRAIN_FILE):
    # print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    # print("Parsing aiml files")
    k.bootstrap(learnFiles="../dialog_system/aiml/pretrained_model/learningFileList.aiml", commands="load aiml")
    # print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)

# while True:
with  open(os.path.abspath("./audio/coloncoace-output.txt")) as file:
    query = file.read()
    print(query)
    query = [spell(w) for w in (query.split())]
    question = " ".join(query)
    queryResponse = main.queryApp(question)

    if queryResponse is None:
        response = k.respond(question)
    else:
        response = queryResponse

    if 'weather' in question.lower():
        query_response = main.meteo_query(question)
        if query_response is None:
            response = k.respond(question)
        else:
            response = query_response

    if 'route' in question.lower():
        query_response = main.map_query(question)
        if query_response is None:
            response = k.respond(question)
        else:
            response = query_response

    if response:
        print("\nbot>" + str(response))
    else:
        print("\nbot>:)")
