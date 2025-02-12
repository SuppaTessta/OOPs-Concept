# instance/object method     ---  First parameter should always be "self"
# "self" represent the object that is going to get created.
class Person:

    country = "India" # Class variable/property

    # Below "greet" method is a class method.
    @classmethod # Decorator to indicate that this method is a class method.
    # Decorator is like annotations(meta data). It is used to tell the python compiler additional information.
    def greet(cls):
        print("Hello from the class method", cls.country)
    # The above class method wil have access to the class variables/properties.
    # But it will not have access to the object properties.


    # Below "hello" method is a static method.
    # It is used to keep the function isolated from outside influence.
    @staticmethod
    def hello():
        print("Hello from the static method.")
    # Static method is totally independent.
    # Neither it has access to class properties/variables nor it has access to instance properties/variables.

    def __init__(self, name, age): # Here we use additional parameter with "self".
        self.name = name
        self.age = age

    # below method is an instance method and "self" is mandatory.
    # instance method can only be called by the object.
    def findAge(self): # Here we use "self" as the only parameter.
        return self.age

per = Person("John", 32)
print(per.findAge()) # Calling the instance method

Person.greet() # Calling the class method directly without object
per.greet() # Calling the class method through object.

Person.hello() # Calling the static method directly without object.
per.hello() # Calling the static method through object.


''' Method Overloading - A class with two or more methods with same name but different parameters.
Method Overloading is further divided into two parts - EXPLICIT and IMPLICIT.

Explicit Method Overriding - is defining two or more functions with same name but variable number of parameters.
     Example - def sum(a,b) 
               def sum(a,b,c) 
               def sum(a,b,c,d) 
##Python does not support method overloading.##
BECAUSE IN PYTHON - WHEN WE DEFINE MULTIPLE METHODS WITH THE SAME NAME IN A CLASS, THE LAST DEFINED METHOD IS ALWAYS USED.

Since Python does not support method overloading, it is not possible to define multiple methods with same name in a class.

Thus to bypass that we use something called IMPLICIT Method Overloading.
Here instead of creating two or more methods with same name in a class, we can create one method and declare default values for the optional parameters.
'''
# Example of Explicit Method Overloading
class Calculator:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c):
        return a + b + c
cal = Calculator()
#print(cal.add(10, 20)) # Throughs error since last defined method is used and it has 3 parameters so our code needs 3 arguments.

# Example of Implicit Method Overloading
class Calculator:
    # Using Default values for Optional Parameters.
    # Which can be overridden by giving required arguments in the function call.
    def add(self, a, b, c=0, d=0):
        return a + b + c + d
cal = Calculator()
print(cal.add(10, 20)) # Takes default values while compiling.
print(cal.add(10, 20, 30, 40)) # Override the default values when necessary arguments are passed.


