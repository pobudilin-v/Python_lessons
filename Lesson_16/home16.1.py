class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __ne__(self, other):
        return self.get_square() != other.get_square()

    def __lt__(self, other):
        return self.get_square() < other.get_square()

    def __le__(self, other):
        return self.get_square() <= other.get_square()

    def __gt__(self, other):
        return self.get_square() > other.get_square()

    def __ge__(self, other):
        return self.get_square() >= other.get_square()

    def __add__(self, other):
        square = self.get_square() + other.get_square()
        return Rectangle(1, square)

    def __mul__(self, number):
        square_number = self.get_square() * number
        return Rectangle(1, square_number)

    def __str__(self):
        return f"Rectangle: width = {self.width}, height = {self.height}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
# print(r1)
# print(r2)
# print(r3)
# print(r4)