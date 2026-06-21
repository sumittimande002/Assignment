# # Question 1: Student Batch Management System (Basic)

# ### Problem Statement

# A training institute wants to maintain the details of students enrolled in different batches.

# Create a class named **Student**.
class Student:

    Institute_Name = "ABC Traning Institute"

    def __init__(self,Student_ID,Student_Name,Course):
        self.Student_ID = Student_ID
        self.Student_Name = Student_Name
        self.Course = Course
    
    def display_student(self):
        print("----------------------------------")
        print("         Student Details ")
        print("----------------------------------")
        print(f"Institute Name : {self.Institute_Name}")
        print(f"Student ID     : {self.Student_ID}")
        print(f"Student Name   : {self.Student_Name}")
        print(f"Course         : {self.Course}")


s1 = Student(101,"Kunal","Java")
s1.display_student()

s2 = Student(102,"Omkar","CSS")
s2.display_student()

s3 = Student(103,"Sumit","Pthon")
s3.display_student()

s4 = Student(104,"Darshan","Java")
s4.display_student()

s5 = Student(105,"Kavita","JS")
s5.display_student()

# Use the following variables:

# ### Instance Variables

# * Student ID
# * Student Name
# * Course

# ### Class Variable

# * Institute Name = "ABC Training Institute"

# Create a method named **display_student()** to display all the information.

# ### Requirements

# * Create **5 Student objects**.
# * Display the details of all students.
# * The institute name should be common for every student.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Student Details
# -----------------------------------------

# Institute Name : ABC Training Institute

# Student ID     : 101
# Student Name   : Rahul
# Course         : Python Full Stack
