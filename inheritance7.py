class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id 

    def display(self):
        print(self.name,self.id)


emp1 = Employee("john",67)
emp2 = Employee("David",756)
emp1.display()
emp2.display()