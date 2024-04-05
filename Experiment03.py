'''Experiment 03
Classes: Employee, Developer, Tester, Manager
Developer, tester, Manager inherit Employee
Manager handles Developer, tester
Manager class : implement functions to add Developer/Tester and Remove Developer/ Tester
Display .. to see the list of employees he manages'''
class Employee:
    def __init__(self,fname,lname,empId):
        self.fname=fname
        self.lname=lname
        self.empId=empId

class Developer(Employee):
    def __init__(self,fname,lname,empId,programming_language):
        super().__init__(fname,lname,empId)
        self.programming_language=programming_language

class Tester(Employee):
    def __init__(self,fname,lname,empId,testingTool):
        super().__init__(fname,lname,empId)
        self.testingTool=testingTool

class Manager(Employee):
    all_managers=[]
    def __init__(self,fname,lname,empId,managed_employees):
        super().__init__(fname,lname,empId)
        self.managed_employees=managed_employees
        Manager.all_managers.append(self)

    def add_employee(self,employee):
        if employee in self.managed_employees:
            print(f"{employee.fname}{employee.lname} already managed by {self.fname}{self.lname}")
        elif any(employee in manager.managed_employees for manager in Manager.all_managers):
            print(f"{employee.fname} {employee.lname} is already managed by another manager.")
        else:
            self.managed_employees.append(employee)
            
    def remove_employee(self,employee):
        if employee in self.managed_employees:
            self.managed_employees.remove(employee)
        else:
            print(f"{employee.empId}{employee.fname}{employee.lname} is not not managed by{self.fname}{self.lname} ")

    def print_employees(self):
        print(f"Employees managed by {self.fname}{self.lname}")
        for employee in self.managed_employees:
            print(f"-{employee.fname}{employee.lname}{employee.empId}")



Developer01=Developer('Vidhi','Shah',45,'Python')
Developer02=Developer('Devesh','Sharma',46,'C++')
Developer03=Developer('Fenil','Shah',47,'Python')
Developer04=Developer('Rushaan','Shah',78,'C++')

tester01=Tester('Vedant','Taware',232,'Python')
tester02=Tester('Taran','Shah',256,'C++')

Manager01=Manager('Sejal','Yadav',179,[Developer03,Developer04,tester01])
Manager02=Manager('Netra','Agarwal',178,[Developer01,tester02])

Manager01.print_employees()


Manager02.add_employee(Developer02)
Manager02.add_employee(Developer03)

Manager02.print_employees()

Manager02.remove_employee(Developer02)

Manager02.print_employees()

