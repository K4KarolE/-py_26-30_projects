''' Class methods'''
'''
regular method - pass the instance as the first argument
class method - pass the class as the first argument
static method - do not pass any argument automatically

REGULAR:

def fullname(self):                                         
    return '{} {}'.format(self.first_name, self.last_name)

# how to change this to take the CLASS as the first argument:
    - use class methods (see the methods below with @classmethod decorators)
'''


class Employee:

    number_of_employee = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, email_private, pay):      
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email_comp = first_name + '.' + last_name + 'company.com'
        self.email_private = email_private

        Employee.number_of_employee +=1    
    
    def fullname(self):                                         
        return '{} {}'.format(self.first_name, self.last_name)
    
    def apply_raise(self):                          
        self.pay = int(self.pay * self.raise_amount)
    
    #!!!
    @classmethod        # + cls=class(word class can not be used, already occupied), altering the functionality of the method -> receiving CLASS as the first argument
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    #!!!
    @classmethod        # create alternative constracture
    def from_String(cls, employee_string):
        first_name, last_name, priv_email, pay = employee_string.split('-')
        return cls(first_name, last_name, priv_email, pay)

        
employee_1 = Employee('Bobby','Black', 'blackmoonhunter@darkside.com', 40000)
employee_2 = Employee('Peggy','Wanker', 'bestwife@couch.com', 45000)


Employee.set_raise_amount(1.05)
# employee_1.set_raise_amount(1.05)     # same result, but less professional
print(Employee.raise_amount)
print(employee_1.raise_amount)
print(employee_2.raise_amount)

emp_string_1 = 'Becky-Jane-love@love.com-70000'
emp_string_2 = 'John-Doe-reme@mber.com-74000'

# INSTAED
# first_name, last_name, priv_email, pay = emp_string_1.split('-')
# new_employee = Employee(first_name, last_name, priv_email, pay)
# print(new_employee.first_name, new_employee.last_name, '- pay:', new_employee.pay)

# new method, FROM_STRING - alternative constracture
new_employee = Employee.from_String(emp_string_1)
print(new_employee.first_name, new_employee.last_name, '- pay:', new_employee.pay)






