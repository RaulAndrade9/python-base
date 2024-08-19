"""Hello World Multi Linguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem correspondente

como usar: 
Tenha a variável LANG devidamente configurada ex: export LANG=pt_BR

Execução: 
    python3 hello.py

"""

__version__ = "0.0.1"
__author__ = "Raul Andrade"
__license__ = "Unlicense "

import os

current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello World"

if current_language == "pt_BR":
    msg = "Olá Mundo!"


print(msg)
