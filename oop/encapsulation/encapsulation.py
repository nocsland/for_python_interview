# Инкапсуляция

# Инкапсуляция — это третий столп объектно - ориентированного программирования. Инкапсуляция просто означает скрытие
# данных. Как правило, в объектно - ориентированном программировании один класс не должен иметь прямого доступа к данным
# другого класса. Вместо этого, доступ должен контролироваться через методы класса. Чтобы предоставить контролируемый
# доступ к данным класса в Python, используются модификаторы доступа и свойства. Мы уже ознакомились с тем, как
# действуют модификаторы доступа.В этом разделе мы посмотрим, как действуют свойства. Предположим, что нам нужно
# убедиться в том, что модель автомобиля должна датироваться между 2000 и 2018 годом. Если пользователь пытается ввести
# значение меньше 2000 для модели автомобиля, значение автоматически установится как 2000, и если было введено значение
# выше 2018, оно должно установиться на 2018. Если значение находится между 2000 и 2018, оно остается неизменным. Мы
# можем создать свойство атрибута модели, которое реализует эту логику.

# Взглянем на пример:

# создаем класс Car
class Car:

    # создаем конструктор класса Car
    def __init__(self, model):
        # Инициализация свойств.
        self.model = model

    # создаем свойство модели.
    @property
    def model(self):
        return self.__model

    # Сеттер для создания свойств.
    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model

    def get_car_model(self):
        return "Год выпуска модели " + str(self.model)


car_a = Car(2088)
print(car_a.get_car_model())

# Свойство имеет три части. Вам нужно определить атрибут, который является моделью в скрипте выше. Затем, вам нужно
# определить свойство атрибута, используя декоратор @property. Наконец, вам нужно создать установщик свойства, который
# является дескриптором @model.setter в примере выше. Теперь, если вы попробуете ввести значение выше 2018 в атрибуте
# модели, вы увидите, что значение установлено на 2018.

# Давайте проверим это. Выполним следующий скрипт:

car_a = Car(2088)
print(car_a.get_car_model())

# Здесь мы передаем 2088 как значение для модели, однако, если вы введете значение для атрибута модели через функцию
# get_car_model(), вы увидите 2018 в выдаче.