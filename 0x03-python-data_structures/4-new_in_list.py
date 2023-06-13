#!/usr/bin/python3
def new_in_list(my_list, kdx, element):
    if kdx < 0 or kdx > (len(my_list) - 1):
        return (my_list[:])
    new_list = my_list[:]
    new_list[kdx] = element
    return (new_list)
