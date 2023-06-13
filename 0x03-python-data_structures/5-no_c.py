#!/usr/bin/python3
def no_c(my_string):
    slist = list(my_string)
    [slist.remove(j) for j in slist if j == 'c' or j == 'C']
    return("".join(slist))
