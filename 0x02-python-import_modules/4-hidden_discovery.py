#!/usr/bin/python3

if __name__ == "__main__":
    for name in sorted(hidden_4.__dict__):
        if not name.startswith('__'):
            print(name)
