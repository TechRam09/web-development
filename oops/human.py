class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduceYourSelf(self):
        print(f'My Name is {self.name}')
        print(f'My age is {self.age}')
        
        
class Teacher(Person):
    
    def statProfession(self):
        print("I am Teacher")


author = Teacher("Rakesh",45)
author.introduceYourSelf()
author.statProfession()