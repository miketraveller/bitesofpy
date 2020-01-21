alphas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def get_index_different_char(chars):
    count_alphas = 0
    for char in chars:
        if str(char) in alphas:
            count_alphas +=1
    if count_alphas == 1:
        key = [char for char in t3 if str(char) not in alphas]
        return chars.index(key)
    else:
        key = [char for char in t3 if str(char) in alphas]
        return chars.index(key)
