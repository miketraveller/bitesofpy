def get_profile(name=None, profession=None):
    params = locals()
    if len(params) > 2:
        raise TypeError
    if len(params) == 2 and params[profession] == None:
        return "{} is a programmer".format(name)
    if not name and not profession:
        return 'julian is a programmer'
    else:
        return "{} is a {}".format(name, profession)