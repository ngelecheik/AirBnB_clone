#!/usr/bin/python3
'''this modulwe will be for testing the read and write function'''


with open("mytxt.txt", mode="a", encoding="utf-8") as my_txt:
    my_txt.write("line 1\nline 2\nline 3\n")

with open("mytxt.txt", mode='r', encoding='utf-8') as my_txt:
    print(my_txt.read())
