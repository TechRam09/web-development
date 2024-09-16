class emp_with_default_values():
    def __init__(self,name="Nishanth",sector="FSD",salary="850000",exp="4.5 years"):
        self.name = name
        self.sector = sector
        self.salary = salary
        self.exp = exp

    def person_info(self):
        return ({self.name},{self.sector},{self.salary},{self.exp})

empdv = emp_with_default_values()
print(empdv.name)
print(empdv.sector)
print(empdv.salary)
print(empdv.exp)