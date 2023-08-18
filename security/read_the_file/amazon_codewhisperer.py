# read the txt file from path C:\Users\Documents


import os
import sys


def read_file(path):
    with open(path, 'r') as f:
        return f.read()


def main(path):
    print(read_file(path))


if __name__ == '__main__':
    main(sys.argv[1])
