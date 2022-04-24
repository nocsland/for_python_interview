# 26. Что такое pickle?
#
# Pickle — это модуль сериализации и десериализации объектов в Python.
# В примере ниже мы сериализуем и десериализуем список словарей:

import pickle

obj = [
    {'id': 1, 'name': 'Stuffy'},
    {'id': 2, 'name': 'Fluffy'}
]

with open('file.p', 'wb') as f:
    pickle.dump(obj, f)

with open('file.p', 'rb') as f:
    loaded_obj = pickle.load(f)

print(loaded_obj)
# => [{'id': 1, 'name': 'Stuffy'}, {'id': 2, 'name': 'Fluffy'}]
