# 20. Как объединить два массива?

# Помните, что массивы — это не списки. Это библиотека Numpy и здесь работает линейная алгебра.
# Для объединения массивов нужно использовать соответствующую функцию Numpy:

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([1, 2, 3])
d = np.array([1, 2, 3])

print(np.concatenate((a, b)))
print(c + d)

# => array([1, 2, 3, 4, 5, 6])