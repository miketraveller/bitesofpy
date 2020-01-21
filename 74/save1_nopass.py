import datetime
import calendar


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding 
    weekday string"""
    bday = datetime.datetime.strptime(date)
    return calendar.day_name[bday.weekday()]  