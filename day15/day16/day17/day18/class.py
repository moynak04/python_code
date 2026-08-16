class Student:

    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)


# Creating objects
student1 = Student(int(input("Enter name: ")), int(input("Enter age: ")), input("Enter branch: "))
student2 = Student(int(input("Enter name: ")), int(input("Enter age: ")), input("Enter branch: "))

# Calling the method
student1.display_details()

print()

student2.display_details()