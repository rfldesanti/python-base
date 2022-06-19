#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.1"

# Dados
salas = {
        "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
        "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"],
}

atividades = { 
        "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
        "Música": ["Erik", "Carlos", "Maria"],
        "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

# Listar alunos em cada atividade por sala

for nome_da_atividade, alunos in atividades.items():

    print(f"Alunos da atividade {nome_da_atividade}:\n")

    # refatoração com set
    # retornar intersecção de alunos de cada sala com atividade
    atividade_sala1 = set(salas["sala1"]) & set(alunos)
    atividade_sala2 = set(salas["sala2"]).intersection(set(alunos))

    print("Sala1: ", atividade_sala1)
    print("Sala2: ", atividade_sala2)
    print()
    print("#" * 80)
