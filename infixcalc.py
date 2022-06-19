#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
dfv -> /

Uso:
    $ infixcalc.py sum 5 2
    7
    
    $ infixcalc.py mul 10 5
    50

    $infixcalc.py
    operação: sum
    n1: 5
    n2: 4
    9

    Os resultados serão salvos em 'infixcal.log'
"""
__version__ = "0.1.0"

import sys
import os

arguments = sys.argv[1:]

if not arguments:
    operation = input("operação: " )
    n1 = input("n1: ")
    n2 = input("n2: ")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Invalid number of arguments")
    print("See documentation for more information")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")

if operation not in valid_operations:
    print("Invalid operation")
    print("See documentation for more information")
    sys.exit(1)

validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Invalid number {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    
    validated_nums.append(num)

n1, n2 = validated_nums

results = {
        "sum": n1 + n2,
        "sub": n1 - n2,
        "mul": n1 * n2,
        "div": n1 / n2
}

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")

with open(filepath, "a") as file_:
    file_.write(f"{operation}, {n1}, {n2} = {results[operation]}\n")

print(results[operation])
