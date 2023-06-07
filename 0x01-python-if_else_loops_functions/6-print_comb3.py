#!/usr/bin/python3
for j in range(0, 9):
    for k in range(1, 10):
        if k > j:
            if j != 8:
                print("{}{}, ".format(j, k), end="")
            else:
                print("{}{}".format(j, k))
