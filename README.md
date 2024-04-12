# Calculator
 
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