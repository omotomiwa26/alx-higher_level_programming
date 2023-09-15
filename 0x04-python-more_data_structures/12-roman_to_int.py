#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numeral = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    numeral_result = 0

    if not isinstance(roman_string, str) or not roman_string:
        return 0

    for element in range(len(roman_string)):
        numeral = roman_numeral.get(roman_string[element], 0)

        if element < len(roman_string) - 1:
            next_numeral = roman_numeral.get(roman_string[element + 1], 0)
            if numeral < next_numeral:
                numeral = (-numeral)

        numeral_result += numeral

    return numeral_result
