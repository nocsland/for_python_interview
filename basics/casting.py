# Приведение к int
i = "123"
i = int(i)
print(type(i))

# Приведение к float
f = 2
f = float(f)
print(type(f))

# Дробная или целая часть числа в строке может отсутствовать, функция float все равно сработает верно
print(float(".1"))
print(float("1"))
print(float("1."))


