def calc(val1, val2, func):
    return func(val1, val2)


def mul(a, b):
    return a * b


print(calc(10, 10, mul))
