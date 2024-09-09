class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    radius = 0

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22 / 7) * self.radius * self.radius

def print_shape_area(shape):
    #polymorphism : shape can be an instance of any subclass of shape
    print(f"the area of {shape.__class__.__name__} is {shape.area()}")

if __name__ == "__main__":
    gola = Circle(4)
    sq = Rectangle(4, 4)
    print_shape_area(gola)
