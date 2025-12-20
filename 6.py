#1
class Sedan:
    def init(self, brand):
        self.brand = brand
    
    def accept(self, visitor):
        visitor.visit_sedan(self)


class SUV:
    def init(self, brand):
        self.brand = brand
    
    def accept(self, visitor):
        visitor.visit_suv(self)


class Truck:
    def init(self, brand):
        self.brand = brand
    
    def accept(self, visitor):
        visitor.visit_truck(self)


class CarWash:
    def visit_sedan(self, sedan):
        print(f"Мойка {sedan.brand}: 500 руб")
    
    def visit_suv(self, suv):
        print(f"Мойка {suv.brand}: 700 руб")
    
    def visit_truck(self, truck):
        print(f"Мойка {truck.brand}: 1200 руб")


class Repair:
    def visit_sedan(self, sedan):
        print(f"Ремонт {sedan.brand}: 5000 руб")
    
    def visit_suv(self, suv):
        print(f"Ремонт {suv.brand}: 8000 руб")
    
    def visit_truck(self, truck):
        print(f"Ремонт {truck.brand}: 15000 руб")


cars = [Sedan("Toyota"), SUV("Lexus"), Truck("Volvo")]

print("Мойка:")
wash = CarWash()
for car in cars:
    car.accept(wash)

print("\nРемонт:")
repair = Repair()
for car in cars:
    car.accept(repair)










#2
from abc import ABC, abstractmethod

class Subject(ABC):
    def init(self):
        self._observers = []
    
    def subscribe(self, observer):
        self._observers.append(observer)
        print(f"{observer.name} подписался")
    
    def unsubscribe(self, observer):
        self._observers.remove(observer)
        print(f"{observer.name} отписался")
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer(ABC):
    def init(self, name):
        self.name = name
    
    @abstractmethod
    def update(self, message):
        pass


class CarDealer(Subject):
    def init(self, name):
        super().init()
        self.dealer_name = name
    
    def new_car(self, car, price):
        message = f"{self.dealer_name}: {car} за {price} руб"
        print(f"\n{message}")
        self.notify(message)


class EmailClient(Observer):
    def update(self, message):
        print(f"{self.name} получил email: {message}")


class SMSClient(Observer):
    def update(self, message):
        print(f"{self.name} получил SMS: {message}")


class AppClient(Observer):
    def update(self, message):
        print(f"{self.name} получил push: {message}")


class VIPClient(Observer):
    def init(self, name, discount):
        super().init(name)
        self.discount = discount
    
    def update(self, message):
        print(f"VIP {self.name} получил уведомление со скидкой {self.discount}%: {message}")


dealer = CarDealer("Автосалон Премиум")

client1 = EmailClient("Иван")
client2 = SMSClient("Мария")
client3 = AppClient("Алексей")
client4 = VIPClient("Дмитрий", 15)

dealer.subscribe(client1)
dealer.subscribe(client2)
dealer.subscribe(client3)
dealer.subscribe(client4)

dealer.new_car("Toyota Camry", 3500000)
dealer.new_car("Lexus RX", 6000000)

dealer.unsubscribe(client2)

dealer.new_car("BMW X5", 7500000)

