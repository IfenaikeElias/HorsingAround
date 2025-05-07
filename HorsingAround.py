from typing import Optional, List
class  Employee:
    raise_amount = 1.04

    def __init__(self, first_name, last_name, payment, id):
        self.first = first_name
        self.last = last_name
        self._id = id
        self.email =  first_name + "." + last_name + "@email.com"
        self.pay = payment

    def __repr__(self):
        return f"Employee Name: {self.first} {self.last} ID: {self._id} level: {self.__class__.__name__}"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def HourlyEmployee(cls, first_name, last_name, hourly_rate, id):
        return cls(first_name, last_name, hourly_rate, id)

    @classmethod
    def WeeklyEmployee(cls, first_name, last_name, weekly_salry, id):
        
        return cls(first_name, last_name, weekly_salry, id)

    @classmethod
    def SalaryEmployee(cls, first_name, last_name, anual_salary, id):
        return cls(first_name, last_name, anual_salary, id)
        
class Developer(Employee):
    
    def __init__(self, first_name, last_name, payment, id,  prog_lang):
        super().__init__(first_name, last_name, payment, id)
        self.language =  prog_lang
        
class Manager(Employee):
    def __init__(self, first_name, last_name, payment, id, employees: Optional[List[Employee]]= None):
        super().__init__(first_name, last_name, payment, id)
        if employees is None:
            self._employees  =  []
        elif isinstance(employees, Employee):
            self._employees = [employees]
        elif isinstance(employees, list):
            if all(isinstance(emp, Employee) for emp in employees):
                self._employees =  employees
            else:
                raise ValueError("All elements in 'employees' must be of type 'Employee' ")
        else:
            raise ValueError("The 'employee' arguement must be an Employee or list of Employee objects")

    def add_employee(self, employee):
        if isinstance(employee, Employee) and employee not in self._employees:
            self._employees.append(employee)
        
    def remove_employee(self, employee):
        if employee in self._employees:
            self._employees.remove(employee)
    def check_employees(self):
        if self._employees:
            for emp in self._employees:
                print(f"{emp.fullname()}")
        else:
            print("No employees under management.")


def test_employee_class():
    # Test basic Employee functionality
    emp1 = Employee("John", "Doe", 50000, 101)
    
    assert emp1.first == "John"
    assert emp1.last == "Doe"
    assert emp1.email == "John.Doe@email.com"
    assert emp1.pay == 50000
    assert emp1.fullname() == "John Doe"
    
    # Test apply raise functionality
    emp1.apply_raise()
    assert emp1.pay == 52000  # 50000 * 1.04
    
    print("Employee class tests passed!")

def test_developer_class():
    # Test Developer subclass functionality
    dev = Developer("Alice", "Smith", 60000, 109,  "Python")
    
    assert dev.first == "Alice"
    assert dev.language == "Python"
    assert dev.pay == 60000
    assert dev.fullname() == "Alice Smith"
    
    # Test raise functionality
    dev.apply_raise()
    assert dev.pay == 62400  # 60000 * 1.04
    
    print("Developer class tests passed!")

def test_manager_class():
    # Test Manager subclass functionality with no employees
    manager = Manager("Bob", "Johnson", 80000, "HR101")
    assert manager.first == "Bob"
    assert manager.pay == 80000
    assert manager.fullname() == "Bob Johnson"
    
    # Check initial employee list is empty
    manager.check_employees()  # Expected: No employees under management.
    
    # Add employee and check again
    emp1 = Employee("John", "Doe", 50000, 101)
    manager.add_employee(emp1)
    manager.check_employees()  # Expected: John Doe
    
    # Remove employee and check again
    manager.remove_employee(emp1)
    manager.check_employees()  # Expected: No employees under management.
    
    # Test Manager with employee list
    emp2 = Employee("Jane", "Doe", 55000, 102)
    manager_with_employees = Manager("Sarah", "Connor", 100000, [emp1, emp2])
    manager_with_employees.check_employees()  # Expected: John Doe, Jane Doe
    
    print("Manager class tests passed!")

def test_factory_methods():
    # Test factory methods: HourlyEmployee, WeeklyEmployee, SalaryEmployee
    hourly_emp = Employee.HourlyEmployee("Mark", "Zuckerberg", 30, "H112")  # hourly rate = 30
    assert hourly_emp.first == "Mark"
    assert hourly_emp.pay == 30
    assert hourly_emp.__class__.__name__ == "Employee"
    
    weekly_emp = Employee.WeeklyEmployee("Elon", "Musk", 1500, "W114")  # weekly salary = 1500
    assert weekly_emp.first == "Elon"
    assert weekly_emp.pay == 1500
    assert weekly_emp.__class__.__name__ == "Employee"
    
    salary_emp = Employee.SalaryEmployee("Bill", "Gates", 120000, "OB13")  # annual salary = 120000
    assert salary_emp.first == "Bill"
    assert salary_emp.pay == 120000
    assert salary_emp.__class__.__name__ == "Employee"
    
    print("Factory methods tests passed!")

# Running all tests
def run_tests():
    test_employee_class()
    test_developer_class()
    test_manager_class()
    test_factory_methods()

# Execute the tests
run_tests()
