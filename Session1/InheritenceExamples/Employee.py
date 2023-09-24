# Abstraction
class Employee:
    def __init__(self,name, empid, department):
        #no functionality for Private variables in Python 
        #we use _ to hint the programmers not to modify it
        self.__name = name
        self.__empid = empid
        self.department = department

    def get_employee_details(self):
        print("name is:", self.__name)
        print("empid is: ", self.__empid)
        print("department is:", self.department)

    def assign_department(self, emp_department):
        self.department = emp_department 
    
emp1 = Employee("Soumya",111,"Data")
#print(emp1.__name)
#emp1.get_employee_details()
# we can still modify the value 
emp1.get_employee_details()
print(emp1.__name)
