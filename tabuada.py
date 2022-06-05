#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10.

---Tabuada do 1---
    1 x 1 = 1
    2 x 1 = 2
    3 x 1 = 3
...
####################

---Tabuada do 2---
    1 x 2 = 2
    2 x 2 = 4
    3 x 2 = 6
...
####################
"""
__version__ = "0.1.0"
__author__ = "Rafa"

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

# Iterable

# cabeçalho de início da tabuada:

# para cada número em números
for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        if n2 == 10:
            print("{:^20}".format(f"{n1} x {n2} = {resultado}"))
        else:
            print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print()
    print("#" * 18)
    print()

