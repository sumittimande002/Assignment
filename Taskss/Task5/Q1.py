# # Question 1: Student Result Management System (Basic)

# ### Problem Statement

# A training institute wants to securely store student marks.

# Create a class named **Student**.

# Store the following information:

# * Student ID
# * Student Name
# * Private Variable: **Marks**

class Student:
    def __init__(self, student_id, student_name, marks):
        self.student_id = student_id
        self.student_name = student_name
        self.__marks = marks  

    def set_marks(self, marks):
        self.__marks = marks 

    def get_marks(self):
        return self.__marks 

    def display_student(self):
        print("-----------------------------------------")
        print("         Student Details")
        print("-----------------------------------------")
        print(f"Student ID      : {self.student_id}")
        print(f"Student Name    : {self.student_name}")
        print(f"Marks           : {self.get_marks()}")
    
s1 = Student(101, "Rahul", 88)
s1.display_student()

s2 = Student(102, "Priya", 92)
s2.display_student()

s3 = Student(103, "Amit", 75)
s3.display_student()

s4 = Student(104, "Sneha", 85)
s4.display_student()

s5 = Student(105, "Rohit", 90)
s5.display_student()



# Create the following methods:

# * **set_marks()**
# * **get_marks()**
# * **display_student()**

# ### Requirements

# * Create **5 Student objects**.
# * Marks should not be accessed directly.
# * Update the marks using the setter method.
# * Display the marks using the getter method.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Student Details
# -----------------------------------------

# Student ID      : 101
# Student Name    : Rahul
# Marks           : 88
