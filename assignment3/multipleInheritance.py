#multiple inheritence

class employee_role:
    def main_work(self):
        print("I am a full stack developer")

class alter_work:
    def alter_job(self):
     print("I am a part-time programmer")

class employee_multiple_inheritence(employee_role,alter_work):
    pass

emi = employee_multiple_inheritence()
print("Hi, I am Nishanth")
emi.main_work()
emi.alter_job()