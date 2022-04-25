7. В чем разница между методами экземпляра, класса и статическими методами в Python?

Методы экземпляра: принимают параметр self и относятся к определенному экземпляру класса.

Статические методы: используют декоратор @staticmethod, не связаны с конкретным экземпляром и являются автономными (
атрибуты класса или экземпляра не изменяются).

Методы класса: принимают параметр cls, можно изменить сам класс.

Проиллюстрируем разницу на вымышленном классе CoffeeShop:

class CoffeeShop:
specialty = 'espresso'

    def __init__(self, coffee_price):
        self.coffee_price = coffee_price
  
    # instance method
    def make_coffee(self):
        print(f'Making {self.specialty} for ${self.coffee_price}')
 
    # static method    
    @staticmethod
    def check_weather():
        print('Its sunny')

    # class method
    @classmethod
    def change_specialty(cls, specialty):
        cls.specialty = specialty
        print(f'Specialty changed to {specialty}')

У класса CoffeeShop есть атрибут specialty (фирменный напиток), установленный по умолчанию в значение 'espresso'. Каждый
экземпляр CoffeeShop инициализируется с атрибутом coffee_price. У него также три метода: метод экземпляра, статический
метод и метод класса.

Давайте инициализируем экземпляр с атрибутом coffee_price, равным 5. Затем вызовем метод экземпляра make_coffee:

coffee_shop = CoffeeShop('5')
coffee_shop.make_coffee()
#=> Making espresso for $5

Теперь вызовем статический метод. Статические методы не могут изменять состояние класса или экземпляра, поэтому обычно
используются для служебных функций, например, сложения двух чисел. Наши проверяют погоду. Говорят, что солнечно.
Отлично!

coffee_shop.check_weather()
#=> Its sunny

Теперь используем метод класса для изменения фирменного напитка (specialty), а затем сделаем кофе (make_coffee):

coffee_shop.change_specialty('drip coffee')
#=> Specialty changed to drip coffee

coffee_shop.make_coffee()
#=> Making drip coffee for $5

Обратите внимание, что make_coffee раньше делал эспрессо, а теперь заваривает капельную кофеварку (drip coffee).