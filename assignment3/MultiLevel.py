class Employee:
    def work(self):
        print("Employee can work")

class Manager(Employee):
    def manage(self):
        print("Manager can manage")

class Engineer(Manager):
    def develop(self):
        print("Engineer can develop")

#objects

e = Engineer()
e.work()
e.manage()
e.develop()
