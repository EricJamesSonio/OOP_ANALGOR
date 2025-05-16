from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        self.infoviewer = DetailsViewer(self)
        self.calculator = Calculator(self)
        
    def display_info(self):
        self.infoviewer.display_info()
    
    @abstractmethod
    def calculate_bonus(self):
        pass
        
    def apply_salary_increase(self, increase_percentage):
        return self.calculator.apply_salary_increase(increase_percentage)
        
class DetailsViewer:
    def __init__(self, employee : Employee):
        self.employee = employee
        
    def display_info(self):
        print(f"Name: {self.employee.name}")
        print(f"Position: {self.employee.position}")
        print(f"Salary: ₱{self.employee.salary}")
        
class Calculator:
    def __init__(self, employee : Employee):
        self.employee = employee       
        
    def apply_salary_increase(self, increase_percentage):
        self.employee.salary += self.employee.salary * (increase_percentage / 100)
        print(f"New salary for {self.employee.name}: ₱{self.employee.salary}")

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.2
    
class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.1
    
class Intern(Employee):
    def calculate_bonus(self):
        return self.salary * 0.05