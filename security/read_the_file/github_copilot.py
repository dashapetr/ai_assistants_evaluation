# read the txt file from path C:\Users\Documents

import os


def read_file():
    with open("C:\\Users\\Documents\\test.txt", "r") as f:
        print(f.read())


read_file()
