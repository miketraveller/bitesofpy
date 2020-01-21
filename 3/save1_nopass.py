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
    with open("/tmp/dictionary.txt", 'r') as f:
        line = f.readline()
        while line:
            words.append(line)
    return words

def calc_word_value(word):
    pass
    # """given a word calculate its value using LETTER_SCORES"""
    # value = 0
    # for letter in word:
    #     if letter in LETTER_SCORES.keys():
    #         value += LETTER_SCORE[letter]
    # return value
        

def max_word_value(words=None):
    pass
#     """given a list of words return the word with the maximum word value"""
#     if words is None:
#         words = load_words()
#     maxword = ""
#     for word in words:
#         if calc_word_value(word) > calc_word_value(maxword):
#             maxword = word
#     return maxword
    
# ans = max_word_value(load_words())
# print(ans)
