# Inheritance : When one class (child/derived) drives the properties & methods from other class (parent/Base). 

# Inheritance is the 3rd pillar after in abstraction and encapsulation in the OOPs concept.
'''  class Car:                 --> base/parent class
         ........

     class Toyota(Car):         --> derived/child class
         ................
'''
# Like we human child inherit characteristics, color, blood group, and even properties from our parents, same way in programming child/derived class inherit all the attributes and mehod from it's parent/base class.

'''Inheritance is of 3 types:
    1. Single Inheritance 
    2. Multi-level Inheritance
    3. Multiple Inheritance
'''

# 1. Single Inheritance : Only one parent/base class exist for a derived/child class.
class Car:
    color = "Black"

    # static methods
    @staticmethod
    def startInfo():
        print("Car started....")

    @staticmethod
    def stopInfo():
        print("Car stopped.")

class Toyota(Car):
    # parameterized constructor
    def __init__(self, name, type):
        self.name = name
        self.type = type

c1 = Toyota("Innova", "diesel")
print(c1.name, c1.type)
c1.startInfo()
c1.stopInfo()
print(c1.color)



print("\n")



# 2. Multi-level Inheritance : Every child/derived class has exactly single parent/basse class only but there 
#                              is a series of parent-child like
class Universe:
    size = "Infinite"

    @staticmethod
    def galaxy():
        print("There are millions of galaxy exist in the universe.")

    @staticmethod
    def galaxyInfo():
        print("There are hundreds of universe in each galaxy.")

class Earth(Universe):
    shape = "Round"

    @staticmethod
    def EarthInfo():
        print("There are multiple around 7 continent in planet Earth.")

class Asia(Earth):
    location = "South-east"

    @staticmethod
    def countryCount():
        print("There are 11 counteries in the asia continent.")

class India(Asia):
    loc = "Southern"

    # parametrized constructor
    def __init__(self, state, capital):
        self.state = state
        self.capital = capital

    @staticmethod
    def countryInfo():
        print("There is a democracy in India and it has multiple religion and languages.")

city = India("Madhya Pradesh", "Bhopal")
print(city.state,",",  city.capital)

city.countryInfo()

print(city.size)
print(city.location)
city.countryCount()
city.galaxy()
city.EarthInfo()

# Hence, we can say that there can be any number of levels can exist in the multi-level Inheritance concept as there can be more and more child class which turns out to be the parent class of another child class.



print("\n")



# 3. Multiple-Inheritance : When a single child/derived class has more than 1 parent/base class.

class Mother:
    color = "Fair"

    @staticmethod
    def character():
        print("Inheritated generousity from mother.")

class Father:
    height = 6

    @staticmethod
    def strength():
        print("Got strength from father's honesty and dignity.")

class Child(Mother, Father):
    position = "Elder"

    # parameterized constructor
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def bloodgrp(self):
        self.blood = "A+"
        print("BLood group of",self.name,"is",self.blood)

child1 = Child("Abhishek", "male")

print(child1.name, ",", child1.gender)
child1.bloodgrp()

print(child1.height)
print(child1.color)
child1.character()
child1.strength()


print ("\n")

class A:
    varA = "Welcome to class A."

class B:
    varB = "Welcome to class B."

class C(A,B):
    varC = "Welcome to class C."

c1 = C
print(c1.varC)
print(c1.varB)
print(c1.varA)
    