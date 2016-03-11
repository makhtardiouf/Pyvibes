__author__ = 'Makhtar'
'''Check if a string is a palindrome'''

import sys

def isPalindrome(s):
    ok = True
    for i, j in zip(range(len(s)) , range(len(s)-2, 0, -1)):
        print("Checking: ", i, j, s[i], s[j])
        if s[i] != s[j]:
            ok = False
            break

    if ok:
        sys.stdout.write(s + " is a palindrome\n")
    else:
        sys.stdout.write(s + " is not a palindrome\n")
    sys.stdout.flush()


print("Enter strings to check or q to quit, e.g. anna, ette...: ")
s = sys.stdin.readline()

while s:
    if s == "q\n":
        break
    isPalindrome(s)
    s = sys.stdin.readline()

