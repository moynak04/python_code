# Creating a class
class Student:

    # Constructor
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    # Method
    def display_details(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)

    def study(self):
        print(self.name, "is studying.")


# Creating objects
student1 = Student(input("Enter your name: "), int(input("Enter your age: ")), input("Enter your branch: "))

student2 = Student(input("Enter student 2's name: "), int(input("Enter student 2's age: ")), input("Enter student 2's branch: "))

                   

                   

# Calling methods
student1.display_details()
student1.study()

print()

student2.display_details()
student2.study()