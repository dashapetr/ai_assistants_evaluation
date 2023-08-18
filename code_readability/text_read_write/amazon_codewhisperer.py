# read the text file, remove punctuation and write it to a new text file


def remove_punct(file_name):
    file = open(file_name, 'r')
    new_file = open('new_file.txt', 'w')
    for line in file:
        line = line.strip()
        line = line.replace(',', '')
        line = line.replace('.', '')
        line = line.replace('!', '')
        line = line.replace('?', '')
        new_file.write(line + '\n')
    file.close()
    new_file.close()
    return new_file


remove_punct('file.txt)')
