import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class Preprocessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = nltk.stem.WordNetLemmatizer()
        self.tokens = []
        self.lemmas = []
        self.clean_text = ""

        self.preprocess()
        self.print_results()

    def preprocess(self):
        with open(self.file_path, 'r') as f:
            text = f.read()
            self.tokens = word_tokenize(text)
            self.tokens = [word.lower() for word in self.tokens if word.isalpha()]
            self.tokens = [word for word in self.tokens if word not in self.stop_words]
            self.lemmas = [self.lemmatizer.lemmatize(word) for word in self.tokens]
            self.clean_text = " ".join(self.lemmas)

    def print_results(self):
        print(self.clean_text)
        print(self.tokens)
        print(self.lemmas)


# create tests for text preprocessing class


if __name__ == "__main__":
    preprocessor = Preprocessor("amazon_codewhisperer.txt")
    print(preprocessor.clean_text)
    print(preprocessor.tokens)
    print(preprocessor.lemmas)
