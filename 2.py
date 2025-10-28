from abc import ABC, abstractmethod
import random

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Figure):
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return 3.14 * self.r * self.r
    
    def perimeter(self):
        return 2 * 3.14 * self.r

class Square(Figure):
    def __init__(self, a):
        self.a = a
    
    def area(self):
        return self.a * self.a
    
    def perimeter(self):
        return 4 * self.a

class Triangle(Figure):
    def __init__(self, a):
        self.a = a
    
    def area(self):
        return 0.43 * self.a * self.a
    
    def perimeter(self):
        return 3 * self.a
      
figures = []
for i in range(5):
    num = random.randint(1, 3)
    size = random.randint(1, 8)
    
    if num == 1:
        figures.append(Circle(size))
    elif num == 2:
        figures.append(Square(size))
    else:
        figures.append(Triangle(size))

for i in range(len(figures)):
    fig = figures[i]
    s = fig.area()
    p = fig.perimeter()
    
    if isinstance(fig, Circle):
        print(f"Фигура {i+1} - Круг (радиус={fig.r}): площадь = {s:.2f}, периметр = {p:.2f}")
    elif isinstance(fig, Square):
        print(f"Фигура {i+1} - Квадрат (сторона={fig.a}): площадь = {s:.2f}, периметр = {p:.2f}")
    elif isinstance(fig, Triangle):
        print(f"Фигура {i+1} - Треугольник (сторона={fig.a}): площадь = {s:.2f}, периметр = {p:.2f}")




#Переделанный вариант с полиморфизмом в функции

from abc import ABC, abstractmethod
import random

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Figure):
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return 3.14 * self.r * self.r
    
    def perimeter(self):
        return 2 * 3.14 * self.r

class Square(Figure):
    def __init__(self, a):
        self.a = a
    
    def area(self):
        return self.a * self.a
    
    def perimeter(self):
        return 4 * self.a

class Triangle(Figure):
    def __init__(self, a):
        self.a = a
    
    def area(self):
        return 0.43 * self.a * self.a
    
    def perimeter(self):
        return 3 * self.a

def calculate_and_print(figure):
    
    area = figure.area()        
    perimeter = figure.perimeter()  
    
    if isinstance(figure, Circle):
        print(f"Круг (радиус={figure.r}): площадь = {area:.2f}, периметр = {perimeter:.2f}")
    elif isinstance(figure, Square):
        print(f"Квадрат (сторона={figure.a}): площадь = {area:.2f}, периметр = {perimeter:.2f}")
    elif isinstance(figure, Triangle):
        print(f"Треугольник (сторона={figure.a}): площадь = {area:.2f}, периметр = {perimeter:.2f}")

figures = []
for i in range(5):
    num = random.randint(1, 3)
    size = random.randint(1, 8)
    
    if num == 1:
        figures.append(Circle(size))
    elif num == 2:
        figures.append(Square(size))
    else:
        figures.append(Triangle(size))

print("Результаты с полиморфной функцией:")
for i, fig in enumerate(figures):
    print(f"Фигура {i+1} - ", end="")
    calculate_and_print(fig) 



