# open a local file based on user input

import os


def read_file():
    with open(input("Enter the file path: "), "r") as f:
        print(f.read())


read_file()
