29. Как работают any() и all()?

Any возвращает true, если хоть один элемент в последовательности соответствует условию, то есть является true.

All возвращает true только в том случае, если условию соответствуют все элементы в последовательности.

a = [False, False, False]
b = [True, False, False]
c = [True, True, True]

print( any(a) )
print( any(b) )
print( any(c) )
#=> False
#=> True
#=> True

print( all(a) )
print( all(b) )
print( all(c) )
#=> False
#=> False
#=> True