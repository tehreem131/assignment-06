# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        return(f'Name: {self.name}, Marks: {self.marks}')

student1:student = student("Tehreem",88)
student2:student = student("Dua",86)
print("student 1 Details:",student1.display())
print(student1.name,student1.marks)
print("student 2 Details:",student2.display())

# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class counter:
    count = 0

    def __init__(self):
        counter.count += 1

        @classmethod
        def display_count(cls):
            return f'Total objects created: {cls.count}'
        
# obj1 : counter = counter()
# obj2 : counter = counter()
# obj3 : counter = counter()
# print(counter.display_count()) #type ignore

# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class car:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        return f'{self.brand} is starting'
    
car:car = car("Toyata") # type: ignore
print(car.brand)
print(car.start())

# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name

b1: Bank = Bank()
print(b1.bank_name)
b2:Bank = Bank()
print(b2.bank_name)
Bank.change_bank_name("xyz Bank")
print(b1.bank_name)
print(b2.bank_name)

# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.


class Mathutils:
    @staticmethod
    def add(a,b):
        return a + b
    
print(Mathutils.add(5,10))

# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger object created.")

    # def __del__(self):
    #     print("Logger object destroyed.")

log:Logger = Logger()
del log

# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self,name,salary,ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp1 : Employee = Employee("Tehreem",50000,"123-45-67899")
print(emp1.name)
print(emp1._salary)
# print(emp1.__ssn)
print(emp1._Employee__ssn)


# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self,name):
        self.name = name
class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject

teacher: Teacher = Teacher("Tehreem","English")
print(f'Name: {teacher.name}, subject: {teacher.subject}')

# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

# from abc import ABC, abstractmethod
# from turtle import width

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self,height,widht):
#         self.height = height
#         self.width = width

# def area(self):
#     return self.height * self.width

# rect1: Rectangle = Rectangle(5.8,10.6)
# print(f'Area of Rectangle: {rect1.area()}')

# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self,name,bread):
        self.name = name
        self.bread = bread
    def bark(self):
        print(f'{self.name} says wooofff!')

dog :Dog = Dog("Tommy","Labrador")
print(dog.bark())

# Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    # Class variable to keep track of total books
    total_books = 0

    def __init__(self, title):
        self.title = title
        # Increment book count when a new book is created
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Example usage
book1 = Book("Python Basics")
book2 = Book("Data Structures")
book3 = Book("Machine Learning")

print("Total number of books:", Book.total_books)

# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example usage
celsius_temp = 25
fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)

print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")


# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Engine object inside Car

    def start_car(self):
        return self.engine.start()  # Accessing Engine method via Car

# Example usage
my_engine = Engine()
my_car = Car(my_engine)

print(my_car.start_car())

# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.
class Employee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return f"Employee Name: {self.name}"

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: reference to existing Employee object

    def show_department_details(self):
        return f"Department: {self.department_name}, {self.employee.get_details()}"

# Example usage
emp1 = Employee("Alice")
dept1 = Department("HR", emp1)

print(dept1.show_department_details())

# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        return "Show from A"

class B(A):
    def show(self):
        return "Show from B"

class C(A):
    def show(self):
        return "Show from C"

class D(B, C):  # Diamond Inheritance
    pass

# Example usage
d = D()
print(d.show())  # Follows MRO
print(D.__mro__)  # Shows the MRO chain

# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

# Example usage
say_hello()

# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
p = Person("Alice")
print(p.greet())

# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative.")
        else:
            self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage
p = Product(100)
print("Current Price:", p.price)

p.price = 150
print("Updated Price:", p.price)

del p.price

# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Example usage
m = Multiplier(5)

# Check if the object is callable
print("Is m callable?", callable(m))

# Call the object like a function
result = m(10)
print("Result of calling m(10):", result)

# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

# Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older."):
        self.message = message
        super().__init__(self.message)

# Function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Must be 18 or older.")
    else:
        print("Access granted.")

# Example usage with try-except
try:
    check_age(16)
except InvalidAgeError as e:
    print("Exception caught:", e)

# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # The object itself is the iterator

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value

# Example usage
for number in Countdown(5):
    print(number)
