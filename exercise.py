#classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

# Create an instance of the Person class
person = Person("Alice", 25)

# Use the introduce method
print(person.introduce())  


#inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self, subject):
        return f"{self.name} is studying {subject}."

# Create an instance of the Student class
student = Student("Bob", 20, "S12345")

# Use methods from both Person and Student classes
print(student.introduce())  # My name is Bob and I am 20 years old.
print(student.study("Math"))  # Bob is studying Math.

#Use of super() function
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

# Create an instance of the Rectangle class
rect = Rectangle(5, 4)

# Access properties
print(rect.area)  # 20
print(rect.perimeter)  # 18


#encapsulation
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def _deduct_fee(self, fee):
        self._balance -= fee

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount, fee=0):
        if self._balance >= amount + fee:
            self._balance -= (amount + fee)
            if fee > 0:
                self._deduct_fee(fee)
        else:
            print("Insufficient funds.")

# Create an instance of BankAccount
account = BankAccount(1000)

# Access and use private method (not recommended)
account._deduct_fee(10)

# Use public methods
account.withdraw(200, 5)
print(account._balance)  # 795 (Not recommended to access directly)


#polymorphism
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

circle = Circle(5)
square = Square(4)

print(circle.area())  # 78.53750000000001
print(square.area())  # 16




#using static methods 
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def multiply(cls, x, y):
        return x * y

result1 = MathUtils.add(3, 4)  # Static method
result2 = MathUtils.multiply(3, 4)  # Class method

print(result1)  # 7
print(result2)  # 12



#method overloading
class Calculator:
    def add(self, x, y, z=0):
        return x + y + z

calc = Calculator()

print(calc.add(2, 3))     # 5
print(calc.add(2, 3, 4))  # 9

#using ccomposition in python
class Engine:
    def start(self):
        return "Engine started."

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return f"Car started. {self.engine.start()}"

car = Car()
print(car.start())  # Car started. Engine started.


#using multiple inheritance
class A:
    def method_a(self):
        return "Method A"

class B:
    def method_b(self):
        return "Method B"

class C(A, B):
    pass

obj = C()
print(obj.method_a())  # Method A
print(obj.method_b())  # Method B



#creating a singleton class
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = 0
        return cls._instance

singleton1 = Singleton()
singleton1.value = 10

singleton2 = Singleton()

print(singleton1.value)  # 10
print(singleton2.value)  # 10 (same instance)

