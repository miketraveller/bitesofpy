VOWELS = 'aeiou'
PYTHON = 'python'

def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    if not [char for char in input_str if char.lower() not in VOWELS]:
        return True
    else:
        return False


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    if [char for char in input_str if char.lower() in PYTHON]:
        return True
    else:
        return False


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    if [char for char in input_str if char.isnumeric()]:
        return True
    else:
        return False