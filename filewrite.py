#!/usr/bin/python3
""" Test file writing """

target = "filewrite.log"
prompt = "<> "
print("Welcome to the dynamic text editor".ljust(30, '-'))
print("Press [ENTER] to exit")

try:
    n = 0
    line = ""
    with open(target, "w") as fp:
        while fp.writable() :
            line = input(prompt)
            if len(line) < 1:
                break
            fp.write(line)
            fp.write('\n')
            n += 1

        fp.write('\n')
    print(f"{'-' * 10}Wrote {n} lines to {target}")

except Exception as e:
    print(f"An error occured: {e}")
