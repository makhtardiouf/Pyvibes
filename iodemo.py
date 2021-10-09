__author__ = 'Makhtar'
"""
Demo trivial I/O formatting
"""
import sys
from makhtar import utils as ut

x = int(input("Please enter a number: "))

if x < 0:
    print('That is negative')
elif x == 0:
    print('Null number not allowed')
else:
    print('That is positive')

b = int(input("Enter another number: "))

print(f"Floor division test {x} // {b}: {str(x // b)}\n")

def promptUser(prompt, tries=2, reminder='Answer Yes or No please'):
    """ Prompt user to answer Yes or No """
    while True:
        res = input(prompt)

        if res in ['y', 'ye', 'yes']:
            print("That is super cool")
            return True
        elif res in ['n', 'no', 'nop', 'nope']:
            print("You should try it out")
            return False

        print(reminder)

        tries -= 1
        if tries < 0:
            print("You reached the max allowed retries, wake up John!")
            break

promptUser("Are you a blockchain tech enthusiast? ")
ut.logit("Done running {}".format(sys.argv[0]))
