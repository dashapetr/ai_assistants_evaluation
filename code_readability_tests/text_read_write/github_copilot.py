# read the text file, remove punctuation and write it to a new text file

import string

with open("text.txt", "r") as f:
    text = f.read()

text = text.translate(str.maketrans('', '', string.punctuation))

with open("text_clean.txt", "w") as f:
    f.write(text)
