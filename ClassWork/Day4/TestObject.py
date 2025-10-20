from ClassWork.Day4.Employees import NewEmployee
from Employees import Employee
from datetime import date

e1 = Employee()
print(e1)

dt = date.today()
print(dt) #__str__
print(repr(dt))

# e2 = Employee(empid=100)
# print(e2)
# print(type(e2))


n1 = NewEmployee('ppp', 45000)
n2 = NewEmployee('mmm', 90000)


NewEmployee.show_employee_count()
NewEmployee.set_count()
n3 = NewEmployee('kkk',50000)
NewEmployee.show_employee_count()