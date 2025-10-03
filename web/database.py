from typing import List
from abc import abstractmethod

class Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def getName(self):
        return self.name
    
    def getValue(self):
        return self.value
    
    def setName(self, newName):
        self.name = newName
        
    def setValue(self, newValue):
        self.value = newValue
    
    def getDetails(self):
        return f"Name : {self.name} , Value : {self.value}"
        
class Table:
    def __init__(self, name):
        self.name = name
        self.fields : List[Field] = []
        
    def addField(self, field : Field) :
        existing = self.findField(field.name)
        
        if existing:
            return "Already exist"
        else:
            self.fields.append(field)
            
    def findField(self, name):
        for i in self.fields:
            if name == i.name:
                return i
        return None
    
    def getDetails(self):
        return f"Name {self.name}, Number of fields : {len(self.fields)}"

    def displayFields(self):
        for i in self.fields:
            print(i.getDetails())
        

class Database:
    def __init__(self, name):
        self.name = name
        self.tables : List[Table] = []
        
    def addTable(self, table : Table) :
        existing = self.findTable(table.name)
        
        if existing:
            return "Already exist"
        else:
            self.tables.append(table)
            
    def findTable(self, name):
        for i in self.tables:
            if name == i.name:
                return i
        return None
    
    def displayTables(self):
        for i in self.tables:
            print()
            
# ------ API --------- #


class Model:
    def __init__(self, id):
        self.id = id
        
class Customer:
    def __init__(self,name, id):
        self.name = name
        self.id = id
        

class CustomerRepository:
    def __init__(self):
        self.customers : List[Customer]= []
        
class CustomerService(Model):
    def __init__(self,id):
        super(id)
        
    def request(self, type):
        if type == "POST":
            self.addCustomer()
        elif type == "DELETE":
            self.removeCustomer()
        else:
            return
        
    def addCustomer(self, customer: Customer, repo : CustomerRepository):
        repo.customers.append(customer)
        
    def removeCustomer(self, id, repo : CustomerRepository):
        for c in repo.customers:
            if c.id == id:
                repo.customers.remove(c)
        return
    
        
        
    

class Route:
    def __init__(self, key, model):
        self.key = key
        self.model = model
        


class Api:
    def __init__(self):
        self.routes : List[Route] = []
        
        


customerModel = CustomerService(1)
customerRoute = Route(1, customerModel)

api = Api()
api.routes.append(customerRoute)

        

        