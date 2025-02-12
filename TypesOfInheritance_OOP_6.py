"""
Types Of Inheritance -
         1. Single Level Inheritance [parent_class A ----> child_class B]
         2. Multi-Level Inheritance [parent_class A ----> parent_class B ----> child_class C][Here B serves as child
                                    of A and parent of C]
         3. Hierarchical Inheritance [child_class B ----> parent_class A <---- child_class C]
                                     [When two or more classes inherits a single class, it is known as hierarchical inheritance.
                                     Example, Dog and Cat classes inherits the Animal class,so there is hierarchical inheritance.]
         4. Multiple Inheritance [parent_class B ----> child_class A <---- parent_class C]
                                [When a class inherits more than one class,i.e. a child_class has more than one parent class.]
         5. Hybrid Inheritance [child_Cat <---- parent_Animal ----> child_Dog <---- parent_Pet ----> child_Cat]
                            [it is combination of two or over two types of inheritances.
                            The data members of the base class will be accessed according to the specified visibility mode.]
"""

# 1.Single Level Inheritance
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("Animal is Eating")
class Dog(Animal):
    def __init__(self,name,type):
        super().__init__(name)
        self.type = type

# 2.Multi-Level Inheritance
class Animal:      # Parent class
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("Animal is Eating")
class Dog(Animal): # Child class of Animal but parent class of Pet
    def __init__(self,name,type):
        super().__init__(name)
        self.type = type
class Pet(Dog):    # Child class of Dog
    def __init__(self,name,type,houseName):
        super().__init__(name,type)
        self.houseName = houseName

# 3.Hierarchical Inheritance
class Animal:      # Parent class
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("Animal is Eating")
class Dog(Animal):      # Child class of Animal
    def __init__(self,name,type):
        super().__init__(name)
        self.type = type
class Cat(Animal):      # Child class of Animal
    def __init__(self,name,type):
        super().__init__(name)
        self.type = type


"""
# Multiple Inheritance - Multiple Inheritance faces complexities of ambiguity when two or more parent classes,
that are being inherited have methods/properties of same name. The child class can also share attributes of the same name
with their parent classes.
Thus when calling through the object of the child class, the compiler faces issue of which method to call.
Thus Multiple inheritance is not supported many programming languages like Java.

But Python solves this problem using MRO - Method Resolution Order -  the order in which base classes are searched when
looking for a method is called MRO.
In the case of multiple inheritance, a given attribute is first searched in the current class, if it’s not found then 
it’s searched in the parent classes. The parent classes are searched in a <left-right> fashion and each class is searched once.

To view the MRO of a class: 
            1. Use the mro() method, it returns a list.
                Eg. class_name.mro()
            2.Use the _mro_ attribute, it returns a tuple 
                Eg. class_name.__mro__  

"""
# 4.Multiple Inheritance
class A:
    def meth1(self):
        print("Hello from A")
class B:
    def meth2(self):
        print("Hello from B")
class C(A,B):
    def meth(self):
        print("Hello from Child C")

c = C()
c.meth1()
c.meth2()
c.meth()

# MRO - Multiple Inheritance
class A:
    def meth(self):
        print("Hello from A")
class B:
    def meth(self):
        print("Hello from B")
class C(A,B):
    def meth1(self):
        print("Hello from Child C")

obj = C()
obj.meth()
# In MRO - the order starts with child class and move from left to right in which the parent class is derived in child class.
# Example in class C(A,B) -> the MRO first checks C for the method/properties, then A and then B and then object,
# if any method/properties is defined through the object.
# In case of class C(B,A) -> The MRO first checks C for the method, then B and then A and then object.
# To check the order we use the _mro_ attribute of the class.
print(C.__mro__)


# 5.Hybrid Inheritance
class Pet(Dog,Cat):   # Child class of Dog and Cat
    # Dog and Cat classes shows hierarchical inheritance where Animal is their parent class.
    pass
