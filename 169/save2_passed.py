def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if fmt.lower() != "cm" and fmt.lower() != "in":
        raise ValueError
    
    if fmt == "in":
        return round(value/2.54, 4)
    else:
        return round(value/0.39370079, 4)