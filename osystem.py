'''
 Python OS module demo
'''
import os

path = os.getcwd()
print(f"Welcome to python\n We're running this program from: {path}")

res = os.system("mkdir testme")
print(f"Successfully created test folder?", res == 0)

os.rmdir("testme")