import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    directors = defaultdict(list)
    with open(local) as csvFile:
        reader = csv.DictReader(csvFile, delimiter=",")
        for d in reader:
            val = Movie(d['movie_title'], d['title_year'], d['imdb_score'])
            if d['title_year'] != '':
                if int(d['title_year']) > 1960:
                    directors[d['director_name']].append(val)
    return directors

def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    scores = []
    for movie in movies:
        scores.append(float(movie[2]))
    return round((sum(scores)/len(scores)), 1)

def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    ans=[]
    for dr , ar in directors.items():
        if len(ar) >= MIN_MOVIES:
            ans.append ((dr, calc_mean_score(ar)))
    return ans