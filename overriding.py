class Employee:
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary

class SalesOfficer(Employee):
    def __init__(self,nm,sal,inc):
        super().__init__(self,nm,sal)
        self.incent=inc

    def getSalary(self):
        return self.salary + self.incent
e1=Employee("Rohit",70000)
print("Total salary for {} is rs.{}".format(e1.getName(),e1.getSalary()))
s1=SalesOfficer("Rakesh",20000,5000)
print("Toatl salary for {} is Rs.{}".format(s1.getName(),s1.getSalary()))
