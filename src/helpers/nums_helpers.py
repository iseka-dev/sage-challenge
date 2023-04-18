def max_com_div(a, b):
    temp = 0
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def min_com_mult(a, b):
    return (a * b) / max_com_div(a, b)


def lower_common_multiple_array(numbers):
    """Función para calcular el mínimo múltiplo común (MMC) de un arreglo de números."""
    result = 0
    for i in numbers:
        result = min_com_mult(result, i)
    return result
