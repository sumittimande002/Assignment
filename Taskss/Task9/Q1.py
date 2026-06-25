# # Question 1: Student Information System (Public Members)

# ### Problem Statement

# A college wants to maintain student information that can be accessed from anywhere in the program.

# Create a class named **Student** with the following **Public Attributes**:

# * Student ID
# * Student Name
# * Course
# * Marks

class Student:
    def __init__(self,Student_ID,Student_Name,Course,Marks) :
        self.Student_ID = Student_ID
        self.Student_Name = Student_Name
        self.Course = Course
        self.Marks = Marks

    def display_student_details(self):
        print(f"Student Id   : {self.Student_ID}")
        print(f"Student Name : {self.Student_Name}")
        print(f"Course       : {self.Course}")
        print(f"Marks        : {self.Marks}")

s = Student(101,"Rahul","Python",50)
s.display_student_details()


# Create a public method named:

# * display_student_details()

# ### Requirements

# * Create an object of the class.
# * Access all attributes directly outside the class.
# * Display student details.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Student Details
# -----------------------------------------

# Student ID      : ST101
# Student Name    : Sai Ram
# Course          : Python Full Stack
# Marks           : 92
# ```
