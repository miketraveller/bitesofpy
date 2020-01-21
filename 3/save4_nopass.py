import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    words = []
    with open(DICTIONARY, 'r') as f:
        words = f.readlines()
    bare_words = [x.strip() for x in words]
    return bare_words

def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    value = 0
    return sum(LETTER_SCORES.get(letter.upper(), 0) for letter in word)

def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    if words is None:
        words = load_words()
    maxword = ""
    for word in words:
        if calc_word_value(word) > calc_word_value(maxword):
            maxword = word
    return maxword

# wds = load_words()

# max = max_word_value(wds)