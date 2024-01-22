#!/usr/bin/python3
def safe_print_list(my_list=[], y=0):
    printed_count = 0
    try:
        for x in range(y):
            print(my_list[x], end="")
            printed_count += 1
    except IndexError:
        pass

    print()
    return printed_count
