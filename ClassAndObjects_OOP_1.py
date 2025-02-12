class Person: #empty class
    pass #This keyword works as a placeholder for future code.
#Thus preventing execution of the block of code inside class.
# Since a Class should never be empty, we use pass keyword to avoid getting an error

class Person:
    name = "John"
    age = 36
    country = "Norway"

per = Person() #Creating an object

print(per) # only printing the object gives the address of the object
print(per.name)
print(per.age)
print(per.country)

#You can add more attributes to the object but it will be specific to that object.
per.religion = "Hindu"
print(per.religion)

rson = Person() # Creating another object
#print(rson.religion)
# Since religion is specific to "per" object, and not present in "rson" object,it will give error.

# Create a new class named Person, use the __init__() function to assign values to object properties, and to assign values to the data members of the class.
class Person:
    #initializer/constructor for the objects
    def __init__(self, name, age, country): # every constructor should have the __init__ keyword.
        # The self keyword represents the object to be created.
        # We can write anything in place of self. Like name, Karina, gherhg, etc.
        # But we use "self" keyword since it a established convention.
        self.name = name # Here we are trying to -
        self.age = age # initialize the state of an object.
        self.country = country

print()#new line
# Create two objects p1 and p2
p1 = Person("John", 36, "Norway")
print(p1.name)
print(p1.age)
print(p1.country)
print() #new line
p2 = Person("Jane", 32, "USA")
print(p2.name)
print(p2.age)
print(p2.country)

print()
# A class can not Have multiple __init__() functions(methods).
# Incase of multiple __init__(), the last one will be used.
#Example:
class Person:
    def __init__(self, name, age, country): # This will be ignored.
        self.name = name
        self.age = age
    def __init__(self, name): # Last one will be considered in case of multiple __init__()
        self.name = name

#per = Person("John", 36) # Throws an error since only name(and not age) is defined in the last __init__() function.
#print(per.name)

per = Person("John") # This will work since only name is defined in the last __init__() function.
print(per.name)
print()

class Pers:
    def __init__(self, name, age = 99 ,hobby="Cricket" ):
        # if age,hobby is not passed, it will take the default value
        # Thus making them optional while creating object.
        self.name = name
        self.age = age
        self.hobby = hobby
#Thus we can effictively write all three.
per1 = Pers("John")
per2 = Pers("Jane", 32)
per3 = Pers("Jane", 32, "Football")

# Difference between Class and Instance property.
class Person0:
    country = "India" # Class property/attribute and it has to be initialized in the class. It remains same for all objects.
    def __init__(self, name):
        self.name = name # Instance property/attribute and it keep changing for all objects according to the arguments passed in the __init__() function.

per0 = Person0("John")
per1 = Person0("Jane")
print(per0.name, per1.name)
print(per0.country, per1.country)
print()
# To call class level property, we can directly use the class_name.property_name
# No need to create object.
print(Person0.country) #Example

