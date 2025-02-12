'''
INHERITANCE - OOPs concept inspired from real world concept of hierarchical relationship[Parent-Child] and inheritance.
It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving
a class from another class.

Inheritance allows us to define a class that inherits "all the public methods and public properties" from another class.
            Parent class is the class being inherited from, also called base class or superclass.
            Child class is the class that inherits from another class, also called derived class or subclass.

Uses/Importance/Advantages of Inheritance--
    1. to achieve Reusability of code. It allows us to add more features to a class without modifying it.
    2. to represent the hierarchical relationship(parent-child) between classes.
    3. to provide transitive properties to classes, which means that if class B inherits from another class A,
       then all the subclasses of B would automatically inherit from class A.
    4. Inheritance offers a simple, understandable model structure.

How to check if we can apply/bring Inheritance between two classes?
    To check we use a simple "isA" test which returns a boolean value.
    "isA" test says that--
    between classes C1 and C2,we can apply inheritance if C1 isA C2 is true,i.e. C1 is a child of C2.
    If it returns False, then inheritance is cannot be applied between the two classes(C1 and C2).
Example -
        cat isA animal - returns TRUE - so we can apply inheritance.
    But,cat isA machine - returns FALSE - so we cannot apply inheritance.

## super() keyword - used to access the parent class members(properties and methods).
'''

# Remainder - "self" keyword always refers to the class/method in which it is called.
#INHERITANCE - Example

class Animal:    # Animal is Parent class.
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(self.name + " animal is Eating")

# Dog is Child class. We use parenthesis during class declaration to indicate that it is a child class of Animal.
# Format - class Child_class_name(Parent_class_name):
class Dog(Animal):
    # To make child class we need to make the object of the Parent class.
    # To make child class we need to first declare all the parameters of parent class in the __init__ method.
    # One can also declare extra/optional parameters according to the requirement.
    def __init__(self,name,type):
        #Call the constructor/initializer of parent class(Animal).
        Animal.__init__(self,name)  # Calling the __init__ method of Animal without using super() keyword
        super().__init__(name)  # Using super() keyword to call the parent initializer, here super() represents the parent class"Animal".
        # When using super() we do not need to write the self keyword.
        self.type = type    # Initializing the field"type" of child class(Dog).
    def getTheNameOfDog(self):
        print(self.name)

dog = Dog("Tommy","Husky")  #Creating the object"dog" of child class(Dog).
dog.eat()     # Calling the eat() method of parent class(Animal) through object "dog" of child class(Dog).
# Even though we have not created any method "eat" in "Dog" class, but we can still call the "eat" function due to inheritance.
dog.getTheNameOfDog()

# Use of super() keyword
class Parent:
    property  = 90
    def eat(self):     # Method "eat" is defined in parent class.
        print("Parent eating!")
class Child(Parent):
    property = 100    # same property name"property" as in parent. So to distinguish between parent and child,
                      # we use self.property for child and super().property for parent.
    def display(self):
        print("Child property ", self.property)   # self represent the current class in which it is called.
        print("Parent property ", super().property) # super() always represent the parent class.
    def eat(self):      # Same method name "eat" in child class as in parent class.
        # Example of Method Overriding since method "eat" is already defined in parent class.
        # So method "eat" in child class will override the method "eat" in parent class when we call it in child class.
        # So we need to use super() keyword to call the method in parent class from child class.
        print("Child eating!")
    def callEat(self):
        self.eat()
        super().eat()


obj = Child()
obj.display()
obj.callEat()
'''
Method Overriding - is an ability of any object-oriented programming language 
that allows a subclass or child class to provide a specific implementation of a method
that is already provided by one of its super-classes or parent classes.
Example - "eat" method in the above example of "Parent" and "Child" class.
'''
