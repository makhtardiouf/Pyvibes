'''
Initialize your list and read in the value of  followed by  lines of commands where each command 
will be of the types listed above. Iterate through each command in order and perform the 
corresponding operation on your list.

Example:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''

arr = []
commands = {
    'insert': lambda a: arr.insert(a[0], a[1]),
    'remove': lambda x: arr.remove(x[0]),
    'append': lambda x: arr.append(x[0]),

    'print': lambda _: print(arr),
    'sort': lambda _: arr.sort(),
    'pop': lambda _: arr.pop(),
    'reverse': lambda _: arr.reverse(),
}

if __name__ == '__main__':
    #print("Awaiting input: ")
    N = int(input())
    for _ in range(N):
        cmd, *params = input().strip().split()
        params = list(map(int, params))

        if len(params) > 0:
            commands[cmd](params)
        else:
            commands[cmd](_)
