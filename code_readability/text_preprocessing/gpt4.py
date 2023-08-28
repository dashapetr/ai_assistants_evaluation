# create a class to preprocess a text file: remove stopwords, tokenize and lemmatize

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')


class TextPreprocessor:

    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def remove_stopwords(self, tokens):
        return [word for word in tokens if word.lower() not in self.stop_words]

    def tokenize(self, text):
        return word_tokenize(text)

    def lemmatize(self, tokens):
        return [self.lemmatizer.lemmatize(word) for word in tokens]

    def preprocess(self, text):
        tokens = self.tokenize(text)
        tokens = self.remove_stopwords(tokens)
        return self.lemmatize(tokens)
