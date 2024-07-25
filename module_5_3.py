# Реализуйте класс House, объекты которого будут создаваться следующим образом:
# House('ЖК Эльбрус', 30)
# Объект этого класса должен обладать следующими атрибутами:
# self.name - имя, self.number_of_floors - кол-во этажей
# Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
# Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".
# Пункты задачи:
# 1.Создайте класс House.
# 2.Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
# 3.Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
# 4.Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
# 5.Создайте объект класса House с произвольным названием и количеством этажей.
# 6.Вызовите метод go_to у этого объекта с произвольным числом.
#
# Примечания:
# 1.self - это переменная указывающая на объект. Используйте её для обращения к атрибутам или методам объекта.
# 2.Обращение к атрибутам или методам объекта/класса происходит при помощи "."
# 3.Метод __init__ вызывается в момент создания объекта.


# Задача 5_3 "История строительства":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
#
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
#
# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
#
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
#
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.

class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        if args:
            cls.houses_history.append(args)
            return instance

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor ):
        if 1 <= new_floor <= self.number_of_floor:
            for f in range(1, self.number_of_floor+1):
                print(f)

        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floor


    def __str__(self):
        return f"Название: {self.name}, кол-во этажей {self.number_of_floor}"

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floor == other.number_of_floor
        return False

    def __add__(self, value):
        if isinstance(value, int):
            return self.number_of_floor + value
        return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)


    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor < other.number_of_floor
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor > other.number_of_floor
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floor != other.number_of_floor
        return False

# name = input("Введите название дома: ")
# number_of_floors = int(input("Введите количество этажей в доме: "))
# house = House(name, number_of_floors)
# new_floor = int(input(f"Введите номер этажа: "))
# house.go_to(new_floor)

# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)
# h2.go_to(10)



#Блок_2.
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".
#
# Необходимо дополнить класс House следующими специальными методами:
# 1.__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# 2.__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи


# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# # __str__
# print(h1)
# print(h2)
#
# # __len__
# print(len(h1))
# print(len(h2))



#Блок_3.
#
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".
#
# Необходимо дополнить класс House следующими специальными методами:
# __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
# __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
# Остальные методы арифметических операторов, где self - x, other - y:
#
# Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
# Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
# isinstance(other, int) - other указывает на объект типа int.
# isinstance(other, House) - other указывает на объект типа House.

# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# print(h1)
# print(h2)
#
# print(h1 == h2) # __eq__
#
# h1 = h1 + 10 # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10 # __iadd__
# print(h1)
#
# h2 = 10 + h2 # __radd__
# print(h2)
#
# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)