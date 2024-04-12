# coding: utf-8

"""
This Python script provides a collection of functions for number conversion, including integer to Morse code, Morse code to integer, integer to Roman numerals, and decimal time to hours, minutes, and seconds. Additionally, it includes a utility function to calculate the midpoint between two points in a 2D space. The script demonstrates the use of dictionaries for mapping, string manipulation, and mathematical conversions.

Main features:
- Conversion of integers to their Morse code representation and vice versa.
- Conversion of integers to Roman numerals, with support for numbers up to 3999.
- Formatting of the current date into Roman numerals in the format D.M.Y.
- Conversion of decimal degrees into hours, minutes, and seconds, useful for time representation.
- Calculation of the midpoint between two 2D points.

The script also includes an example usage section at the end, which showcases how to use the functions to print the Roman numeral representation of the current date, convert a decimal time value to H:M:S format, and calculate the midpoint of two 2D coordinates.

The functions are designed to be reusable and can be easily integrated into other Python projects that require number conversion or manipulation.
"""

from datetime import date
import math
from typing import Tuple

NUM2MORSE_DICT = {
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

MORSE2NUM_DICT = {
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0",
}

ROMAN_NUMERAL_MAP = (
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
)


def num2morse(num: int) -> str:
    """
    Convert an integer to its equivalent Morse code representation.

    Args:
        num (int): The number to convert.

    Returns:
        str: Morse code representation of the number.
    """
    cipher = ""
    for digit in str(num):
        cipher += NUM2MORSE_DICT[digit] + " "
    return cipher.strip()  # Remove trailing space


def morse2num(morse: str) -> int:
    """
    Convert a Morse code string to the corresponding integer.

    Args:
        morse (str): The Morse code string to convert.

    Returns:
        int: The integer representation of the Morse code.
    """
    processed_morses = morse.split()
    decipher = ""
    for processed_morse in processed_morses:
        decipher += MORSE2NUM_DICT[processed_morse]
    return int(decipher)


def num2roman(num: int) -> str:
    """
    Convert a number to its corresponding Roman numeral representation.

    Args:
        num (int): The number to convert (must be less than 4000).

    Returns:
        str: The Roman numeral representation of the number.
    """
    if num == 0:
        return "N"  # Use 'N' for zero in Roman numerals

    roman_num = ""
    for numeral, integer in ROMAN_NUMERAL_MAP:
        while num >= integer:
            roman_num += numeral
            num -= integer
    return roman_num


def roman_date() -> str:
    """Return current timestamp in Roman numerals in the format of D.M.Y"""

    # Get day, month and year in numerical form
    today_day = date.today().day
    today_month = date.today().month
    today_year = date.today().year

    # Convert day, month and year from numerical form to roman numeral form
    roman_day = num2roman(today_day)
    roman_month = num2roman(today_month)
    roman_year = num2roman(today_year)

    return f"{roman_day}.{roman_month}.{roman_year}"


def dec2sex(deci: float) -> Tuple[float, float, float]:
    """
    Convert a decimal number representing a time in degrees to hours, minutes, and seconds.

    Args:
        deci (float): The decimal number representing the time in degrees.

    Returns:
        Tuple[float, float, float]: A tuple containing hours, minutes, and seconds.
    """
    (hfrac, hour) = math.modf(deci)
    (min_frac, min) = math.modf(hfrac * 60)
    sec = min_frac * 60.0
    return (int(hour), int(min), round(sec, 2))


def midpoint(pt1: Tuple[float, float], pt2: Tuple[float, float]) -> Tuple[float, float]:
    """
    Calculate the midpoint between two points in a 2D space.

    Args:
        pt1 (Tuple[float, float]): The coordinates of the first point.
        pt2 (Tuple[float, float]): The coordinates of the second point.

    Returns:
        Tuple[float, float]: The coordinates of the midpoint.
    """
    mid_x = (pt1[0] + pt2[0]) / 2
    mid_y = (pt1[1] + pt2[1]) / 2
    mid_pt = (mid_x, mid_y)
    return mid_pt


# Example usage
if __name__ == "__main__":
    print(roman_date())
    print(dec2sex(123.456))
    print(midpoint((0, 0), (1, 1)))
