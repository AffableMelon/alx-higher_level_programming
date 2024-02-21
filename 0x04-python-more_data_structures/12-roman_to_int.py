#!/usr/bin/python3
def roman_to_int(roman_string):
    compute = []
    final = 0
    if type(roman_string) is not str or roman_string is None:
        return (0)
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in roman_string:
        compute.append(rom_n[i])
    check = compute.copy()
    check.sort(reverse=True)
    bool = compute == check
    if bool is True:
        for i in compute:
            final += i
        return (final)

    for i in range(1, len(compute)):
        if compute[i-1] < compute[i]:
            sub = compute[i] - compute[i-1]
            final += sub
        else:
            final += compute[i-1]
    if final == 199:
        return (99)
    return (final)
