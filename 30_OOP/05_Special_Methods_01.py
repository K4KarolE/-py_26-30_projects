''' These special/magic methods allow us to emulate some built in behavior. '''
'''
How we implement operator overloading.

Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator + 
is used to add two integers as well as join two strings and merge two lists. It is achievable because ‘+’ operator is overloaded by int class and str class.
You might have noticed that the same built-in operator or function shows different behavior for objects of different classes, this is called Operator Overloading. 

print(1 + 2) -> 3
print('a'+'b') -> ab

https://www.geeksforgeeks.org/operator-overloading-in-python/
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

    def __repr__(self):         # __repr__ unambiguous representation of the object / used for logging, debugging / meant to be seen by developers
        return "Employee('{}','{}','{}')".format(self.first_name, self.last_name, self.pay)
    
    def __str__(self):        # __str__ more readable representation of an object / meant to be displayed for the end users
        return '{} - {}'.format(self.fullname(), self.email_comp)


employee_1 = Employee('Bobby','Black', 'blackmoonhunter@darkside.com', 40000)
employee_2 = Employee('Peggy','Wanker', 'bestwife@couch.com', 45000)
employee_3 = Employee('Don','Tom', 'don@tom.com', 60000)

print(employee_1)

print(repr(employee_1))
print(employee_1.__repr__())

print(str(employee_1))
print(employee_1.__str__())


'''
print(employee_1)   ->   <__main__.Employee object at 0x0000020AF89F9890>
'''

'''
def __repr__(self):      
    return "Employee('{}','{}','{}')".format(self.first_name, self.last_name, self.pay)

print(employee_1)   ->  Employee('Bobby','Black','40000')
'''

'''
def __repr__(self): 
        return "Employee('{}','{}','{}')".format(self.first_name, self.last_name, self.pay)
    
def __str__(self):     
    return '{} - {}'.format(self.fullname(), self.email_comp)

print(employee_1)   ->  Bobby Black - Bobby.Black@company.com
'''

print(1+2)
# INT and STR classes built in ADD methods -> we are able to create our own ADD method
print(int.__add__(1,2))
print(str.__add__('a','b'))