#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_val = 0

    # Iterating backward makes the subtraction rule much easier to handle
    for char in reversed(roman_string):
        val = roman.get(char, 0)
        if val < prev_val:
            total -= val
        else:
            total += val
        prev_val = val

    return total
