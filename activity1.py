# parent class
class Person( object ):
    # __init__ is know as the consturctor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
      print(self.name)
      print(self.idnumber)

# child class
class Employee( Person ):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

# creation of an object variable or an instance
a = Employee('Peter', 20131001, 645792, "Intern")

# calling a fuction of the class Person using its instance
a.display()