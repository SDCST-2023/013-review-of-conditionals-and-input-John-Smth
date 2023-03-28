#!python3
"""
Debug this program so that it runs

original code:
x = input("enter a decimal number"))
xi = int(x)
if (x - xi) == 0:
    print(f"{x} is an integer")
"""
x = input("enter a decimal number:")
xi = float(x)
xy = round(xi)
if (xy - xi) == 0:
    print(f"{x} is an integer.")
else:
    print(f"{x} is not an integer.")