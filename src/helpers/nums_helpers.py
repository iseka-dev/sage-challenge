from src.logger import log


def max_com_div(a, b):
    temp = a
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def min_com_mult(a, b):
    return (a * b) / max_com_div(a, b)


def lower_common_multiple_array(numbers):
    """Returns Lower Common multiple for an array of numbers"""
    result = numbers[0]
    for i in numbers[1:len(numbers)+1]:
        log.debug(i)
        result = min_com_mult(result, i)
        log.debug(result)
    return result
