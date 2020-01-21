def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    linesList = []
    with open(filepath) as f:
        content = f.read()
        lines = [line for line in content.split('\n')]
    return lines[n-1:]
