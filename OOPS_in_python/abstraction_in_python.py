# What is Abstraction?

# Abstraction isn't supported directly in Python. Calling a magic method, on the other hand, allows for abstraction.

# If an abstract method is declared in a superclass, subclasses that inherit from the superclass must have their own implementation of the method.

# A superclass's abstract method will never be called by its subclasses. But the abstraction aids in the maintenance of a similar structure across all subclasses.

# In our parent class Book, we have defined the __repr__ method. Let's make that method abstract, forcing every subclass to compulsorily have its own __repr__ method.

from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price

    @abstractmethod
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    def __repr__(self):
        return f"Book: {self.title}, Branch: {self.branch}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 655, 'IT')

print(novel1)
print(academic1)
# In the above code, we have inherited the ABC class to create the Book class. We've made the __repr__ method abstract by adding the @abstractmethod decorator.

# While creating the Novel class, we intentionally missed the implementation of the __repr__ method to see what happens.

# Output:

# Traceback (most recent call last):
#   File "C:\Users\ashut\Desktop\Test\hello\test.py", line 40, in <module>
#     novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
# TypeError: Can't instantiate abstract class Novel with abstract method __repr__
# We get a TypeError saying we cannot instantiate object of the Novel class. Let's add the implementation of the __repr__ method and see what happens now.

class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"
# Output:

# Book: Two States, Quantity: 20, Author: Chetan Bhagat, Price: 160.0
# Book: Python Foundations, Branch: IT, Quantity: 12, Author: PSF, Price: 655
# Now it works fine.