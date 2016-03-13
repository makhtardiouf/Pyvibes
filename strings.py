__author__ = 'makhtar'
# Trivial strings operations

s = "hello python world"

# slice
print(s[5:12])

print(3*s, " ")
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


#Python strings cannot be changed — they are immutable.
#s[0] = 'J'  # error

