alphas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def get_index_different_char(chars):
    characters = []
    non_characters = []
    for pos, char in enumerate(chars):
        if str(char) != '' and str(char) in alphas:
            characters.append((pos, char))
        else:
            non_characters.append((pos, char))

    if len(non_characters) < len(characters):
        # print(non_characters[0][0])
        return non_characters[0][0]
    else:
        # print(characters[0][0])
        return characters[0][0]
