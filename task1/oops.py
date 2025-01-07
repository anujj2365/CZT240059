# Student Class
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

# Example
student1 = Student("Anuj", 19, [78, 85, 92])
student1.display_details()
print(f"Average Grade: {student1.calculate_average()}")
