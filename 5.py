#1
class Car:
    def __init__(self, brand, model, engine, color):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.color = color

    def clone(self):
        return Car(self.brand, self.model, self.engine, self.color)

    def clone_with(self, **kwargs):
        return Car(
            kwargs.get('brand', self.brand),            kwargs.get('model', self.model),            kwargs.get('engine', self.engine),            kwargs.get('color', self.color),        )



    def __str__(self):
        return f"{self.brand} {self.model} ({self.engine}, {self.color})"bmw_prototype = Car("BMW", "X5", "3.0 V6", "Черный")
print("Прототип:", bmw_prototype)

bmw_sport = bmw_prototype.clone()
bmw_sport.model = "M5"bmw_sport.engine = "4.4 V8"bmw_sport.color = "Красный"print("Клон:", bmw_sport)
print("Оригинал:", bmw_prototype)

class Car:
    def __init__(self, brand, model, engine, color):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.color = color

    def clone(self):
        return Car(self.brand, self.model, self.engine, self.color)

    def clone_with(self, **kwargs):
        return Car(
            kwargs.get('brand', self.brand),            kwargs.get('model', self.model),            kwargs.get('engine', self.engine),            kwargs.get('color', self.color),        )



    def __str__(self):
        return f"{self.brand} {self.model} ({self.engine}, {self.color})"bmw_prototype = Car("BMW", "X5", "3.0 V6", "Черный")
print("Прототип:", bmw_prototype)

bmw_sport = bmw_prototype.clone()












#2
class Car:
    def __init__(self):
        self.brand = None        self.engine = None        self.seats = None        self.color = None    def __str__(self):
        return f"Машина: {self.brand}, двигатель {self.engine}, {self.seats} мест, цвет {self.color}"class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_brand(self, brand):
        self.car.brand = brand
        return self    def set_engine(self, engine):
        self.car.engine = engine
        return self    def set_seats(self, seats):
        self.car.seats = seats
        return self    def set_color(self, color):
        self.car.color = color
        return self    def build(self):
        tmp = self.car
        self.car = Car()
        return tmp


builder = CarBuilder()

sports_car = (builder
              .set_brand("Ferrari")
              .set_engine("V12")
              .set_seats(2)
              .set_color("Красный")
              .build())

family_car = (builder
              .set_brand("Toyota")

              .set_seats(7)
              .set_color("Синий")
              .build())

print(sports_car)
print(family_car)
bmw_sport.model = "M5"bmw_sport.engine = "4.4 V8"bmw_sport.color = "Красный"print("Клон:", bmw_sport)
print("Оригинал:", bmw_prototype)
