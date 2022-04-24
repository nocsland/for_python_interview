40. Как реализуется наследование классов в Python?

В приведенном ниже примере класс Audi является наследником Car. И вместе с этим наследуются методы экземпляра
родительского класса:

class Car():
    def drive(self):
        print('vroom')
class Audi(Car):
    pass
audi = Audi()
audi.drive()