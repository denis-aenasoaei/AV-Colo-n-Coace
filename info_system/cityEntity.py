import spacy
from spacy import displacy


def cityEntity(query):
    NER = spacy.load("en_core_web_sm")
    response = NER(query)
    for word in response.ents:
        if word.label_ == "GPE":
            return word.text
    return 0
