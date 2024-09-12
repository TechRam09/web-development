# class Human:
    
#     def __init__(self,name):
#         self.name = name
        
        
# p = Human("Shree")
# print(p.name)


# class Human:
    
#     def __init__(self,firstname,lastname,age,city,country):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.city = city
#         self.country = country
        
# p = Human("Shreeram","N S",20,"Mysore","India")
# print(p.firstname)
# print(p.lastname)
# print(p.age)
# print(p.city)
# print(p.country)

class Human:
    
    def __init__(self,firstname="Shreeram",lastname="N S",age=20,city="Mysore",country="India"):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.city = city
        self.country = country
        
    def personInfo(self):
       return f"firstName:{self.firstname},lastname:{self.lastname},age:{self.age},City:{self.city},Country:{self.country}"
        
        
p = Human()
print(p.personInfo())

p1 = Human("Nishanth","H S","Mysore","India")
print(p1.personInfo())