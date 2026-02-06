from car import Car
from employee import Employee
from office import office
from open import open

def main():
    # Create Car
    car1 = Car("Fiat128", fuelRate=50, velocity=100)

    # Create Employee
    emp1 = Employee(emp_id=1, name="Samy", money=1000, mood="happy", healthRate=100,
                    car=car1, email="samy@iti.org", salary=5000, distanceToWork=20)

    # Create Office
    iti_office = office("ITI Smart Village")
    iti_office.hire(emp1)

    # Test methods
    emp1.sleep(6)
    emp1.eat(2)
    emp1.buy(1)
    emp1.work(9)
    emp1.drive(distance=20, velocity=120)
    emp1.refuel(30)
    emp1.send_mail("manager@iti.org", "Report", "I am on time today.")

    iti_office.check_lateness(emp1.emp_id, moveHour=8)
    print("Employees:", iti_office.get_all_employees())
    print("Total Employees:", office.employeesNum)

    # Open random website
    open()

if __name__ == "__main__":
    main()
