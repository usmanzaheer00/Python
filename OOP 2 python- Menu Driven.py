class employe:
    def calculate_salary(self):
        print(f"Salary Of Employee : {0}")

class manager(employe):
    def __init__ (self,salary,bonus):
        self.salary = salary
        self.bonus = bonus
        
    def calculate_salary(self):
        m_salary = self.salary + self.bonus
        print(f"Manager Salary : {m_salary}")
        
class developer(employe):
    def __init__ (self,hourly_wage,no_hour):
        self.hourly_wage = hourly_wage
        self.no_hour = no_hour
    def calculate_salary(self):
        d_salary = self.hourly_wage * self.no_hour
        print(f"Developer Salary : {d_salary}")
        
class designer(employe):
    def __init__ (self,salary):
        self.salary = salary
    def calculate_salary(self):
        print(f"Designer Salary : {self.salary}")
        

while True:
    inp = int(input(f" Enter 1 for Manager\n Enter 2 for Developer\n Enter 3 for Designer\n Enter 0 to Exit\n"))
    print(f"_________________________________________________________________")
    match inp:
        case 0:
            print(f"____________________________________________________________")
            print(f"THANK YOU!")
            print(f"____________________________________________________________")
            break
        case 1:
            m_salary = int(input(f"Enter manager's salary :"))
            bonus = int(input(f"Enter Bonus : "))
            mg = manager(m_salary,bonus)
            print(f"____________________________________________________________")
            mg.calculate_salary()
            print(f"____________________________________________________________")

            
        case 2:
            hourly_wage = int(input(f"Enter developer's hourly wage :"))
            no_hour = int(input(f"Enter today's number of hours worked :"))
            dv = developer(hourly_wage,no_hour)
            print(f"____________________________________________________________")
            dv.calculate_salary()
            print(f"____________________________________________________________")

        case 3:
            salary = int(input(f"Enter designer's salary :"))
            ds = designer(salary)
            print(f"____________________________________________________________")
            ds.calculate_salary()        
            print(f"____________________________________________________________")

            
        case _:
            print(f"____________________________________________________________")
            print("Wrong Input\n")         
            print(f"____________________________________________________________")
