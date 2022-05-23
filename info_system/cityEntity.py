import spacy
from datasets import load_dataset


def cityEntity(query):
    # ronec = load_dataset("ronec")
    NER = spacy.load("en_core_web_sm")
    response = NER(query)

    for word in response.ents:
        if word.label_ == "GPE":
            return word.text

    return 0
