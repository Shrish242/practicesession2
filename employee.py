class Employee:
    raise_amount = 2
    num_of_emp = 0
    
    def __init__(self, first, last, pay, mail):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = mail
        Employee.num_of_emp += 1


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
class Developer(Employee):
        raise_amt = 1.10


        def __init__(self, first ,last ,pay , pro_lang):
           mail = first + "." + last + "@" + "gmail.com"
           super().__init__(first , last ,pay , mail)
           self.pro_lang = pro_lang

class manager(Employee):
    def __init__(self, first ,last ,pay , employees = None):
          mail = first + "." + last + "@" + "gmail.com"
          super().__init__(first , last ,pay , mail )
          if employees is None:
                self.employees = []
          else:
           self.employees = Employee
            
    def add_employee(self , emp):
                if emp not in self.employees:
                    self.employees.append(emp)


    def remove_employee(self , emp):
                if emp in self.employees:
                    self.employees.remove(emp)
                    
    def print_emps(self):
                for emp in self.employees:
                    print("-->" , emp.fullname()) 
                           
dev_1 = Developer("Sam" , "Smith" , 18000 , "python")
dev_2 = Developer("Ram" , "Gayish" , 45000 , "rol")
mgr_1 = manager("John", "Doe", 100000)

mgr_1.add_employee(dev_1)
mgr_1.add_employee(dev_2)
mgr_1.print_emps()

                  


