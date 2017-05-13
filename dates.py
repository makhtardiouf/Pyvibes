__author__ = 'Makhtar'
import datetime

now = datetime.date.today()
now2 = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print(now2)

birth = datetime.date(1981, 5, 16)
print("Your are ", str(now.year - birth.year), " years old !?")
