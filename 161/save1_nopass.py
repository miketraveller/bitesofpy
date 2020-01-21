import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    directories = 0
    files = 0
    for root, dirs, files in os.walk(directory):
        for f in files:
            files += 1
        for d in dirs:
            directories += 1
    return (directories, files)
        