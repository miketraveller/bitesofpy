from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here

# Blog = namedtuple('Blog', 'name founders stated tags location site')


def dict2nt(dict_):
    return namedtuple('Blog', dict_.keys())(**dict_)


def nt2json(nt):
    od = nt._asdict()
    return json.dumps(od, indent=4, sort_keys=True, default=str)

# # define namedtuple here
# Blog = namedtuple('Blog', blog.keys())


# def dict2nt(dict_):
#     return Blog(**dict_)


# def nt2json(nt):
#     nt = nt._replace(started=str(nt.started))
#     return json.dumps(nt._asdict())