import spacy

nlp = spacy.load("en_core_web_sm")

def extract_symptoms(user_input):
    doc = nlp(user_input)
    symptoms = [ent.text for ent in doc.ents if ent.label_ == "SYMPTOM"]
    return symptoms