# pylint: disable=too-few-public-methods missing-module-docstring

class Shape:
    """Base shape with color and name."""

    def __init__(self, color, name):
        self.color = color
        self.name = name.capitalize()
        return

    def say_name(self):

        return f"My name is {self.name}."


class Rectangle(Shape):
    """Rectangle shape with width and height."""

    def __init__(self, color, name, width, height):
        super().__init__(color, name)
        self.width = width
        self.height = height

    def say_name(self):
        return f"My name is {self.name} and I am a rectangle."

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Circle shape with a radius."""

    def __init__(self, color, name, radius):
        super().__init__(color, name)
        self.radius = radius

    def say_name(self):
        return f"My name is {self.name} and I am a circle."

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
