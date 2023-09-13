class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if len(self.grades) == 0:
            return None
        return sum(self.grades) / len(self.grades)

# Create an instance of Student with name "Alice" and age 18
student = Student("Alice", 18)

# Print the name, age, and grades of the student
print(student.name)  # Alice
print(student.age)  # 18
print(student.grades)  # []

# Add some grades to the student
student.add_grade(90)
student.add_grade(85)
student.add_grade(95)

# Print the updated grades and the average grade of the student
print(student.grades)  # [90, 85, 95]
print(student.average_grade())  
