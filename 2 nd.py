import csv

# Ask how many students to enter
n = int(input("Enter number of students: "))

# Prepare an empty list for student records
students = []

# Take input from user
for i in range(n):
    print(f"\nEnter details for student {i+1}:")
    name = input("Name: ")
    roll_no = input("Roll No: ")
    student_class = input("Class: ")
    marks = input("Marks: ")
    
    # Create a dictionary for the student and append to list
    student = {
        "Name": name,
        "Roll No": roll_no,
        "Class": student_class,
        "Marks": marks
    }
    students.append(student)

# File name to save the data
filename = "student_records.csv"

# Write to CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Roll No", "Class", "Marks"])
    writer.writeheader()
    writer.writerows(students)

print(f"\nCSV file '{filename}' created successfully with {n} records.")
