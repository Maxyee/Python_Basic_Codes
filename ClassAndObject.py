class Employee: # define the class
    empCount = 0

    def __init__(self, name, salary):  # it is a method of employee class
        self.name = name
        self.salary = salary
        Employee.empCount += 1


    def displayCount(self):             # this is displayCount method
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):          # this is displayEmployee method
        print("name : ", self.name, "Salary : ", self.salary)

emp1 = Employee("Eyamin", 2000)         # this emp1 object and assigning values of emp1
emp2 = Employee("Julhas", 5000)         # this emp2 object and assigning values of emp2

emp1.displayEmployee()                  # calling object with the class property / method
emp2.displayEmployee()

print("Total Employee %d" % Employee.empCount)