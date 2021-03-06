# 51. В чем разница между remove, del и pop?

# remove() удаляет первое совпадающее значение:
li = ['a', 'b', 'c', 'd']
li.remove('b')
print(li)
# => ['a', 'c', 'd']

# del удаляет элемент по его индексу:
li = ['a', 'b', 'c', 'd']
del li[0]
print(li)
# => ['b', 'c', 'd']

# pop() удаляет элемент по индексу и возвращает этот элемент:
li = ['a', 'b', 'c', 'd']
print(li.pop(2))
# => 'c'
print(li)
# => ['a', 'b', 'd']
