from decimal import Decimal


def round_even(number):
    """Takes a number and returns it rounded even"""
    a = str(number).split('.')
    if a[1] == '5':
        even = int(Decimal(number+0.5))
        if even % 2 == 0:
            return even
        else:
            return even-1
    else:
        return int(round(number, 0))