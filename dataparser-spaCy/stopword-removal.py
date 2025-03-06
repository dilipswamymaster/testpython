import spacy
load_model = spacy.load("en_core_web_sm")

# Create an nlp object
nlp = load_model("Apple's name was inspired by his visit to an apple farm while on a fruitarian diet.")

for token in nlp:
    if not token.is_stop:
        print(token)