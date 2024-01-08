#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        output = (len(sentence), None)
    else:
        output = (len(sentence), sentence[0])
    return output
