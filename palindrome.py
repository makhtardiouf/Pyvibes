__author__ = 'Makhtar'
'''Check if a string is a palindrome: reversing it gives the same string'''

import sys

def isPalindrome(s):
    ok = True
    # Double iteration
    for i, j in zip(range(len(s)) , range(len(s)-1, 0, -1)):
        print("Checking: ", i, j, s[i], s[j])
        if s[i] != s[j]:
            ok = False
            break

    if ok:
        sys.stdout.write(s + " is a palindrome\n")
    else:
        sys.stdout.write(s + " is not a palindrome\n")
    sys.stdout.flush()


prompt = "\nEnter string or q to quit, e.g. anna, ette...: "
s = input(prompt)

while s:
    if s in ("q", "quit"):
        break

    isPalindrome(s)
    s = input(prompt)

