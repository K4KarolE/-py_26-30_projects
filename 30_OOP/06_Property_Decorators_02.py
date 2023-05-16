''' Setter, Deleter '''
'''
we want:
employee_1.fullname = 'Becky Boo'
-> first_name, last_name, email should be updated

How can we achieve this?
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
    
    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name
    
    @fullname.deleter
    def fullname(self):
        print('- Delete Name -')
        self.first_name = None
        self.last_name = None

employee_1 = Employee('Bobby','Black', 40000)
employee_2 = Employee('Peggy','Wanker', 45000)

employee_1.first_name = 'Jim'
employee_1.fullname = 'Becky Boo'
print(employee_1.first_name)
print(employee_1.email)
print(employee_1.fullname)

print('\n')

del employee_1.fullname
print(employee_1.first_name)
print(employee_1.email)
print(employee_1.fullname)


'''
@property
def fullname(self):                                         
    return '{} {}'.format(self.first_name, self.last_name)

@fullname.setter            - original method`s name.setter
def fullname(self, name):   - original method`s name
    first_name, last_name = name.split(' ')
    self.first_name = first_name
    self.last_name = last_name
'''

'''
@fullname.deleter
def fullname(self):
    print('- Delete Name -')
    self.first_name = None
    self.last_name = None

    
del employee_1.fullname
'''