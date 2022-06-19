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
"""
__version__ = "0.1.0"
__author__ = "Rafael"

import sys

operations = ["sum", "sub", "mul", "dfv"]

if len(sys.argv) == 1:
    operation = input("operação: ").strip()
    n1 = float(input("n1: "))
    n2 = float(input("n2: "))
elif len(sys.argv) == 4:
    operation, n1, n2 = sys.argv[1].strip(), float(sys.argv[2]), float(sys.argv[3])
else:
    print("Invalid number of arguments")
    sys.exit()

if operation not in operations:
    print(f"Invalid argument '{operation}'")
    sys.exit()

results = {
        "sum": n1 + n2,
        "sub": n1 - n2,
        "mul": n1 * n2,
        "dfv": n1 / n2
}

print(results[operation])
