def get_profile(*name, profession):
    params = locals()
    if len(params) > 2:
        raise TypeError
    if len(params) == 1:
        return "{} is a programmer".format(name)
    if not name and not profession:
        return 'julian is a programmer'
    else:
        return "{} is a {}".format(name, profession)