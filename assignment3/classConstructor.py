#employee info with constructor

class emp_with_constructor():
    def __init__(self,name,sector,salary,exp,city):
        self.name = name
        self.sector = sector
        self.salary = salary
        self.exp = exp
        self.city = city

empd = emp_with_constructor("Nishanth","Full stack web development",700000,"5 years","Mysuru")
print(empd.name)
print(empd.sector)
print(empd.salary)
print(empd.exp)
print(empd.city)