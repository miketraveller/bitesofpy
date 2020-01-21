IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5

def filter_names(names):
    ret_list = []
    for name in names:
        if name.startswith(QUIT_CHAR):
            break
        elif name.startswith(IGNORE_CHAR):
            continue
        elif any(char.isdigit() for char in name):
            continue
        else:
            ret_list.append(name)

    return ret_list[:5]