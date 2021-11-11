"""Check if input is a leap year, that is contains a leap day, February 29th

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
    The year can be evenly divided by 100, it is NOT a leap year, unless:
        The year is also evenly divisible by 400. Then it is a leap year.

e.g 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years
"""
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

try:
    print("Input year or Enter to quit...")
    year = input(">> ").strip()
    while year:
        res = is_leap(int(year))
        print(f"{year} {'is a leap year' if res else 'is not a leap year'}")
        year = input(">> ").strip()

    print("Thank you for programming with us")

except Exception as e:
    print(f"Error: {e}")
    