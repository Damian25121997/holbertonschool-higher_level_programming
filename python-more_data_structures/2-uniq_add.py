#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = []
    for number in my_list:
        if number not in res:
            res.append(number)
    Result = sum(res)
    return Result
