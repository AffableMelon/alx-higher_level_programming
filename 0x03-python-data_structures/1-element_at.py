#!/usr/bin/python3

def element_at(mylist, idx):
    if idx < 0 and idx >= len(mylist):
        return None
    elif idx >= 0:
        return (mylist[idx])
