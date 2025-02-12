'''
Any object that is defined has two things -
            1. Data(State or Properties)
            2. Methods(Behaviour or Actions)

ENCAPSULATION - is to bind the data/state of the object with the methods/behaviour of the object.
                It is done to hide or make the data/state of the object private.

Properties of Encapsulation:
    1. All the fields/properties of the object should be private.
    2. Getters and Setters methods/behaviour of the object should be public.
'''

# Encapsulation - Example

class Person:
    def __init__(self,name,car):
        self.__name = name   # Private property
        self.__car = car     # Private property

# Now we define Getters and Setters to access the private properties from outside the class.
# Getters and Setters - public methods to allow controlled interactions(i.e. controlled access to the private properties).
# The Getters and Setters are used to get and set the values of the private variables respectively.
    def getName(self):   # Getters method
        return self.__name
    def setName(self,name):   # Setters method
        self.__name = name
    def getCar(self):    # Getters method
        return self.__car
    def setCar(self,car):    # Setters method
        self.__car = car

per = Person("John", "BMW")
print(per.getName())
per.setName("Jane")
print(per.getName())

print(per.getCar())
per.setCar("Mercedes")
print(per.getCar())

'''
In encapsulation, all fields are made private. 
And to access/modify them we can use methods(Getters and Setters) which are made public.
This is done to ensure that to change any properties, we need to first call the methods.
And we can write logic to control them, to put proper checks and balances in those methods.
This prevents anyone to do anything without proper permission.
'''

