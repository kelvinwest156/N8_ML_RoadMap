class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return self.length*2 + self.width*2

    def is_square(self):
        return self.length == self.width


rectangle1 = Rectangle(length=14, width=14)


print(f"The Area of the rectangle is {rectangle1.area()}")
print(f"The Perimeter of the rectangle is {rectangle1.perimeter()}")

if rectangle1.is_square():
    print("This rectangle is a square")
else:
    print("This rectangle not a square")