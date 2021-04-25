from typing import Callable


def leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def validate_int(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        print("Input was not an integer.")
        return False


def validate_year(s: str) -> bool:
    if int(s) > 0:
        return True
    print("Years cannot be negative or zero.")
    return False


def int_input(message: str, validate: Callable[[str], bool] = validate_int) -> int:
    answer = input(message)
    while not validate(answer):
        answer = input(message)
    return int(answer)


if __name__ == "__main__":
    year: int = int_input("Please enter a year: ", lambda s: validate_int(s) and validate_year(s))
    print(f"The year {year} is{' ' if leap_year(year) else ' not '}a leap year.")
