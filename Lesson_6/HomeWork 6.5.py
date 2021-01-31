# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш),  (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title='Что-то что может рисовать'):
        self.title = title

    def draw(self):
        print(f'Начни рисовать! {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Начни рисовать, {self.title} ручкой!')


class Pencil(Stationery):
    def draw(self):
        print(f'Начни рисовать, {self.title} карандашом!')


class Handle(Stationery):
    def draw(self):
        print(f'Начни рисовать, {self.title} маркером!')


start = Stationery()
start.draw()
pen = Pen('Parker')
pen.draw()
pencil = Pencil("Faber-Castell")
pencil.draw()
handle = Handle("COPIC")
handle.draw()

