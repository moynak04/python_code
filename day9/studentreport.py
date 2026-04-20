# Student data (nested dictionary)
students = {
    "Harry": {"Math": 88, "Science": 76, "English": 90},
    "Ron": {"Math": 70, "Science": 65, "English": 72},
    "Hermione": {"Math": 98, "Science": 95, "English": 100},
    "Draco": {"Math": 60, "Science": 55, "English": 58}
}

report = {}

# Function to assign grade
def get_grade(avg):
    if avg >= 90:
        return "Outstanding"
    elif avg >= 80:
        return "Exceeds Expectations"
    elif avg >= 70:
        return "Acceptable"
    else:
        return "Fail"

# Processing data
for name, marks in students.items():
    total = sum(marks.values())
    avg = total / len(marks)
    
    report[name] = {
        "Total": total,
        "Average": round(avg, 2),
        "Grade": get_grade(avg)
    }

# Finding topper
topper = max(report, key=lambda x: report[x]["Average"])

# Output
print("Student Report:\n")
for student, details in report.items():
    print(f"{student}: {details}")

print("\nTopper:", topper)