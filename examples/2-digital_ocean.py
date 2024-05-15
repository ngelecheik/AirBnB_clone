#!/usr/bin/python3

def print_values(**kwargs):
    for key, value in kwargs.items():
        print("{} is {}".format(key, value))


print_values(name="kiprop", role="CEO")
