# Shape area calculator with inheritance

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    """Represents a rectangle shape with width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    """Represents a circle shape with a given radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi* (self.radius ** 2)
    
print("Rectangle docstring:", Rectangle.__doc__)
print("Circle docstring:", Circle.__doc__)

shapes = [
    Rectangle(4, 5),
    Circle(3),
    Rectangle(2, 6),
    Circle(1.5),
    Rectangle(7, 3)
]

rectangles = 0
circles = 0

for shape in shapes:
    if isinstance(shape, Rectangle):
        rectangles += 1
    elif isinstance(shape, Circle):
        circles += 1

print(f"Total Rectangles: {rectangles}\nTotal Circles: {circles}")



# Bank account with encapsulation

class BankAccount:
    def __init__(self):
        self.__balance = 0 # Private attribute

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

account = BankAccount()

account.deposit(100)
print("Balance after deposit:", account.balance)

account.withdraw(40)
print("Balance after withdrawal:", account.balance)



# Notification system with polymorphism

class EmailNotification:
    def send(self, message):
        print(f"Email sent with message: {message}")

class SMSNotification:
    def send(self, message):
        print(f"SMS sent with mesage: {message}")

def send_bulk(notifiers, message):
    for notifier in notifiers:
        notifier.send(message)

email = EmailNotification()
sms = SMSNotification()

notifier_list = [email, sms, email, email, sms]
send_bulk(notifier_list, "Your order has been shipped!")