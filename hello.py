"""Hello World Multi Linguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem correspondente

como usar: 
Tenha a variável LANG devidamente configurada ex: export LANG=pt_BR

ou informe através do CLI argument --lang
ou o usuário terá que digitar

Execução: 
    python3 hello.py

"""

__version__ = "0.1.3"
__author__ = "Raul Andrade"
__license__ = "Unlicense "

import os
import sys

arguments = {
    "lang": None,
    "count": 2,
}

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value
    




current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG", "en_US")[:5]


msg = {
    "en_US": "Hello World",
    "pt_BR": "Olá Mundo",
    "it_IT": "Ciao Mondo",
    "es_SP": "Hola Mundo",
    "fr_FR": "Bonjour Monde",
}


print(msg[current_language] * int(arguments["count"]))
