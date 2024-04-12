# coding: utf-8

"""
This script provides an advanced mathematics calculator with a command-line interface.
It includes basic arithmetic operations, a feature to draw triangles based on angles,
and comprehensive logging of operations and calculations.

The script utilises the `io` module for file handling, `math` for mathematical operations,
`fractions.Fraction` for handling fractions, and `os` for checking file existence.
External modules `utility` and `triangle` are imported for additional functionality.

The main components of the script are as follows:

- MENU_ITEMS: A dictionary that maps menu item numbers to their descriptions.
- initialisation(log, is_new_file): Initializes the calculator by reading from the log file and resetting it.
- show_menu(): Displays the main menu options to the user.
- menu(): Provides the main interactive interface for the calculator, allowing users to select operations and manage logs.
- valid_float_input(prompt): Validates user input as a float, with an option to exit input by typing 'x'.
- arithmetic functions (addition, subtraction, multiplication, division): Perform the corresponding arithmetic operations with overflow handling.
- show_formatting_submenu(is_fraction): Displays formatting options for the operation submenu.
- formatting_submenu(result, is_fraction): Handles formatting requests to the result according to the user's choice.
- running_confirmation(): Prompts the user for confirmation before exiting the program.
- upload_log(log, new_log, old_log, new_calc_count, old_calc_count): Saves all log entries and updates the total calculation count in the log file.

The script is designed to be interactive and user-friendly, with error handling and input validation to ensure a smooth user experience.
"""

import math
from fractions import Fraction
import os
import utilities, triangle
import io

ADDITION = "1"
SUBTRACTION = "2"
MULTIPLICATION = "3"
DIVISION = "4"
DRAW_TRIANGLE = "5"
EXIT = "9"

MENU_ITEMS = {
    ADDITION: "Addition",
    SUBTRACTION: "Subtraction",
    MULTIPLICATION: "Multiplication",
    DIVISION: "Division",
    DRAW_TRIANGLE: "Draw Triangle",
    EXIT: "Exit Program",
}


def initialisation(log: io.TextIOWrapper, is_new_file: bool) -> tuple[list[str], int]:
    """
    Initialise the calculator by reading from the log file and resetting the log.

    Args:
        log (io.TextIOWrapper): The file instance for the logs.
        is_new_file (bool): Flag indicating whether the log file is new.

    Returns:
        old_log (list[str]): The lines from the previous log.
        old_calc_count (int): The number of previous calculations.
    """
    log.seek(0)
    if not is_new_file:
        old_calc_msg = log.readline()[20:].rstrip()
        old_calc_count = utilities.morse2num(old_calc_msg) if old_calc_msg else 0
        log.seek(0)
        old_log = log.readlines()[1:]
    else:
        old_calc_count = 0
        log.seek(0)
        old_log = []
    log.truncate(0)
    return old_log, old_calc_count


def show_main_menu() -> None:
    """
    Display main menu options
    """
    print("\nMenu")
    print("Select from the following:")
    for choice_num, choice in MENU_ITEMS.items():
        print(f"{choice_num}: {choice}")


def main_menu() -> tuple[list[str], int]:
    """
    Provide a terminal-based interface for the calculator, allowing users to perform basic arithmetic operations
    and draw triangles. It also handles logging and exiting the program.

    Returns:
        new_log (list[str]): The newly added lines of logs.
        new_calc_count (int): The new amount of computation done.
    """
    menu_running = True
    new_calc_count = 0
    new_log: list[str] = []
    while menu_running:
        show_main_menu()

        # Compute operations based on user input
        calc_msg = None
        new_result = None
        try:
            user_selection = input("\nPlease input a valid menu number: ")
            if user_selection == ADDITION:  # Addition
                new_addend1 = valid_float_input("Input addend 1: ")
                new_addend2 = valid_float_input("Input addend 2: ")

                new_result = addition(new_addend1, new_addend2)
                calc_msg = f"Calculation {new_addend1} + {new_addend2} = {new_result}"

            elif user_selection == SUBTRACTION:  # Subtraction
                new_minuend = valid_float_input("Input minuend: ")
                new_subtrahend = valid_float_input("Input subtrahend: ")

                new_result = subtraction(new_minuend, new_subtrahend)
                calc_msg = (
                    f"Calculation {new_minuend} - {new_subtrahend} = {new_result}"
                )

            elif user_selection == MULTIPLICATION:  # Multiplication
                new_factor1 = valid_float_input("Input factor 1: ")
                new_factor2 = valid_float_input("Input factor 2: ")

                new_result = multiplication(new_factor1, new_factor2)
                calc_msg = (
                    f"Calculation {new_factor1} {chr(215)} {new_factor2} = {new_result}"
                )

            elif user_selection == DIVISION:  # Division
                new_dividend = valid_float_input("Input dividend: ")
                new_divisor = valid_float_input("Input divisor: ")

                new_result = division(new_dividend, new_divisor)
                calc_msg = f"Calculation {new_dividend} {chr(247)} {new_divisor} = {new_result}"

            elif user_selection == DRAW_TRIANGLE:  # Draw triangle
                new_angle1 = valid_float_input("Angle 1 of triangle: ")
                new_angle2 = valid_float_input("Angle 2 of triangle: ")
                new_angle3 = valid_float_input("Angle 3 of triangle: ")
                if new_angle1 + new_angle2 + new_angle3 != 180:
                    raise ValueError(
                        "Invalid triangle! Angle sum of triangle must equal to 180˚."
                    )
                elif (new_angle1 <= 0) or (new_angle2 <= 0) or (new_angle3 <= 0):
                    raise ValueError(
                        "Invalid triangle! All angles must be bigger than 0˚."
                    )
                elif (new_angle1 < 5) or (new_angle2 < 5) or (new_angle3 < 5):
                    raise ValueError(
                        "Minimum angle accepted is 5˚for the triangle to display properly."
                    )

                print("Please view the exported PNG for the drawn triangle.")
                triangle.draw_triangle(new_angle1, new_angle2, new_angle3)

            elif user_selection == EXIT:  # Exit Program
                menu_running = running_confirmation()
            else:
                raise KeyError("That is not a main menu option!")

            # If the four basic arthimetic is done, the calc_msg would have a str value
            if calc_msg:
                print(calc_msg)

                # Manage adding the new logs
                new_log.append(f"Timestamp {utilities.roman_date()} {calc_msg}\n")
                new_calc_count += 1

                # Provide formatting option for the result
                display_fraction = not new_result.is_integer()
                formatting_submenu(new_result, display_fraction)

        except KeyError as exception:
            print(exception.args[0])
        except ZeroDivisionError:
            print("Division by zero! Please try again.")
        except OverflowError:
            print("Number too big in magnitude! Please try again.")
        except ValueError as exception:
            print(exception)

        # If user manually exited program, menu is forcefully closed to save the existing new logs
        except (EOFError, KeyboardInterrupt):
            break

        # When user want to quit inputting
        except Exception as exception:
            if exception.args == ("Quit User Input",):
                continue

    return new_log, new_calc_count


def valid_float_input(prompt: str) -> float:
    """
    Get a validated float input from the user with the given prompt.

    Args:
        prompt (str): The message to display to the user before taking input.

    Returns:
        float: The validated float input.
    """
    valid_num = False
    while not valid_num:
        try:
            strInput = input(prompt).lower()
            float_input = float(strInput)
        except ValueError:
            if strInput == "x" or strInput == "exit":
                raise Exception("Quit User Input")
            print("Invalid number! Please try again. Type 'x' to exit inputting")
        else:
            valid_num = True
    return float_input


def addition(addend1: float, addend2: float) -> float:
    """
    Perform addition on two float numbers and handle potential overflow.

    Args:
        addend1 (float): The first number to add.
        addend2 (float): The second number to add.

    Returns:
        float: The result of the addition.
    """
    sum_ = addend1 + addend2
    if math.isinf(sum_):
        raise OverflowError
    return sum_


def subtraction(minuend: float, subtrahend: float) -> float:
    """
    Perform subtraction on two float numbers and handle potential overflow.

    Args:
        minuend (float): The number from which to subtract.
        subtrahend (float): The number to subtract.

    Returns:
        float: The result of the subtraction.
    """
    difference_ = minuend - subtrahend
    if math.isinf(difference_):
        raise OverflowError
    return difference_


def multiplication(factor1: float, factor2: float) -> float:
    """
    Perform multiplication on two float numbers and handle potential overflow.

    Args:
        factor1 (float): The first multiplication factor.
        factor2 (float): The second multiplication factor.

    Returns:
        float: The result of the multiplication.
    """
    product_ = factor1 * factor2
    if math.isinf(product_):
        raise OverflowError
    return product_


def division(dividend: float, divisor: float) -> float:
    """
    Perform division on two float numbers and handle division by zero and potential overflow.

    Args:
        dividend (float): The number to be divided.
        divisor (float): The number by which to divide.

    Returns:
        float: The result of the division.
    """
    quotient_ = dividend / divisor
    if math.isinf(quotient_):
        raise OverflowError
    return quotient_


def show_formatting_submenu(is_fraction: bool) -> None:
    """
    Display formatting options for the operation submenu.

    Args:
        is_fraction (bool): Indicates if a fraction format option should be included.
    """
    print("\nFormatting Submenu")
    print("-- Select from the following:")
    print("|_ 1. Standard Format")
    print("|_ 2. Scientific Notation Format")
    print("|_ 3. Sexagesimal Format")
    if is_fraction:
        print("|_ 4. Fraction Format")
    print("|_ 9. Exit Submenu\n")


def formatting_submenu(result: float, is_fraction: bool) -> None:
    """
    Handle formatting options including display and formatting of the result.

    Args:
        result (float): The result to be formatted.
        is_fraction (bool): Indicates if the result can be formatted as a fraction.
    """
    submenu_running = True
    while submenu_running:
        show_formatting_submenu(is_fraction)
        user_selection = input("Please input a valid submenu number: ")
        if user_selection == "1":  # Display in original format
            print("    = ", result)
        elif user_selection == "2":  # Display in scientific notation format 2 d.p.
            print(f"   = {result:.2e}")
        elif user_selection == "3":  # Display in sexagesimal format
            sexagesimal_result = utilities.dec2sex(result)
            print(
                f"   = {sexagesimal_result[0]}˚ {sexagesimal_result[1]}' {sexagesimal_result[2]}''"
            )
        # Display in fractional format if it can be represented by a fraction
        elif user_selection == "4" and is_fraction:
            print(f"   = {Fraction(result).limit_denominator(1000)}")
        elif user_selection == "9":  # Exit submenu
            submenu_running = running_confirmation()
        else:
            raise KeyError("That is not a submenu option!")


def running_confirmation() -> bool:
    """
    Prompt the user for confirmation to exit the program.

    Returns:
        bool: True if the user confirms they want to exit, False otherwise.
    """
    confirmation = input("Are you sure? [y/n]: ").lower()
    while confirmation not in ("y", "n", "yes", "no"):
        print("Invalid input!\n")
        confirmation = input("Are you sure? [y/n]: ").lower()

    return confirmation in ("n", "no")


def upload_log(
    log: io.TextIOWrapper,
    new_log: list[str],
    old_log: list[str],
    new_calc_count: int,
    old_calc_count: int,
) -> None:
    """
    Save all log entries, including old and new logs, and update the total calculation count.

    Args:
        log (io.TextIOWrapper): The log file stream.
        new_log (list[str]): The newly added lines of logs.
        old_log (list[str]): The existing lines of logs.
        new_calc_count (int): The number of new calculations made.
        old_calc_count (int): The number of old calculations from previous runs.
    """
    total_calc_msg = (
        f"Total calculations: {utilities.num2morse(new_calc_count+old_calc_count)}\n"
    )
    log.writelines(total_calc_msg)
    log.writelines(old_log)
    log.writelines(new_log)
    log.close()


if __name__ == "__main__":
    # Introduction
    print("Welcome to the advanced mathematics calculator.")

    # File Initlisation
    is_new_file = not os.path.isfile("adv_calc_logs.txt")

    log = open("adv_calc_logs.txt", mode="a+")

    # Initialise the calculator with the log file
    old_log, old_calc_count = initialisation(log, is_new_file)
    # Run the calculator menu and perform calculations
    new_log, new_calc_count = main_menu()
    # Upload the logs to the file and close it
    upload_log(log, new_log, old_log, new_calc_count, old_calc_count)
