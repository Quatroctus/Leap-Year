def leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def int_input(message: str):
    while True:
        try:
            answer = input(message)
            i = int(answer)
            return i
        except ValueError:
            print("Input is not an integer.")
    raise RuntimeError()

if __name__ == "__main__":
    year: int = int_input("Please enter a year: ")
    print(f"The year {year} is{' ' if leap_year(year) else ' not '}a leap year.")
