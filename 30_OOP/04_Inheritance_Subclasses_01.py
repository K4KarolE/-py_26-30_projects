''' Inheritance'''
'''
Inheritance allow us to inherit attributes and methods from a parent class.
We are able to create sublasses
    - and get all the functionality of the parent class
    - and we can override or add new functionality without affecting the parent class
'''

''' Creating Developer and Manager subclasses '''

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
class Developer(Employee): # inherit from the Employee class
    pass 
    
employee_1 = Employee('Bobby','Black', 'blackmoonhunter@darkside.com', 40000)
employee_2 = Employee('Peggy','Wanker', 'bestwife@couch.com', 45000)

print(employee_1.email_comp)
print(employee_2.email_comp, '\n')

employee_3 = Developer('Bobby','Black', 'blackmoonhunter@darkside.com', 40000)
employee_4 = Developer('Peggy','Wanker', 'bestwife@couch.com', 45000)

print(employee_3.email_comp)
print(employee_4.email_comp)
''' Same result '''



'''
class Developer(Employee):
    pass

Searching for atributes and methods -> Developer class is empty -> looking for the Employee class -> called: Method Resolution Order
'''
print(help(Developer))