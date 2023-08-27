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

# create tests for text preprocessing class


import unittest
class TestTextPreprocessor(unittest.TestCase):

    def setUp(self):
        self.preprocessor = TextPreprocessor()
        self.sample_text = "The quick brown foxes were jumping over the lazy dogs."

    def test_tokenize(self):
        tokens = self.preprocessor.tokenize(self.sample_text)
        self.assertEqual(tokens,
                         ['The', 'quick', 'brown', 'foxes', 'were', 'jumping', 'over', 'the', 'lazy', 'dogs', '.'])

    def test_remove_stopwords(self):
        tokens = ['The', 'quick', 'brown', 'foxes', 'were', 'jumping', 'over', 'the', 'lazy', 'dogs', '.']
        clean_tokens = self.preprocessor.remove_stopwords(tokens)
        self.assertEqual(clean_tokens, ['quick', 'brown', 'foxes', 'jumping', 'lazy', 'dogs', '.'])

    def test_lemmatize(self):
        tokens = ['foxes', 'were', 'jumping']
        lemmatized_tokens = self.preprocessor.lemmatize(tokens)
        self.assertEqual(lemmatized_tokens, ['fox', 'were', 'jumping'])

    def test_preprocess(self):
        preprocessed_tokens = self.preprocessor.preprocess(self.sample_text)
        self.assertEqual(preprocessed_tokens, ['quick', 'brown', 'fox', 'jumping', 'lazy', 'dog', '.'])


if __name__ == "__main__":
    unittest.main()
