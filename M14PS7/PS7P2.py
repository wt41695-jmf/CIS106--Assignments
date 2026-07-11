# Student class to compute tuition

class Student:
    def __init__(self, first_name, last_name, district_code, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.credits = credits

    def compute_tuition(self):
        if self.district_code.upper() == "I":
            tuition = self.credits * 250.00
        else:
            tuition = self.credits * 500.00
        return tuition

    def full_name(self):
        return self.first_name + " " + self.last_name


def main():
    first = input("Enter student first name: ")
    last = input("Enter student last name: ")
    code = input("Enter district code, I for in-district or O for out-of-district: ")
    credits = float(input("Enter enrolled credits: "))

    student1 = Student(first, last, code, credits)

    tuition = student1.compute_tuition()

    print("Student name:", student1.full_name())
    print("District code:", student1.district_code)
    print("Credits:", student1.credits)
    print("Tuition owed: $", format(tuition, ",.2f"))


main()
