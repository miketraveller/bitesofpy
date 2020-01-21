from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    hundreds = [PYBITES_BORN + timedelta(days=(x+1)*100) for x in range(20)]
    years = [PYBITES_BORN + timedelta(days=(x+1)*365) for x in range(3)]
    for i, j in zip(hundreds, years):
        yield i
        yield j