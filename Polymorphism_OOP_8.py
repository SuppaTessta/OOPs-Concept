"""
POLYMORPHISM - comes from the words "poly - meaning - many/multiple" and "morphs - meaning - many forms".
In Python programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

Polymorphism has the following advantages:
        1.It is beneficial to reuse the codes.
         2.The codes are simple to debug.
          3.A single variable can store multiple data types.



"""
# Polymorphism

# 1.Polymorphism - Using Inheritance and Method Overriding.
class Animal:   # Parent class
    def eat(self):
        print("Animal is eating")

class Dog(Animal):  # Child class
    def eat(self):   # Method Overriding
        print("Dog is eating")

class Cat(Animal):
    def eat(self):     # Method Overriding
        print("Cat is eating")


c = Cat()
d = Dog()
a = Animal()

c.eat()  # Case 1
d.eat()  # Case 2
a.eat()  # Case 3
"""
In the above 3 cases, although we call the same method "eat" in the same way, but depending on the context of the object,
the method will be executed differently and outputs will be different.
--> This is Polymorphism in action. Although the same method is called but depending on which object it is called by,
    the method will be executed differently.
"""
# 2.Polymorphism - Duck Typing Concept - using Interface.
#    Duck typing - is a programming concept where the type or the class of an object is less important than the methods it defines.
#    When you use duck typing, you do not check types at all. Instead, you check for the presence of a given method or attribute.
class BirdFly:
    def flyBird(self, bird):   # "bird" is a parameter of the method
        bird.fly()    # "bird" parameter should know what to do. That is every bird object should have a method "fly".
        # This is done by creating a "bird" object.

class Parrot:
    def fly(self):          # Method "fly" is defined in Parrot class
        print("Parrot is flying")

class Crow:
    def fly(self):          # Method "fly" is defined in Crow class
        print("Crow is flying")


p = Parrot() # Parrot object(which represent "bird" object according this example)
c = Crow()   # Crow object(which represent "bird" object according this example)
bf = BirdFly()   # BirdFly object

bf.flyBird(p)  # Parrot object is passed as an object(in place of "bird") to BirdFly object
bf.flyBird(c)  # Crow object is passed as an object(in place of "bird") to BirdFly object

# Thus FlyBird method will be executed differently depending on the object passed.
# --> This is Polymorphism in action.
'''
If any "fly" method would have been missing in any bird object, ie. if bird object did not have a fly method,
then Python would have thrown an error when called through the BirdFly object.
In duck typing, the method should be same as class type is not checked.
'''