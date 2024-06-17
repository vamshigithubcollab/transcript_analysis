import spacy

# Load the medium-sized English language model
nlp = spacy.load('en_core_web_md')

# Process a text
doc = nlp("Apple is looking at buying U.K. startup for $1 billion.")

# Tokenization
print("Tokens:")
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.dep_)

# Named Entity Recognition
print("\nNamed Entities:")
for ent in doc.ents:
    print(ent.text, ent.label_)

# Similarity (comparing two words)
apple = nlp("apple")
fruit = nlp("fruit")
print("\nSimilarity between 'apple' and 'fruit':", apple.similarity(fruit))
