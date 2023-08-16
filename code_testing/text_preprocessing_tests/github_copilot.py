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


# create tests for text preprocessing class

# create a text preprocessing object
text_preprocessing = TextPreprocessing('This is a text file.')

# test the remove_stopwords method
text_preprocessing.remove_stopwords(['is', 'a'])
assert text_preprocessing.get_text() == 'This text file.'

# test the tokenize method
text_preprocessing.tokenize()
assert text_preprocessing.get_text() == ['This', 'text', 'file.']

# test the lemmatize method
text_preprocessing.lemmatize()
assert text_preprocessing.get_text() == ['This', 'text', 'file.']

# test the get_text method
assert text_preprocessing.get_text() == ['This', 'text', 'file.']
