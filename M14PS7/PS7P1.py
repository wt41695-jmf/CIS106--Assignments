# Employee class with bonus method

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def full_name(self):
        return self.first_name + " " + self.last_name

    def compute_bonus(self, bonus_rate):
        bonus = self.salary * bonus_rate
        return bonus


def main():
    first = input("Enter employee first name: ")
    last = input("Enter employee last name: ")
    salary = float(input("Enter employee salary: "))
    rate = float(input("Enter bonus rate as a decimal, for example .10 for 10%: "))

    employee1 = Employee(first, last, salary)

    bonus = employee1.compute_bonus(rate)

    print("Employee name:", employee1.full_name())
    print("Salary: $", format(employee1.salary, ",.2f"))
    print("Bonus: $", format(bonus, ",.2f"))


main()
