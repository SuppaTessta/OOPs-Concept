'''
There are three types of access modifiers in Python:
Public - Accessible from anywhere.
Private - Accessible only within the class.
Protected - Accessible only within the class and its subclasses.

By Default Python classes and methods are PUBLIC.
To make them PRIVATE we use "__" before the variable name.
And to make them PROTECTED we use "_" before the variable name.

BUT you can access private methods by using the format - "(object_name)._(class_name)__(private_method_name())"
Example - print(Cal._Calculator__add(10,20)) where __add is the private method.

The name scrambling is used to ensure that subclasses don't accidentally override the private methods and attributes of
their superclasses.
It's not designed to prevent deliberate access from outside.
'''

class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary # Salary is a private variable which is made by adding "__" before it.

    def findAge(self):
        return self.age
    def getSalary(self): # This is a public method.
        print(self.__salary)
        # Although "__salary" is a private variable, since it is called within the class, it will provide output.
        self.__Tax() # This is being executed inside class so provides output.
    def __Tax(self): # This is a private method.
        return "Tax"


per = Person("John", 36,50000)
print(per.name) # Because by default name attribute is public.
print(per.findAge()) # Because by default findAge() method is public.

# print(per.__salary)
# Throws error because salary is a private variable and is being read outside the class.
per.getSalary() # Since private method is defined within class, it will provide output.
# But here it provides output of __Tax() private method since it is called inside the class "Person" in the public method "getSalary()".

# per.__Tax()
# Throws error because compiler can't read private method from outside the class.

# To access private methods, we use the format - "(object_name)._(class_name)__(private_method_name())" to call the private method/attribute.
# Example-
print(per._Person__salary)
print(per._Person__Tax())

