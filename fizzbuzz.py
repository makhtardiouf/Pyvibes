'''
Take in a list of integers and replaces all integers that 
are evenly divisible by 3 with the string "fizz", replaces all integers divisible by 5 with the string "buzz", 
and replaces all integers divisible by both 3 and 5 with the string "fizzbuzz".
https://realpython.com/lessons/range-vs-enumerate/#description

'''
from random import randint

def fizz_buzz(numbers: list):
    for k,v in enumerate(numbers):
        if (v % 3 == 0) and (v % 5 == 0):
            numbers[k] = "fizzbuzz"
        elif v % 3 == 0:
            numbers[k] = "fizz"
        elif v % 5 == 0:
            numbers[k] = "buzz"
    return numbers

numbers = [ randint(x, 20) for x in range(10)]
cop = numbers.copy()
res = fizz_buzz(numbers)

print(*zip(cop, res))
