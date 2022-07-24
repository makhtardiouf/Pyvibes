'''
Wrap text to the specified width
'''

import textwrap

def wrap(text, max_width):
    data = []
    i = 0
    for j in list(text):
        if (j % max_width) == 0:
            print(f"Indexes: {i}:{j} > {text[i]}")
            data.append[text[i:j]]
            i = j
            
    res = '\n'.join(data)
    return res

if __name__ == '__main__':
    print("Please indicate the text and width to wrap at: ")
    text, max_width = input(), int(input())
    print("Inputs: ", text, max_width)
    result = wrap(text, max_width)
    print(result)
