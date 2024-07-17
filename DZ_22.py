# Задание 1
# Создать базовый класс Фигура с методом для подсчета площади. Создать производные классы: прямоугольник, круг, прямоугольный треугольник,
# трапеция со своими методами для подсчета площади.
import abc


class Figure(abc.ABC):
    @abc.abstractmethod
    def square(self):
        pass


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def square(self):
        return self.a * self.b


class Circle(Figure):
    def __init__(self, r):
        self.r = int(r)

    def square(self):
        return 3.14 * self.r ** 2


class Right_angled_triangle(Figure):
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def square(self):
        return self.a * self.b / 2


class Trapezoid(Figure):
    def __init__(self, a, b, h):
        self.a = int(a)
        self.b = int(b)
        self.h = int(h)

    def square(self):
        return (self.a + self.b) * (self.h ** 2)


# Задание 2
# Для классов из задания 1 нужно переопределить магические методы int(возвращает площадь) и str(возвращает информацию о фигуре).


class Rectangle_square(Rectangle):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.sq = Rectangle.square(self)

    def __str__(self):
        return f'Прямоугольник площадью - {self.sq}'


class Circle_square(Circle):
    def __init__(self, r):
        super().__init__(r)
        self.sq = Circle.square(self)

    def __str__(self):
        return f'Круг площадью - {self.sq}'


class Right_angled_triangle_square(Right_angled_triangle):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.sq = Right_angled_triangle.square(self)

    def __str__(self):
        return f'Прямоугольный треугольник площадью - {self.sq}'


class Trapezoid_square(Trapezoid):
    def __init__(self, a, b, h):
        super().__init__(a, b, h)
        self.sq = Trapezoid.square(self)

    def __str__(self):
        return f'Трапеция площадью - {self.sq}'


rec = Rectangle_square(4, 5)
print(rec)

# Задание 3
# Создайте базовый класс Shape для рисования плоских фигур.
# Определите методы:
# ■ Show() — вывод на экран информации о фигуре;
# ■ Save() — сохранение фигуры в файл;
# ■ Load() — считывание фигуры из файла.
# Определите производные классы:
# ■ Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
# ■ Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
# ■ Circle — окружность с заданными координатами центра и радиусом;
# ■ Ellipse — эллипс с заданными координатами верхнего угла описанного вокруг него прямоугольника со сторонами, параллельными осям
# координат, и размерами этого прямоугольника.
# Создайте список фигур, сохраните фигуры в файл, загрузите в другой список и отобразите информацию о каждой из фигур.
import json


class Shape(abc.ABC):
    @abc.abstractmethod
    def show(self):
        pass

    def save(self):
        with open('shape.txt', mode='w', encoding='utf-8') as file:
            file.write(json.dumps(self.show(), indent=4, ensure_ascii=False))

    def load(self):
        try:
            with open('shape.txt', mode='r', encoding='utf-8') as file:
                shape = json.loads(file.read())
            return shape
        except FileNotFoundError:
            return []


class Square(Shape):
    def __init__(self, x_sq, y_sq, a_sq):
        self.x_square = int(x_sq)
        self.y_square = int(y_sq)
        self.a_square = int(a_sq)

    def show(self):
        return f'Квадрат с координатами верхнего левого угла ({self.x_square},{self.y_square}) и длиной стороны {self.a_square}'


class Rectangle(Shape):
    def __init__(self, x_rect, y_rect, a_rect, b_rect):
        self.x_rect = int(x_rect)
        self.y_rect = int(y_rect)
        self.a_rect = int(a_rect)
        self.b_rect = int(b_rect)

    def show(self):
        return f'Прямоугольник с координатами верхнего левого угла ({self.x_rect},{self.y_rect}) и сторонами {self.a_rect} и {self.b_rect}'


class Circle(Shape):
    def __init__(self, x_circ, y_circ, r_circ):
        self.x_circ = int(x_circ)
        self.y_circ = int(y_circ)
        self.r_circ = int(r_circ)

    def show(self):
        return f'Окружность с координатами центра ({self.x_circ},{self.y_circ}) и радиусом {self.r_circ}'


class Ellipse(Shape):
    def __init__(self, x_ell, y_ell, a_ell, b_ell):
        self.x_ell = int(x_ell)
        self.y_ell = int(y_ell)
        self.a_ell = int(a_ell)
        self.b_ell = int(b_ell)

    def show(self):
        return f'Эллипс с координатами верхнего угла описанного вокруг него прямоугольника  ({self.x_ell},{self.y_ell}) и сторонами этого прямоугольника {self.a_ell} и {self.b_ell}'


sq = Square(1, 5, 4)
sq.save()
print(sq.load())