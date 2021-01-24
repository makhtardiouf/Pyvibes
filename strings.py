# $Id: strings.py, fdbfe3d97370  makhtar $
# Trivial strings operations. Str are immutable sequences

s = "Hello Python World"

# slices
print(s[:5])
print(s[5:12])

print(3*s, sep=" ")
print("Length of s:", len(s))

s = s.capitalize()
r = s.split(' ')
print(r)

r = [x.upper() for x in r]
r.reverse()
print(r)

r.reverse()
r = [x.capitalize() for x in r]
# Rebuild the string
s = ' '.join(r)
print(s)

# Python 3.9
print(s.removeprefix("H"))
