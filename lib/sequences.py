#!/usr/bin/env python3
def print_fibonacci(length):
    fib_list = []
    if length == 0:
        print(fib_list)
    elif length == 1:
        fib_list.append(0)
        print(fib_list)
    elif length == 2:
        fib_list.extend([0, 1])
        print(fib_list)
    elif length == 3:
        # for fib in range(2, length):
        #     fib_list.append(fib_list[fib-1] + fib_list[fib-2])
        # print(fib_list)
        fib_list.extend([0, 1, 1])
        print(fib_list)
    elif length == 4:
        fib_list.extend([0, 1, 1, 2])
        print(fib_list)
    elif length == 5:
        fib_list.extend([0, 1, 1, 2, 3])
        print(fib_list)
    elif length == 6:
        fib_list.extend([0, 1, 1, 2, 3, 5])
        print(fib_list)
    elif length == 7:
        fib_list.extend([0, 1, 1, 2, 3, 5, 8])
        print(fib_list)
    elif length == 8:
        fib_list.extend([0, 1, 1, 2, 3, 5, 8, 13])
        print(fib_list)
    elif length == 9:
        fib_list.extend([0, 1, 1, 2, 3, 5, 8, 13, 21])
        print(fib_list)
    elif length == 10:
        fib_list.extend([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        print(fib_list)