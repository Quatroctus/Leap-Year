from typing import Callable


def leap_year(year: int) -> bool:
    """Return whether the int parameter is a leap year.
    If the year is a multiple of 4 and the year is not a multiple of 100.
    Or year is a multiple of 400.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def validate_int(s: str) -> bool:
    """Return True if the string can be converted to an integer using base 10 digits, otherwise return False."""
    try:
        int(s)
        return True
    except ValueError:
        print("Input was not an integer.")
        return False


def validate_year(s: str) -> bool:
    """Return True if the string when converted to an integer using base 10 digits is a positive integer, otherwise return False."""
    if int(s) > 0:
        return True
    print("Years cannot be negative or zero.")
    return False


def int_input(message: str, validate: Callable[[str], bool] = validate_int) -> int:
    """Obtain user input from the console until validate returns True and return that input as an int."""
    answer = input(message)
    while not validate(answer):
        answer = input(message)
    return int(answer)


if __name__ == "__main__":
    year: int = int_input("Please enter a year: ", lambda s: validate_int(s) and validate_year(s))
    print(f"The year {year} is{' ' if leap_year(year) else ' not '}a leap year.")
