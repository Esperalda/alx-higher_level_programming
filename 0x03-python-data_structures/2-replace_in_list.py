#!/usr/bin/python3
def replace_in_list(my_list, jdx, element):
    if jdx < 0 or jdx > (len(my_list) - 1):
        return (my_list)
    my_list[jdx] = element
    return (my_list)
