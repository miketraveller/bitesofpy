def positive_divide(numerator, denominator):

    # if not numerator.isdigit() or denominator.isdigit:
    #     raise TypeError

    try:
        answer = numerator / denominator
        if answer >=0:
            return answer
        else:
            raise ValueError
    except ZeroDivisionError as e:
        return 0
    except TypeError as e:
        raise e
