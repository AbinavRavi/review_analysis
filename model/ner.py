import spacy
from spacy.tokens import Span
from spacy.language import Language


class NamedEntityRecognition:
    def __init__(self, model_name, ent_label) -> None:
        self.model_name = model_name
        self.ent_label = ent_label 
        self.nlp = spacy.load(self.model_name)

    @Language.component("add_product_entities")
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
    
    def extract_product_names(self,review_text):
        # self.nlp.add_pipe("add_product_entities", after="ner")
        doc = self.nlp(review_text)
        product_names = []
        for ent in doc.ents:
            if ent.label_ == self.ent_label:
                product_names.append(ent.text)
        return product_names