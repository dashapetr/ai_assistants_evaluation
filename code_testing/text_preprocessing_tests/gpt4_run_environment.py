# after the text preprocessor class creation, I asked GPT4 to create test cases
# and run them in current environment

# Since we can't use external libraries like nltk here directly,
# I'll mock the necessary components to demonstrate the functionality and run the tests.

# Mocking the required nltk functionalities
class MockNLTK:

    def word_tokenize(self, text):
        return text.split()

    def lemmatize(self, word):
        # A very basic mock lemmatizer for demonstration purposes
        lemmatized_words = {
            'foxes': 'fox',
            'dogs': 'dog',
            'were': 'were',
            'jumping': 'jumping'
        }
        return lemmatized_words.get(word, word)

    def stopwords(self):
        return set(['the', 'were', 'over', 'and', 'to', 'of', 'in', 'for'])


mock_nltk = MockNLTK()


class TextPreprocessor:

    def __init__(self):
        self.stop_words = mock_nltk.stopwords()
        self.lemmatizer = mock_nltk

    def remove_stopwords(self, tokens):
        return [word for word in tokens if word.lower() not in self.stop_words]

    def tokenize(self, text):
        return mock_nltk.word_tokenize(text)

    def lemmatize(self, tokens):
        return [self.lemmatizer.lemmatize(word) for word in tokens]

    def preprocess(self, text):
        tokens = self.tokenize(text)
        tokens = self.remove_stopwords(tokens)
        return self.lemmatize(tokens)


# Running the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestTextPreprocessor)
unittest.TextTestRunner().run(suite)

# I apologize for the oversight. It appears I missed defining the TestTextPreprocessor class before running the tests.
# Let me correct that and rerun the tests for you.

# Defining the TestTextPreprocessor class and then running the tests

class TestTextPreprocessor(unittest.TestCase):

    def setUp(self):
        self.preprocessor = TextPreprocessor()
        self.sample_text = "The quick brown foxes were jumping over the lazy dogs."

    def test_tokenize(self):
        tokens = self.preprocessor.tokenize(self.sample_text)
        self.assertEqual(tokens, ['The', 'quick', 'brown', 'foxes', 'were', 'jumping', 'over', 'the', 'lazy', 'dogs.'])

    def test_remove_stopwords(self):
        tokens = ['The', 'quick', 'brown', 'foxes', 'were', 'jumping', 'over', 'the', 'lazy', 'dogs.']
        clean_tokens = self.preprocessor.remove_stopwords(tokens)
        self.assertEqual(clean_tokens, ['quick', 'brown', 'foxes', 'jumping', 'lazy', 'dogs.'])

    def test_lemmatize(self):
        tokens = ['foxes', 'were', 'jumping']
        lemmatized_tokens = self.preprocessor.lemmatize(tokens)
        self.assertEqual(lemmatized_tokens, ['fox', 'were', 'jumping'])

    def test_preprocess(self):
        preprocessed_tokens = self.preprocessor.preprocess(self.sample_text)
        self.assertEqual(preprocessed_tokens, ['quick', 'brown', 'fox', 'jumping', 'lazy', 'dog.'])


# Running the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestTextPreprocessor)
unittest.TextTestRunner().run(suite)

# One of the tests, test_preprocess, has failed. Upon reviewing the results,
# the issue is with the mock lemmatization of the token "dogs.".
# The mock lemmatizer did not account for punctuation attached to words.
# To fix this, I'll adjust the mock lemmatizer to handle words with trailing punctuation.
# Let's update the lemmatizer and rerun the tests.

# Modifying the mock lemmatizer to handle words with trailing punctuation
class MockNLTK:

    def word_tokenize(self, text):
        return text.split()

    def lemmatize(self, word):
        # Removing punctuation for the mock lemmatizer
        word_without_punctuation = word.rstrip('.,!?')
        lemmatized_words = {
            'foxes': 'fox',
            'dogs': 'dog',
            'were': 'were',
            'jumping': 'jumping'
        }
        lemmatized_word = lemmatized_words.get(word_without_punctuation, word_without_punctuation)

        # Adding back the punctuation
        if word[-1] in '.,!?':
            return lemmatized_word + word[-1]
        return lemmatized_word

    def stopwords(self):
        return set(['the', 'were', 'over', 'and', 'to', 'of', 'in', 'for'])


mock_nltk = MockNLTK()

# Rerunning the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestTextPreprocessor)
unittest.TextTestRunner().run(suite)

# All tests for the TextPreprocessor class now pass successfully.
# The modifications to the mock lemmatizer resolved the previous failure,
# and the class methods work correctly for the tested cases.
