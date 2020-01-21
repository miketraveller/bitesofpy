import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()



# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    c = Counter()

    tree = ET.ElementTree(ET.fromstring(content))
    root = tree.getroot()

    for it in root.iter('category'):
        print(it.text)
        c[it.text] += 1
    
    return c.most_common(n)

# TAG_HTML = re.compile(r'<category>([^<]+)</category>')


# # start coding

# def get_pybites_top_tags(n=10):
#     """use Counter to get the top 10 PyBites tags from the feed
#        data already loaded into the content variable"""
#     tags = TAG_HTML.findall(content)
#     return Counter(tags).most_common(n)