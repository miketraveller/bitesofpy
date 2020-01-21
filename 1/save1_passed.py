def sum_numbers(numbers=None):
    if numbers == None:
        return sum([x for x in range(101)])
    else:
        return sum([x for x in numbers])


def sum_numbers2(numbers=None):
    if numbers is None:
        numbers = range(1, 101)
    return sum(numbers)