#  Question 1: Student Admission System (Basic)

# ### Problem Statement

# A training institute wants to automate the student admission process.

# Create a class named **Student**.
class Student:
    def __init__(self,Student_ID,Student_Name,Course,Course_Fee):
        self.Student_ID = Student_ID
        self.Student_Name = Student_Name
        self.Course = Course
        self.Course_Fee = Course_Fee
    
    def display_student(self):
        print("-------------------------------------")
        print("         Student Details    ")
        print("-------------------------------------")
        print(f"Student ID      : {self.Student_ID}")
        print(f"Student Name    : {self.Student_Name}")
        print(f"Course          : {self.Course}")
        print(f"Course Fee      : {self.Course_Fee}")



s1 = Student(1001,"Sumit","Computer Sciance",40000)
s1.display_student()

s2 = Student(1002,"Rajuu","IT",80000)
s2.display_student()

s3 = Student(1003,"Vilas","ECE",30000)
s3.display_student()

s4 = Student(1004,"Rajesh","Computer Sciance and Engineering",45000)
s4.display_student()

# Initialize the following details using a **parameterized constructor**:

# * Student ID
# * Student Name
# * Course
# * Course Fee

# Create a method named **display_student()** to display all the student information.

# ### Requirements

# * Create **4 Student objects** using the constructor.
# * Display the details of all students.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Student Details
# -----------------------------------------

# Student ID      : 101
# Student Name    : Rahul
# Course          : Python Full Stack
# Course Fee      : ₹45,000
