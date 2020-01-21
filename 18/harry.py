import os
import urllib.request
from collections import Counter

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)

c = Counter()
def get_harry_most_common_word():
    with open(stopwords_file) as f:
        stop_list = f.read()
        stop_words = [word for word in stop_list.split('\n')]
    with open(harry_text) as f:
        harry_list = f.read()
        harry_words = [word.lower() for word in harry_list.split() if  (word.lower() not in stop_words) & (word.isalpha())]
        for word in harry_words:
            c[word] += 1
    return c.most_common(1)[0]