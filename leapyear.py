"""Check if input is a leap year """

year = int(input("Input year: ").strip())

res = (year % 4 == 0) and (year % 400 == 0 or (year % 100 != 0))

print(f"Is {year} a leap year? {'Yes it is' if res else 'No it is not!'}")
