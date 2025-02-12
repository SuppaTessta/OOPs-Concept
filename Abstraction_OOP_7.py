"""
ABSTRACT - is all about providing the important details. Hide the unnecessary details.
            Example - we hide the inner working of a car and only show the end consumer how to use/drive the car.
Uses in real World - <> Easy for the customers.
                        <> Protect/avoid internal information to be leaked.

ABSTRACTION - is used to hide irrelevant details from the user and show the details that are relevant to the users.
              Abstraction is used to hide the internal functionality of the function from the users.
              The users only interact with the basic implementation of the function, but inner working is hidden.
              User is familiar with that "what function does" but they don't know "how it does."

Importance - It is used to reduce complexity and increase efficiency of the program.

Abstract Class : -->An Abstract class can contain both normal and abstract method.
                  -->An Abstract class should have atleast one abstract method.
                      [Abstract method - declared method that should not have any implementation details.
                         It is there just to provide a signal what this method going to do but is not implemented.]
                   -->An Abstract class cannot be instantiated[creating an instance of a class,which is called object];
                       we cannot create objects for the abstract class.

ABSTRACT Methods are created so that Child_Class of Abstract_Class can implement the methods.

Implementation of ABSTRACTION in Python - by using @abstractmethod decorator and "ABC" class of "abc" module.
                                          We create the Abstract_class to be the child class of "ABC" class.
                                    And we implement the abstract method of the same by using @abstractmethod decorator.
"""

# "abc" is a module which contains several in-built classes.
# We import "ABC" class and "abstractmethod" decorator from "abc" module.
from abc import ABC, abstractmethod

# Create an Abstract Class
class Animal(ABC):  # "Animal" is an abstract class.
    @abstractmethod   # "abstractmethod" is a decorator to indicate that this method is an abstract method.
    def eat(self):   # "eat" is an abstract method.
        pass

# a = Animal()  --> Throws error when we try to create an object of the abstract class.

# Create a child class of "Animal" class
class Dog(Animal):  #"Dog" is a child of "Animal" abstract_class. So its will also inherit the abstract method "eat".
    def sleep(self):
        print("Dog is sleeping")

# d = Dog()
# Can't instantiate "Dog", since it inherits the abstract method "eat" but does not implements it.

# To create object of the child class, we need to implement the abstract method "eat".
class Dog(Animal):

    def sleep(self):
        print("Dog is sleeping")

    # Implementing abstract_method "eat" of parent class "Animal".
    def eat(self):  #Method Overriding - happens when both parent and child class have same method(here 'eat').
                    # And we override parent method with child method.
        print("Dog is eating")


obj = Dog()
obj.eat()
obj.sleep()

