"""
Unlike Parent-Child relationship, which is checked using 'isA' test,

RELATIONSHIP OF ASSOCIATION is checked using 'hasA' test between two objects.
In this kind of relationship, two objects can exist independently without any relationship between them, but they are
related in someway.

The kind of relationship in which one has someone/something, is called "AGGREGATION"/"Loose Coupling".
It is a uni-directional relationship.
Example -> PERSON hasA CAR
Example -> PERSON hasA COUNTRY

"COMPOSITION"/"Tight/Closed Coupling" - in this relationship, existing of one object will depend on the existence of
                                        another object. It is a both way relationship.
Example -> Human_body hasA Heart - two objects are inter-dependent for existence.
"""

# AGGREGATION - hasA relationship

class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

class Person:
    def __init__(self,name,car):  # Initializer of "Person" class hasA "car" object parameter
        self.name = name
        self.car = car


car = Car("BMW","Black")
person = Person("John",car)  # "person" object hasA "car" object
# Here "car" object is associated/aggregated with "person" object during creation.
print(person.name, person.car.brand, person.car.color)
# Syntax to call attribute/methods of an object: main_object.sub_object.attribute/method
# One can use the "." operator to increase the number of sub_object until the desired attribute/method is reached.


# COMPOSITION - here one object is created inside another object and not passed like in aggregation.
class Engine:
    def engineDetails(self):
        print("Car engine is model E1213")

class Tyres:
    def tyreDetails(self):
        print("Car tyres is Apollo")

class Doors:
    def doorDetails(self):
        print("Doors of the car is Automatic")

class Car:
    def __init__(self):  # We will create the objects inside the initializer of "Car" class.
        self.engine = Engine()  # Object of "Engine" class
        self.tyres = Tyres()    # Object of "Tyres" class
        self.doors = Doors()    # Object of "Doors" class
        # Their existence is only possible if the "Car" object is there since they are created inside the "Car" class.

    def printDetails(self):  # This method will print the details of the car
        self.engine.engineDetails()
        self.tyres.tyreDetails()
        self.doors.doorDetails()


c = Car()  # car object is created.
# "Car" object hasA "Engine" object, "Car" object hasA "Tyres" object, "Car" object hasA "Doors" object which are created inside.
c.printDetails()
# Without "car" object there is no existence of "Engine", "Tyres" and "Doors" and vice versa.
# This is called "COMPOSITION"/"Tight/Closed Coupling".
