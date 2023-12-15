import sys

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    year_to_check = 2023
    result = is_leap_year(year_to_check)
    if result:
        print(f"{year_to_check} is a leap year.")
    else:
        print(f"{year_to_check} is not a leap year.")
