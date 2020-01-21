def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + 
       file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    lines = 0
    words = 0
    chars = 0
    with open(file_) as f:
        for line in f.readlines():
            lines += 1
            for word in line.split(" "):
                words +=1
                for char in word:
                    chars += 1
    return str(lines) + " " + str(words) + " " + str(chars) + " " + str(file_)

