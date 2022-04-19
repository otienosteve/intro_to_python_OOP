class User:

    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def printUser(self):
        print(f"{self.name} is {self.age}")

    def describe(self):
        print("I am a User")



class Admin(User):
    pass


admin1=Admin("Super001",30)
admin1.printUser()




# childclass extends baseclass
# User1=User("Steve",40)
# # User.printUser()
# User1.printUser()
# User1.describe()

#python does not have the this keyword