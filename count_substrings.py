'''
Count substrings taking into account overlaps
str.count() cannot handle it
'''

def count_substring(s, sub):
    '''Count substring, including overlap '''
    found = set()
    for i in range(len(s)):
        found.add(s.find(sub, i))
        print(f"Index: {i}, hits: {list(found)}")

    return len([x for x in found if x >= 0 ])

source = "ininini"
sub = "ini"
print(f"\nNumber of sub-strings '{sub}' found in '{source}': ", count_substring(source, sub))
