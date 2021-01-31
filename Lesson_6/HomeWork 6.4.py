# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    ''' Автомобиль '''

    def __init__(self, name, clor, speed, is_police=False):
        self.name = name
        self.clor = clor
        self.speed = speed
        self.is_police = is_police
        print(f'Новая маштна: {self.name} (Цвет{self.clor}) машина полицейская - {self.is_police}')

    def go(self):
        print(f'{self.name}: Машина поехала.')

    def stop(self):
        print(f'{self.name}: Машина остановилась.')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"НАлево" if direction == 0 else "направо"}.')

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}.'


class TownCar(Car):
    ''' Городской автомобиль '''

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f"{self.name}: Скорость автомобиля {self.speed}"


class WorkCar(Car):
    ''' Грузовой  автомобиль '''

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля {self.speed}"


class SportCar(Car):
    ''' Спортивный автомобиль '''

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 160 else f"{self.name}: Скорость автомобиля {self.speed}"


class PoliceCar(Car):
    ''' Полицейский автомобиль '''

    def __init__(self, name, clor, speed, is_police=True):
        super().__init__(name, clor, speed, is_police)


police_car = PoliceCar("'Полиция'", 'Белый', 88)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = WorkCar("'Грузовичек'", 'зеленый', 38)
work_car.go()
work_car.turn(4)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()

sport_car = SportCar("'Спортивня'", 'Красный', 120)
sport_car.go()
sport_car.turn(4)
print(sport_car.show_speed())
sport_car.turn(0)
sport_car.stop()

town_car = TownCar("'Малолитражка'", 'желтый', 55)
town_car.go()
town_car.turn(1)
print(town_car.show_speed())
town_car.turn(1)
town_car.stop()


