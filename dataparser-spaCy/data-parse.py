# pip install -U spacy
# python -m spacy download en_core_web_sm
'''
`en_core_web_sm` is an English language multi-task Convolutional Neural Network(CNN) trained on OntoNotes. 
Assigns context-specific token vectors, POS tags, dependency parse, and named entities. 
'''
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = (''' 
At the trailer launch, director Mudassar Aziz spoke about the unfair treatment that comedy films have received in the industry. He underscored the importance of the viewing experience that these movies provide, especially when one is watching a film with the family.
''')

'''
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
'''
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
