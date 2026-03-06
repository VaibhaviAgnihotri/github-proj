import sys
def add(a, b):
    c=a+b
    return c
def subtract(a, b):
    c=a-b
    return c
def multiply(a, b):
    c=a*b
    return c
num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])
if operation == "add":
    print(add(num1, num2))
if operation == "subtract":
    print(subtract(num1, num2))
if operation == "multiply":
    print(multiply(num1, num2))