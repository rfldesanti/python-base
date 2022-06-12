#!/usr/bin/env python3
"""Hello World Multi Linguas

Dependendo da lingua configurada no ambiente, o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada. Ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.2"
__author__ = "Rafael"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]
# another way to do the same as the code above:
# current_language = os.getenv("LANG", "en_US").split(".")[0]

msg = {
        "en-US": "Hello, World!",
        "pt_BR": "Olá, Mundo!",
        "it_IT": "Ciao, Mondo!",
        "es_SP": "Hola, Mundo!",
        "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language])

