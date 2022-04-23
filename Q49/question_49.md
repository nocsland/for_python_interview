49. Получите список ключей из словаря

Это можно сделать через передачу словаря в конструктор list():

d = {'id':7, 'name':'Shiba', 'color':'brown', 'speed':'very slow'}

list(d)
#=> ['id', 'name', 'color', 'speed']