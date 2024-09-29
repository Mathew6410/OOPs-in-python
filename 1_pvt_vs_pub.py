# pub vs pvt Attribute and methods

class Account:
    def __init__(self, accNO, accPass):
        self.accNO = accNO
        self.__accPass = accPass

    # But we can access pvt attribute/method within the class
    # method
    def reset(self):
        print(self.__accPass)


acc1 = Account(123456789, "absche@123")
print(acc1.accNO)

acc1.reset()    # o/p -> absche@123          Although the __accPass is a pvt sttribute and we do not have direct access to it but still we got to 
#                                            access it indirectly through the reset function which is present in the class. 

# print(acc1.__accPass)       # AttributeError: 'Account' object has no attribute '__accPass'

# Conclusion : Unlike other languages such as C++ and java where private attribute and method exist, in python purely private attribute/method not 
#              exist but yes private like attributes/methods does exist.

print("\n")

class Student:
    # parameterized constructor
    def __init__(self, name, marks, blood):
        self.name = name
        self.__marks = marks
        self.__blood = blood

    # Pvt method
    def __bloodInfo(self):
        print("Blodd group is -->", self.__blood)

    # Pvt method
    def __marksInfo(self):
        print("Marks alloted is ->", self.__marks)

    # Public method
    def allInfo(self):
        self.__bloodInfo()
        self.__marksInfo()

stu1 = Student("Abhishek", 900, "A+")

print(stu1.name)

# print(stu1.__marks)     # AttributeError: 'Student' object has no attribute '__marks'

# print(stu1.__blood)     # AttributeError: 'Student' object has no attribute '__blood'

# stu1.__bloodInfo()      # AttributeError: 'Student' object has no attribute '__bloodInfo'

# stu1.__marksInfo()        # AttributeError: 'Student' object has no attribute '__marksInfo'  

stu1.allInfo()



































