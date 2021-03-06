"""
In this bite you will work with a list of names.

First you will write a function to take out duplicates and title case them.

Then you will sort the list in alphabetical descending order by surname 
and lastly determine what the shortest first name is. For this exercise 
you can assume there is always one name and one surname.

With some handy Python builtins you can write this in a pretty concise way. Get it sorted :)
"""

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    deduped = set(names)
    capped = [n.title() for n in deduped]
    return capped



def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    sort = sorted(names, key=lambda x: x.split()[1], reverse=True)
    return sort


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    shortest = "asdkas;dkas;dkas;dkas;dk"
    for name in names:
        if len(name.split()[0]) < len(shortest):
            shortest = name.split()[0]
    return shortest


# def dedup_and_title_case_names(names):
#     """Should return a list of title cased names,
#        each name appears only once"""
#     return list({name.title() for name in names})


# def sort_by_surname_desc(names):
#     """Returns names list sorted desc by surname"""
#     names = dedup_and_title_case_names(names)
#     return sorted(names,
#                   key=lambda x: x.split()[-1],
#                   reverse=True)


# def shortest_first_name(names):
#     """Returns the shortest first name (str).
#        You can assume there is only one shortest name.
#     """
#     names = dedup_and_title_case_names(names)
#     names = [name.split()[0] for name in names]
#     return min(names, key=len)