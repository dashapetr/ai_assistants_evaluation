# read the text file, remove punctuation and write it to a new text file

import string

# Step 1: Read the contents of the given text file
with open("/mnt/data/text.txt", "r") as file:
    content = file.read()

# Step 2: Remove any punctuation from the contents
translator = str.maketrans('', '', string.punctuation)
cleaned_content = content.translate(translator)

# Step 3: Write the cleaned contents to a new text file
output_filename = "/mnt/data/cleaned_text.txt"
with open(output_filename, "w") as file:
    file.write(cleaned_content)

output_filename
