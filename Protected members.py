class Employee:
    def __init__(self, name, age):
        self.name = name
        self._age = age

class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)

emp = SubEmployee("Hanuman", 21)
print(emp.name)
emp.show_age()
