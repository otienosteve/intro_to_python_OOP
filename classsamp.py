from abc import ABC, abstractmethod
class User(ABC):
    @abstractmethod
    def haveName():
        pass

class Admin(User):

    def __init__(self, name, age):
        self.__name=name
        self.age=age
    def haveName(self, name):
        print("I have a name it is "+name)
        
    def printUser(self):
        print(f"{self.name} is {self.age}")


    
    def describe(self, name=None,age=None):
        if name!=None and age!=None:
            print(f"Your name is {name} and your age is {age}")
            return
        if age!=None:
            print(f"You are {age} years old")
            return
        if name!=None:
            print(f" Your Name is {name}")
            return
      
    def overload(self,*args):
        for i in args:
            print(i)

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name=name

    
# user1=User("Python",50)
# user1.setName("Java")
# admin1=Admin("Super001",30)
# admin1.describe("Steve")
# ls=[1,"Steve",True]
# admin1.overload(*ls)
# admin1.describe("Steve",40,"Technical Mentor")
# admin1.haveName("Steve")
# admin1.printUser()
# print(admin1._name)
# print(user1.getName())
# user1.describe()
# user1.describe("Steve")
# user1.describe("Steve", 40)


# admin1.describe(None,"Steve")

# childclass extends baseclass
# User1=User("Steve",40)
# # User.printUser()
# User1.printUser()
# User1.describe()
#inheritance
#encapsulation
#polymorphism-taking many forms
#method overloading
#abstraction
# private, protected, public

#python does not have the this keyword