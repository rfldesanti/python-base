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

aulas = {
        "aula_ingles": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
        "aula_musica": ["Erik", "Carlos", "Maria"],
        "aula_danca": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

atividades = { 
        "Inglês": aulas["aula_ingles"],
        "Música": aulas["aula_musica"],
        "Dança": aulas["aula_danca"],
}

# Listar alunos em cada atividade por sala

for nome_da_atividade, atividade in atividades.items():

    print(f"Alunos da atividade {nome_da_atividade}:\n")

    # refatoração com set
    # retornar intersecção de alunos de cada sala com atividade
    atividade_sala1 = set(salas["sala1"]) & set(atividade)
    atividade_sala2 = set(salas["sala2"]).intersection(set(atividade))

    print("Sala1: ", atividade_sala1)
    print("Sala2: ", atividade_sala2)
    print()
    print("#" * 80)
