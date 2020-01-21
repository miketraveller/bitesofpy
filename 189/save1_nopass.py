IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5



ret_list = []
def filter_names(names):
    for name in names:
        if name.startswith(QUIT_CHAR):
            break
        elif name.startswith(IGNORE_CHAR):
            continue
        elif  string.digits in name:
            continue
        else:
            ret_list.append(name)

    return ret_list[:4]