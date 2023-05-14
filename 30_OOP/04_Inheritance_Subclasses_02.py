
class Employee:

    raise_amount = 1.04

    def __init__(self, first_name, last_name, email_private, pay):      
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email_comp = first_name + '.' + last_name + '@company.com'
        self.email_private = email_private

    def fullname(self):                                         
        return '{} {}'.format(self.first_name, self.last_name)
    
    def apply_raise(self):                          
        self.pay = int(self.pay * self.raise_amount)

#!!!
class Developer(Employee):
    raise_amount = 2

employee_1 = Developer('Bobby','Black', 'blackmoonhunter@darkside.com', 40000)
employee_2 = Employee('Peggy','Wanker', 'bestwife@couch.com', 45000)

'''
class Developer(Employee):
    pass                    -> For a Developer, able to use the Employee class` data(raise_amount) and method(apply_raise)
'''
'''
class Developer(Employee):
    raise_amount = 1.5      -> this raise_amount will be used for Developers, no effect on the Employee`s raise_amount
'''
# Dev
print(employee_1.pay)
employee_1.apply_raise()
print(employee_1.pay)
# Emp
print('\n')
print(employee_2.pay)
employee_2.apply_raise()
print(employee_2.pay)









