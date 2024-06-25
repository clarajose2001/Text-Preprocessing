import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Get user input for a sentence
sentence = input("Enter a sentence: ")

# Word tokenization
words = word_tokenize(sentence)
print("Word Tokens:", words)

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Get stop words
stop_words = set(stopwords.words('english'))

# Stemming
stemmed_words = [stemmer.stem(word) for word in words]
print("Stemmed Words:", stemmed_words)

# Lemmatization
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print("Lemmatized Words:", lemmatized_words)

# Stop words removal
filtered_words = [word for word in words if word.lower() not in stop_words]
print("Filtered Words:", filtered_words)
