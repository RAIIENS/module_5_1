# Создаём класс House
class House:
# Внутри класса House прописываем метод __init__, в который пропишем название здания
# и кол-во этажей.
    def __init__(self, name, number_of_floors):
# Внутри метода __init__ создаём атрибуты объекта self.name и self.number_of_floors
# и присваиваем им переданные значения.
        self.name = name
        self.number_of_floors = number_of_floors
# Создаём метод go_to с параметром new_floor и пишем логику внутри него согласно
# поставленной задачи.
# Теперь появляется человечек, который будет ходить по домам по разным этажам: :=))
    def go_to(self, new_floor):
        floor = 0
        print(f'Здание {self.name} имеет {self.number_of_floors} этажей \nПоднимаемся '
              f'на {new_floor}-й')
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'{new_floor} - такого этажа не существует')
        else:
            for floor in range(new_floor):
                print(floor + 1)

h1 = House('ЖК Горский', 18)
h1.go_to(5)
h1.go_to(19)
h2 = House('Домик в деревне', 2)
h2.go_to(2)
h2.go_to(10)
