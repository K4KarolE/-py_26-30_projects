'''
Object-Oriented Programming benefits:
    - allow us to logically group our data / functions in a way:
        + easy to re-use
        + easy to build upon

data aka attribute
function aka method
'''

class Employee:     # class is a blueprint to create instances // first letter always uppercase
    pass

employee_1 = Employee()     # each employee are unique instances of the Employee class
employee_2 = Employee()

print(employee_1, employee_2)   # unique <- different memory allocation

# Manually create instance variables:       // time-consuming + open to mistake + tons of code
employee_1.first_name = 'Bobby'
employee_1.last_name = 'Black'
employee_1.email_comp = f'{employee_1.first_name}.{employee_1.last_name}@company.com'
employee_1.email_private = 'blackmoonhunter@darkside.com'
employee_1.pay = '40000'

employee_2.first_name = 'Peggy'
employee_2.last_name = 'Wanker'
employee_2.email_comp = f'{employee_2.first_name}.{employee_2.last_name}@company.com'
employee_2.email_private = 'bestwife@couch.com'
employee_2.pay = '45000'

print(employee_1.email_comp)
print(employee_2.email_comp)

class Employee:
    def __init__(self, first_name, last_name, email_private, pay):  # automatically takes instance as "self" as first argument
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email_comp = first_name + '.' + last_name + 'company.com'
        self.email_private = email_private