#single inheritence


class employee_inheritance:
    def __init__(self,name,post):
        self.name = name
        self.post = post

    def about(self):
        print("Employee name is " + self.name)
        print("employee post is "+ str(self.post))

class non_working_staff(employee_inheritance): #inheritence
    def stateprofession(delf):
        print("I am a peon")

emp_inherit = employee_inheritance("Ram","peon")
print("My name is : \n",emp_inherit.name)
print("The post i work for: \n",emp_inherit.post)