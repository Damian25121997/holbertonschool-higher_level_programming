#!/usr/bin/python3
for number in range(0, 100):
    if number is 99:
        print("{}".format(number))
    else:
        print("{:02d}".format(number), end=", ")
