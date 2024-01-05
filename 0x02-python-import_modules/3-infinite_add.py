#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    int_list = list(map(int, sys.argv[1:]))

    print(sum(int_list))
