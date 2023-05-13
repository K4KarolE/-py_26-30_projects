
class Employee:

    number_of_employee = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, email_private, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email_comp = first_name + '.' + last_name + 'company.com'
        self.email_private = email_private

        Employee.number_of_employee +=1     #!
    
    def fullname(self):   
        return '{} {}'.format(self.first_name, self.last_name)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)      # without self or Employee_Snd will drop an error
        # self.pay = int(self.pay * self.raise_amount)    

        
employee_1 = Employee('Bobby','Black', 'blackmoonhunter@darkside.com', 40000)
employee_2 = Employee('Peggy','Wanker', 'bestwife@couch.com', 45000)

print(Employee.number_of_employee) # created 2 employees -> number_of_employee = 2



