class Employee():

    num_of_employees = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = f"{fname }.{lname}@company.com "

        Employee.num_of_employees += 1
    def full_name(self):
        return f" {self.fname } {self.lname}"
    def raised(self):
        self.salary = int(self.salary + 5000)
        return self.salary
emp1 = Employee(fname="Mehdi",lname="Abbas",salary=500000)
emp2 = Employee(fname="Ali",lname="Abbas",salary=600000)
print(emp1.email)
print(Employee.full_name(emp1))
print(Employee.raised(emp2))

emp2.salary = 2.001
print(Employee.raised(emp2))
print(emp2.raised())
print(emp1.__dict__)
print(Employee.num_of_employees)