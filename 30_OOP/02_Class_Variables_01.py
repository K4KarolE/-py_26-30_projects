'''
Class Variables - variables that are shared among all instances of a class (example: annual raise)
Instance Variables - unique for each instance (example: name, email, pay)
'''
class Employee:
    def __init__(self, first_name, last_name, email_private, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email_comp = first_name + '.' + last_name + 'company.com'
        self.email_private = email_private
    
    def fullname(self):   
        return '{} {}'.format(self.first_name, self.last_name)
    
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)     # raise amount placement is not ideal -> create a class variable / see below   

        
employee_1 = Employee('Bobby','Black', 'blackmoonhunter@darkside.com', 40000)
employee_2 = Employee('Peggy','Wanker', 'bestwife@couch.com', 45000)

# print(employee_1.pay)
# employee_1.apply_raise()
# print(employee_1.pay)

'''----------------------------------------------------------------------------'''

class Employee_Snd:

    raise_amount = 1.04     # CLASS VARIABLE

    def __init__(self, first_name, last_name, email_private, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email_comp = first_name + '.' + last_name + 'company.com'
        self.email_private = email_private
    
    def fullname(self):   
        return '{} {}'.format(self.first_name, self.last_name)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee_Snd.raise_amount)      # without self or Employee_Snd will drop an error
        # self.pay = int(self.pay * self.raise_amount)    

        
employee_1 = Employee_Snd('Bobby','Black', 'blackmoonhunter@darkside.com', 40000)
employee_2 = Employee_Snd('Peggy','Wanker', 'bestwife@couch.com', 45000)


# print(employee_1.raise_amount)      # employees do not have raise amount attributes -> accessing the class raise_amoint attrubte
# print(employee_2.raise_amount)
# print(Employee_Snd.raise_amount)

print('\n')
# print(employee_1.__dict__)
''' no raise_amount for an instance
{'first_name': 'Bobby', 'last_name': 'Black', 'pay': 40000, 'email_comp': 'Bobby.Blackcompany.com', 'email_private': 'blackmoonhunter@darkside.com'}
'''

print('\n')
# print(Employee_Snd.__dict__)
''' includes raise_amount
{'__module__': '__main__', 'raise_amount': 1.04, '__init__': <function Employee_Snd.__init__ at 0x0000021A348699E0>, 'fullname': <function Employee_Snd.fullname at 0x0000021A34869A80>, 'apply_raise': <function Employee_Snd.apply_raise at 0x0000021A34869B20>, '__dict__': <attribute '__dict__' of 'Employee_Snd' objects>, '__weakref__': <attribute '__weakref__' of 'Employee_Snd' objects>, '__doc__': None}
'''

Employee_Snd.raise_amount = 1.05    # will change for the whole class / all instances
print(employee_1.raise_amount)      
print(employee_2.raise_amount)
print(Employee_Snd.raise_amount)

employee_1.raise_amount = 1.07    # will change only for the employee_1
print(employee_1.raise_amount)      
print(employee_2.raise_amount)
print(Employee_Snd.raise_amount)
print('\n')
print(employee_1.__dict__)
''' INCLUDES raise_amount for this instance // employee_2`s raise amount still coming from the class attribute
{'first_name': 'Bobby', 'last_name': 'Black', 'pay': 40000, 'email_comp': 'Bobby.Blackcompany.com', 'email_private': 'blackmoonhunter@darkside.com', 'raise_amount': 1.07}
'''

'''
def apply_raise(self):
        self.pay = int(self.pay * Employee_Snd.raise_amount) -> ?? still able to update individual instance // updating the value: will change for the whole class / all instances
        self.pay = int(self.pay * self.raise_amount)  -> able to change/update for individual instances and allow any subclass to overwrite it
'''


