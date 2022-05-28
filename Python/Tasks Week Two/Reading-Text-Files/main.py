# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
from collections import Counter


def read_file_content(filename):
    with open(filename) as file_content:
        contents = file_content.read()
    # print(contents)
    return contents

# read_file_content("story.txt")


def count_words():
    text = read_file_content("./story.txt")
    words = text.strip().split()
    # counting_words = Counter(words)
    # print(counting_words)
    counter = dict()

    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    return counter


print(count_words())
