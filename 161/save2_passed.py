import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    directory_count = 0
    file_count = 0
    for root, dirs, files in os.walk(directory):
        for f in files:
            file_count += 1
        for d in dirs:
            directory_count += 1
    return (directory_count, file_count)
        