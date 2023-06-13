#!/usr/bin/python3
def delete_at(my_list=[], jdx=0):
    if jdx < 0 or jdx > (len(my_list) - 1):
        return (my_list)
    del my_list[jdx]
    return (my_list)
