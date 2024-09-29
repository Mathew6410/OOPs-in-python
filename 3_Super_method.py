# Super method : super() method is special method used to access the methods of parent class. It is related to 
#                Inheritance.

# syntax --> super().propertyofparentclass(attribute)

class Car:
    # parameterized constrcutor
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped.")

class Toyota(Car):
    # parameterized constructor
    def __init__(self, name, type):
        self.name = name
        # self.type = type --> Iss command se 'type' attribute create hoga 'Toyota' class mein na ki parent 
        #                      class k 'type' parameter mein.  
        super().__init__(type)
        
        # Iss toyota class k ander agar base class mein jo type parameter hain, oosey access karke usmey store karna hain data toh super() class ka use karna padega kyonki yahan par agar type attribute bana kar type param mein kuc pass karenge toh wo actually Toyota class k ander ka attribute hoga.

car1 = Toyota("Range Rover","electric")
print(car1.name)

# Now i want to print suppose type 
print(car1.type)



print("\n")



class Motorbike:
    # parameterized constructor
    def __init__(self, type):
        self.type = type

    # method
    @staticmethod
    def ignite():
        print("Droom Droom droom droom......")

    @staticmethod
    def stopped():
        print("phisssssssss.")

class TVS(Motorbike):
    #parameterized constructor
    def __init__(self, name, type):
        # for storing value of bike i.e. 'petrol' inside the parameter of parent class 'motorbike''s constructor from this child class, we use super() method in the following way:
        super().__init__(type)
        self.name = name


bike1 = TVS("Apache", "petrol")
print(bike1.name)
print(bike1.type)

