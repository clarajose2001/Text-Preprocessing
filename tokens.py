import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize

# Sample sentence
sentence = "NLTK is a powerful Python library for natural language processing."

# Word tokenization
words = word_tokenize(sentence)

print("Word Tokens:", words)
