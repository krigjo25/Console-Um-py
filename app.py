#   Um
#   Importing repositories
import re
import sys


def main():
    print(count(input("Text: ").lower()))


def count(arg):

    #   Initializing a list
    arg = [i for i in str(arg).lower().split(' ')]

    #   Initializing variable
    counter = 0

    #   Counting the words "Um" in the list
    for i in arg:

        #   Ensure the regex matches for each element in the list
        if re.search(r'^(um)', i, re.I):
            counter += 1 if not 'mm' in i else 0

    return counter


if __name__ == "__main__":
    main()