class office : 
    def __init__ (self , name , employees) :
        self.name = name 
        self.employees = []
    employeesNum = 0 

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.emp_id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        office.employeesNum += 1

    def fire(self, empId):
        self.employees = [emp for emp in self.employees if emp.emp_id != empId]
        office.employeesNum -= 1

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward

    def check_lateness(self, empId, moveHour, targetHour=9):
        emp = self.get_employee(empId)
        if emp:
            is_late = office.calculate_lateness(targetHour, moveHour, emp.distanceToWork, emp.car.velocity)
            if is_late:
                self.deduct(empId, 10)
            else:
                self.reward(empId, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        time_needed = distance / velocity
        arrival_time = moveHour + time_needed
        return arrival_time > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num
 