def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    return [pos for pos, char in enumerate(text) if char != ' '][0]