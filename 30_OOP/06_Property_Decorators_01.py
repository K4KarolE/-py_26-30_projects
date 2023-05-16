''' Getter '''
'''
Allows us to give class attributes Getters, Setters, Deleters functionality

Allows us to define a method where we can access it like an attribute
'''

class Employee:

    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):      
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        # self.email = first_name + '.' + last_name + '@company.com'
    
    @property
    def email(self):                                         
        return '{}.{}@company.com'.format(self.first_name, self.last_name)

    @property
    def fullname(self):                                         
        return '{} {}'.format(self.first_name, self.last_name)
    

employee_1 = Employee('Bobby','Black', 40000)
employee_2 = Employee('Peggy','Wanker', 45000)

employee_1.first_name = 'Jim'


print(employee_1.first_name)
print(employee_1.email)
print(employee_1.fullname)

'''
employee_1.first_name = 'Jim'

print(employee_1.first_name)
print(employee_1.email)
print(employee_1.fullname())

Jim
Bobby.Black@company.com     - did not change
Jim Black
'''

'''
def __init__(self, first_name, last_name, pay):      
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        #!! REMOVE - self.email_comp = first_name + '.' + last_name + '@company.com'
    
    #!! ADD
    def email(self):                                         
        return '{}.{}@company.com'.format(self.first_name, self.last_name)


print(employee_1.email())      - () should be given and code should be updated to this method call - solution below
'''

''' Adding @property to the method -> will act like an attribute of the class
@property
def email(self):                                         
    return '{}.{}@company.com'.format(self.first_name, self.last_name)

print(employee_1.email)      - no () needed - email will be updated - no further code update needed 
'''

