#!/usr/bin/python3
def multiply(*args):
    """multiply unknown number of arguments"""

    mul = 1
    for i in args:
        mul *= i
    print(mul)


multiply(2, 3)
multiply(2, 3, 6)
multiply(2, 3, 9, 7, 5)
