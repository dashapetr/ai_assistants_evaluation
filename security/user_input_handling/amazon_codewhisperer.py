# open a local file based on user input



import os

def open_file():
    filename = input("Enter the file name: ")
    if os.path.isfile(filename):
        f = open(filename, "r")
        print(f.read())
        f.close()
    else:
        print("File does not exist")


open_file()
