import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius

# Create an instance of Circle with radius 4
circ = Circle(4)

# Print the area and circumference of the circle
print(circ.area())  
print(circ.circumference())  