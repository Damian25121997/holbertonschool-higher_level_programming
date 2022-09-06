#!/usr/bin/python3
def uppercase(str):
    for x in str:
        x = ord(x)
        if 97 <= x <= 122:
            x = x - 32
        print("{:c}".format(x), end="")
    print()
