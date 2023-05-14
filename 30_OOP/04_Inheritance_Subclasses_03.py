''' Adding more attributes for the subclass '''

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

    def __init__(self, first_name, last_name, email_private, pay, programming_lang):    # adding prog._lang which was not part of the Employee class
        super().__init__(first_name, last_name, email_private, pay)                     # Employee class` attributes (apart from self)       
        # Employee.__init__(self, first_name, last_name, email_private, pay)            # same result as the previous line
        
        self.programming_lang = programming_lang


class Manager(Employee):

    def __init__(self, first_name, last_name, email_private, pay, employees=None): # why None? - do not want to pass a mutable data type (like list) as default argument
        super().__init__(first_name, last_name, email_private, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('- ', emp.fullname())


dev_1 = Developer('Bobby','Black', 'blackmoonhunter@darkside.com', 40000, 'Python')
dev_2 = Developer('Peggy','Wanker', 'bestwife@couch.com', 45000, 'Java')
employee_3 = Employee('Don','Tom', 'don@tom.com', 60000)
mang_1 = Manager('Bambi','Dambi', 'temtere@tom.com', 80000, [dev_1])

print(mang_1.email_comp)
mang_1.add_employee(dev_2)
mang_1.add_employee(employee_3)
mang_1.remove_employee(dev_1)
mang_1.print_employees()
print('\n\n')


''' Relation check '''
print(isinstance(mang_1, Manager))      # True
print(isinstance(mang_1, Employee))     # True
print(isinstance(mang_1, Developer))    # False

print('\n\n')

print(issubclass(Manager, Employee))    # True
print(issubclass(Manager, Developer))   # False

