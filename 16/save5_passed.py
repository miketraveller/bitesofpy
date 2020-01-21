from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    hundreds = [PYBITES_BORN + timedelta(days=(x+1)*100) for x in range(20)]
    years = [PYBITES_BORN + timedelta(days=(x+1)*365) for x in range(3)]
    hundreds_string = [str(date) for date in hundreds]
    years_string = [str(date) for date in years]
    new_list = years_string + hundreds_string
    new_list.sort(key=lambda date: datetime.strptime(date, "%Y-%m-%d %H:%M:%S"))
    for date in new_list:
        yield datetime.strptime(date, "%Y-%m-%d %H:%M:%S")