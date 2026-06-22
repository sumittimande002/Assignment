
# # Question 1: Student Grade Management System (Basic)

# ### Problem Statement

# A training institute wants to evaluate student performance.

# Create a class named **Student**.

class Student:
    def __init__(self, student_id, student_name, marks):
        self.student_id = student_id
        self.student_name = student_name
        self.marks = marks

    def display_student(self):
        print(f"Student ID   : {self.student_id}")
        print(f"Student Name : {self.student_name}")
        print(f"Marks        : {self.marks}")

    @classmethod
    def college_name(self):
        print("-----------------------------------")
        print("       Student Details")
        print("-----------------------------------")
        print("College Name : ABC Training Institute")

    @staticmethod
    def pass_marks():
        print("Pass Marks   : 35")

s1 = Student(101,"Rahul",60)
s1.college_name()
s1.display_student()
s1.pass_marks()


# Store the following details:

# * Student ID
# * Student Name
# * Marks

# Create the following methods:

# ### Instance Method

# **display_student()**

# * Display student details.

# ### Class Method

# **college_name()**

# Display:

# ```text
# ABC Training Institute
# ```

# ### Static Method

# **pass_marks()**

# Display:

# ```text
# Pass Marks : 35
# ```

# ### Requirements

# * Create **5 Student objects**.
# * Call all three methods.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Student Details
# -----------------------------------------

# College Name : ABC Training Institute

# Student ID   : 101
# Student Name : Rahul
# Marks        : 85

# Pass Marks   : 35
# `