'''
print(1+2)      -> 3
# INT and STR classes built in ADD methods -> we are able to create our own ADD method
print(int.__add__(1,2))         -> 3
print(str.__add__('a','b'))     -> ab
'''

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

    def __repr__(self):        
        return "Employee('{}','{}','{}')".format(self.first_name, self.last_name, self.pay)
    
    def __str__(self):        
        return '{} - {}'.format(self.fullname(), self.email_comp)
    
    #!!!
    def __add__(self, other):
        return self.pay + other.pay
    
    #!!!
    def __len__(self):
        return len(self.fullname())


employee_1 = Employee('Bobby','Black', 'blackmoonhunter@darkside.com', 40000)
employee_2 = Employee('Peggy','Wanker', 'bestwife@couch.com', 45000)
employee_3 = Employee('Don','Tom', 'don@tom.com', 60000)

print(employee_1 + employee_2)  # -> 85000
print(employee_1 + employee_3)  # -> 100000

# ANOTHER EXAMPLE
print(len('test'))              # -> 4
print('test'.__len__())         # -> 4
# own Employee class` LEN method
print(employee_1.__len__())     # -> 11