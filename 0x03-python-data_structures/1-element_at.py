#!/usr/bin/python3
def element_at(my_list, jdx):
    if jdx < 0 or jdx > (len(my_list) - 1):
        return None
    return (my_list[jdx])
