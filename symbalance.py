#
# Balanced tokens checker
# More general solution than http://interactivepython.org/runestone/static/pythonds/BasicDS/SimpleBalancedParentheses.html
# $Id$
__author__ = "Makhtar Diouf"

symbols = {'{': '}', '(': ')', '[': ']'}

def isbalanced(_target):
    # Opening
    ostack = list()
    # Matching closing symbol
    cstack = list()
    for s in list(_target):
        # Ignore characters not in the table
        #ostack = [s for s in symbols]
        if s in symbols:
            ostack.append(s)
        elif s in symbols.values():
            cstack.append(s)

    #print(ostack, cstack)
    if len(ostack) == len(cstack):
        i = 0
        for s in ostack:
            print(s, symbols[s])
            if not (ostack.count(s) == cstack.count(symbols[s])):
                return False
            elif ostack.index(s, i) == cstack.index(symbols[s], i):
                print("Match: ", s, symbols[s])
                #break #continue
            else:
                return False
            i += 1
        return True
    return False


print(isbalanced('((([abc])))'))
print(isbalanced('ac(()'))
print(isbalanced(')xya('))

