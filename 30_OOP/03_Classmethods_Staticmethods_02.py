''' Static method'''
'''
static method - do not pass any argument automatically
regular method - pass the instance as the first argument
class method - pass the class as the first argument
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
    
    @classmethod        
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    
    @classmethod        
    def from_String(cls, employee_string):
        first_name, last_name, priv_email, pay = employee_string.split('-')
        return cls(first_name, last_name, priv_email, pay)
    
    #!!!
    @staticmethod           # no access to to INSTANCE or the CLASS in the function
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: # 0-Monday, 6-Sunday
            return False
        return True

        
employee_1 = Employee('Bobby','Black', 'blackmoonhunter@darkside.com', 40000)
employee_2 = Employee('Peggy','Wanker', 'bestwife@couch.com', 45000)

import datetime
my_date = datetime.date.today()
my_date_snd = datetime.date(2023,5,10)

print(Employee.is_workday(my_date))
print(Employee.is_workday(my_date_snd))









