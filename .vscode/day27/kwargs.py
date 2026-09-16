def student_info(**kwargs):
    print(kwargs)


name = input("Enter your name: ")
age = int(input("Enter your age: "))
branch = input("Enter your branch: ")

student_info(name=name, age=age, branch=branch)