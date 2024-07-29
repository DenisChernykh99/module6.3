class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'Такого этажа не существует')
        elif isinstance(new_floor, int):
            list_ = []
            for i in range(1, new_floor + 1):
                list_.append(i)
            print(*list_)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(self and other, House):
            if isinstance(self.number_of_floors and other.number_of_floors, int):
                return self.number_of_floors == other.number_of_floors
        else:
            print(f'Неподходящие данные')

    def __lt__(self, other):
        if isinstance(self and other, House):
            if isinstance(self.number_of_floors and other.number_of_floors, int):
                return self.number_of_floors < other.number_of_floors
        else:
            print(f'Неподходящие данные')

    def __le__(self, other):
        if isinstance(self and other, House):
            if isinstance(self.number_of_floors and other.number_of_floors, int):
                return self.number_of_floors <= other.number_of_floors
        else:
            print(f'Неподходящие данные')

    def __gt__(self, other):
        if isinstance(self and other, House):
            if isinstance(self.number_of_floors and other.number_of_floors, int):
                return self.number_of_floors > other.number_of_floors
        else:
            print(f'Неподходящие данные')

    def __ge__(self, other):
        if isinstance(self and other, House):
            if isinstance(self.number_of_floors and other.number_of_floors, int):
                return self.number_of_floors >= other.number_of_floors
        else:
            print(f'Неподходящие данные')

    def __ne__(self, other):
        if isinstance(self and other, House):
            if isinstance(self.number_of_floors and other.number_of_floors, int):
                return self.number_of_floors != other.number_of_floors
        else:
            print(f'Неподходящие данные')

    def __add__(self, value):
        if isinstance(self.number_of_floors and value, int):
            self.number_of_floors += value
            return self
        else:
            print(f'Неподходящие данные')

    def __radd__(self, value):
            return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

House1 = House('ЖК Высота', 24)
House2 = House('ЖК Южный Бульвар', 10)
print(House1)
print(House2)

print(House1 == House2)
print(House1 < House2)
print(House1 <= House2)
print(House1 > House2)
print(House1 >= House2)
print(House1 != House2)

House2 = House2 + 14
print(House2)
print(House1 == House2)

House1 += 6
print(House1)

House2 = 6 + House2
print(House2)
