# 27. Какая разница между словарями и JSON?
#
# Dict (словарь) — это тип данных Python, представляющий собой набор индексированных, но неупорядоченных пар
# ключ-значение.
#
# JSON — просто строка, которая следует заданному формату и предназначена для передачи данных.

import json

my_dict = {'id': 1, 'name': 'Stuffy'}

my_json = {
    "string_1": "value_1",
    "string_2": "value_2",
    "string_3": "value_3",
    "properties": [
        {
            "property_1": "one",
            "property_2": "two"

        }
    ]
}


