import itertools
import operator
import numpy as np
def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    seq = (list(itertools.accumulate(sequence, operator.add)))
    end = []
    for i, num in enumerate(seq):
        end.append(round(num/(i+1), 2))
    print(end)