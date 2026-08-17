class Student:
    # Method 1: Display student details
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    # Method 2: Set student details
    def set_details(self, name, age):
        self.name = name
        self.age = age


# Creating an object
student1 = Student()

# Calling the method
student1.set_details("Moynak", 18)

# Calling another method
student1.display()