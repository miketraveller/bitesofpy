def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    linesList = []
    with open(filepath) as f:
        for i, line in enumerate(f.readlines()):
            if i == n or i == n-1:
                linesList.append(line[:-2])
    return(linesList)

