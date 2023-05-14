
class Employee:
    def __init__(self, first_name, last_name, email_private, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email_comp = first_name + '.' + last_name + '@company.com'
        self.email_private = email_private
    
    def fullname(self):     # automatically takes instance as "self" as first argument
        return '{} {}'.format(self.first_name, self.last_name)


employee_1 = Employee('Bobby','Black', 'blackmoonhunter@darkside.com','40000')
employee_2 = Employee('Peggy','Wanker', 'bestwife@couch.com','45000')

print(employee_1.email_comp)
print(employee_2.email_comp)


# Display employee full name
# Manually
print('{} {}'.format(employee_1.first_name, employee_1.last_name))
# Method called on an instance -- could have added to the Employee class as another attribute: self.fullname = first_name + last_name
print(employee_1.fullname())
# Same - method called on the class - instance needed as argument
print(Employee.fullname(employee_1))


'''
if no self in fullname(****) -> TypeError: Employee.fullname() takes 0 positional arguments but 1 was given

class Employee
    ...
    def fullname():
        return '{} {}'.format(self.first_name, self.last_name)

print(employee_1.fullname())

---
employee_1.fullname()
fullname() - looks like no argument passed in (), but instance (employee_1) getting passed automatically as below
---
print( Employee.fullname(employee_1) )

'''