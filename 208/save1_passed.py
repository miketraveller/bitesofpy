from itertools import combinations
def find_number_pairs(numbers, N=10):
    combs = list(combinations(numbers, 2))
    return [it for it in combs if sum(it)==N]