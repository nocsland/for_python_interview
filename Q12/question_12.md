12. Переменные в Python передаются по ссылке или по значению?

Будьте готовы спуститься в кроличью нору семантики, если загуглите этот вопрос и прочтете несколько первых страниц. В
общем, все имена передаются по ссылке, но в некоторых ячейках памяти хранятся объекты, а в других — указатели на другие
ячейки памяти.

name = 'object'

Давайте посмотрим, как это работает со строками. Создадим экземпляр имени и объекта, на который указывают другие имена.
Затем удалим первое:

x = 'some text' 
y = x 
x is y 
#=> True

del x # удаляем имя 'x' , но не объект в памяти

z = y 
y is z 
#=> True

Мы видим, что все имена указывают на один и тот же объект в памяти, который остался нетронутым после операции удаления
имени del x.

Вот еще один интересный пример с функцией:

name = 'text' 
def add_chars(str1):
    print( id(str1) ) 
#=> 4353702856 print( id(name) ) #=> 4353702856

    # новое имя, тот же объект
    str2 = str1
  
    # создаем новое имя (не отличается от предыдущего) и новый объект
    str1 += 's' 
    print( id(str1) ) #=> 4387143328
    
    # объект не изменился
    print( id(str2) ) #=> 4353702856

add_chars(name)
print(name) #=>text

Обратите внимание, что добавление буквы s в строку внутри функции создает новое имя — и новый объект тоже. Даже если у
нового объекта то же самое имя, что и у существующего.