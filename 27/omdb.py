import json
import re

def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = []
    for file in files:
        with open(file) as f:
            movies.append(f.read())

    return [json.loads(movie) for movie in movies]



def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    return str([movie['Title'] for movie in movies if 'Comedy' in movie['Genre']][0])

def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    noms = [(movie['Title'], re.split('&', movie["Awards"])[1]) for movie in movies]
    noms_int = [(nom[0], int(nom[1][:3])) for nom in noms]
    return(sorted(noms_int, key=lambda noms_int: noms_int[1], reverse=True))[0][0]


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    runs = [(movie['Title'], movie['Runtime']) for movie in movies]
    return sorted(runs)[0][0]


# import json
# import re


# def get_movie_data(files: list) -> list:
#     """Parse movie json files into a list of dicts"""
#     movies = []
#     for fi in files:
#         with open(fi) as f:
#             json_ = json.loads(f.read())
#         movies.append(json_)
#     return movies


# def _grep_movies(movies, key):
#     for movie in movies:
#         yield movie.get('Title'), movie.get(key)


# def get_single_comedy(movies: list) -> str:
#     """Return the movie with Comedy in Genres"""
#     movies = dict(_grep_movies(movies, 'Genre'))
#     comedies = {k: v for k, v in movies.items() if 'Comedy' in v}
#     return list(comedies.keys())[0]


# def get_movie_most_nominations(movies: list) -> str:
#     """Return the movie that had the most nominations"""
#     movies = dict(_grep_movies(movies, 'Awards'))
#     extract_nominations = lambda m: int(re.sub(r'.*\s(\d+)\snomin.*', r'\1', m[1]))  # noqa E731 E501
#     return max(movies.items(), key=extract_nominations)[0]