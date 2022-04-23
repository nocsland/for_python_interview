6. Определите класс car с двумя атрибутами: color и speed. Затем создайте экземпляр и верните speed

Вот как это сделать:

class Car :
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
car = Car('red','100mph')
car.speed
#=> '100mph'