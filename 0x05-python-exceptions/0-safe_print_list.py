#!/usr/bin/python3
def safe_print_list(my_list=[], y=0):
    print_count = 0;
    try:
        for a in range(y):
            print(my_list[a], end="")
            printed_count += 1
            except IndexError:
        pass
    finally:
        print()
        return printed_count
