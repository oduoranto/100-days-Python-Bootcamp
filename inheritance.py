class Worker:
    def __init__(self,name,date_of_birth, end_date) :
        self.name = name
        self.date_of_birth = date_of_birth

    def get_age(self):
        self.date_of_birth = date_of_birth   


    def collectPay(payment):
        return payment
    


class Employee(Worker):
    def __init__(self, name, date_of_birth, end_date,employee_id, hire_date):
        super().__init__(name, date_of_birth, end_date)
        self.employee_id = employee_id
        self.hire_date = hire_date


class SalariedEmployee(Employee):
    def __init__(self, name, date_of_birth, end_date, employee_id, hire_date, annual_salary, is_retired):
        super().__init__(name, date_of_birth, end_date, employee_id, hire_date)   
        self.annual_salary = annual_salary
        self.is_retired = is_retired

    def retire(is_retired):
        if(is_retired == True):
            print("Retire")
        else:
            print("Still young") 


anto = SalariedEmployee("Antony Oduor","11/10/2002", " ", 10001,"11/04/2002",300000.50, False)

print(f"Annual salary = $ {anto.annual_salary}")

            
