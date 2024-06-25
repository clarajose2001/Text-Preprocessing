import spacy

# Load the English language model in spaCy
nlp = spacy.load('en_core_web_sm')

# Get user input for a sentence
sentence = input("Enter a sentence: ")

# Process the sentence using spaCy
doc = nlp(sentence)

# Word tokenization
words = [token.text for token in doc]
print("Word Tokens:", words)

# Lemmatization and optional pseudo-stemming
lemmatized_words = [token.lemma_.lower().strip() if token.lemma_ != "-PRON-" else token.lower_ for token in doc]
print("Lemmatized Words:", lemmatized_words)

# Stop words removal (spaCy has built-in stop word functionality)
filtered_words = [token.text for token in doc if not token.is_stop]
print("Filtered Words:", filtered_words)
