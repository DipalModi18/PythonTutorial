class Employee:
    """Optional class documentation string"""
    empCount = 0

    def __init__(self, name: str, salary: float):
        print("In Employee's constructor")
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)
        return

    def changeDetails(self):
        self.name = input("Enter name: ")
        self.salary = int(input("Enter salary: "))
        self.displayEmployee()
        return


emp1 = Employee("Dipal", 21000)

setattr(emp1, 'salary', 20000)
# hasattr(emp1, 'salary')    # Returns true if 'salary' attribute exists
# getattr(emp1, 'salary')    # Returns value of 'salary' attribute
# setattr(emp1, 'salary', 7000) # Set attribute 'salary' at 7000
# delattr(emp1, 'salary')    # Delete attribute 'salary'

emp1.displayEmployee()

emp2 = Employee("Ekta", 21000)
print("Employee count: ", emp2.empCount)


class Developer(Employee):

    def __init__(self, name: str, salary: float, lang: str):
        super().__init__(name, salary)
        self.lang = lang
        print("In Developer's constructor")
        return

    def displayEmployee(self):
        super().displayEmployee()
        print("Languages known: ", self.lang)


dev1 = Developer("Dipal", 20000, "Python")
dev1.displayEmployee()


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        return

    def __add__(self, other):  # To override + operator
        return Vector(self.x + other.x, self.y + other.y)

    def displayVector(self):
        print("X: ", self.x, " Y: ", self.y)
        return


v1 = Vector(3, 4)
v2 = Vector(5, 6)
(v1+v2).displayVector()
