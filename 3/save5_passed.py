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
    return max(words, key=calc_word_value)

# wds = load_words()

# max = max_word_value(wds)

# def load_words():
#     """Load the words dictionary (DICTIONARY constant) into a list
#        and return it"""
#     with open(DICTIONARY) as f:
#         return [word.strip() for word in f.read().split()]


# def calc_word_value(word):
#     """Given a word calculate its value using the LETTER_SCORES dict"""
#     return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# def max_word_value(words):
#     """Given a list of words calculate the word with the maximum value and return it"""
#     return max(words, key=calc_word_value)