# create a class to preprocess a text file: remove stopwords, tokenize and lemmatize

import nltk
from nltk.stem import WordNetLemmatizer


class TextPreprocessing:
    def __init__(self, text):
        self.text = text

    def remove_stopwords(self, stopwords):
        self.text = ' '.join([word for word in self.text.split() if word not in stopwords])

    def tokenize(self):
        self.text = self.text.split()

    def lemmatize(self):
        lemmatizer = WordNetLemmatizer()
        self.text = [lemmatizer.lemmatize(word) for word in self.text]

    def get_text(self):
        return self.text
