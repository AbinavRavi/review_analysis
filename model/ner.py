import spacy
from spacy.tokens import Span
from spacy.pipeline import EntityRuler

nlp = spacy.load("en_core_web_sm")

def add_product_entities(doc):
    new_entities = []
    for i, token in enumerate(doc):
        # Check for tokens starting with uppercase letters
        if token.is_upper and i > 0 and doc[i - 1].is_title:
            # Merge consecutive uppercase tokens into a single entity
            if len(new_entities) > 0 and isinstance(new_entities[-1], Span):
                entity = doc[new_entities[-1].start:token.i + 1]
                new_entities[-1] = entity
            else:
                new_entities.append(doc[i - 1:token.i + 1])
    doc.ents = list(doc.ents) + new_entities
    return doc

# Create an instance of the EntityRuler
ruler = EntityRuler(nlp)

# Define the pattern for the product entity
product_patterns = [{"label": "PRODUCT", "pattern": [{"is_upper": True}]}]

# Add the product entity pattern to the EntityRuler
ruler.add_patterns(product_patterns)

# Add the EntityRuler to the pipeline
nlp.add_pipe(ruler, before="ner")
nlp.add_pipe(add_product_entities, after="ner")

def extract_product_names(review_text):
    doc = nlp(review_text)
    product_names = []
    for ent in doc.ents:
        if ent.label_ == "PRODUCT":
            product_names.append(ent.text)
    return product_names