from info_system import main
from flask import Flask, render_template, request
import os
import aiml
from autocorrect import Speller

app = Flask(__name__)
BRAIN_FILE = "aiml_pretrained_model.dump"

# Kernel object is the public interface to the AIML interpreter.
# “learn” method loads the contents of an AIML file into the kernel.
# While the “respond” method is used to get the response from the learned AIML file.
k = aiml.Kernel()

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="./pretrained_model/learningFileList.aiml", commands="load aiml")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    spell = Speller()
    query = request.args.get('msg')
    query = [spell(w) for w in (query.split())]
    question = " ".join(query)

    queryResponse = main.queryApp(question)
    if queryResponse is None:
        response = k.respond(question)
    else:
        response = queryResponse[0]['name']
    if response:
        return str(response)
    else:
        return str(":)")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
