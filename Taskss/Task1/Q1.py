# Question 1: Student Profile System (Basic)

# ### Problem Statement

# A coaching institute wants to maintain the details of its students.

# Create a class named **Student**.
class Students:
    def __init__(self ,Student_id,Student_Name,Course_Name):
        self.Student_id = Student_id
        self.Student_Name = Student_Name
        self.Course_Name = Course_Name

    def display_deteils(self):
        print("---------------------------------------------")
        print("   Student Details     ")
        print("---------------------------------------------")
        print(f"Student id   : {self.Student_id}")
        print(f"Student Name : {self.Student_Name}")
        print(f"Course Name  : {self.Course_Name}")

s1 = Students(101 , "Rahul", "Full Stack Python Developer")
s1.display_deteils()
s2 = Students(102 , "Sumit", "Full Stack Python Developer")
s2.display_deteils()
s3 = Students(103 , "Raju", "Full Stack Java Developer")
s3.display_deteils()
        
# The class should store the following information:

# * Student ID
# * Student Name
# * Course Name

# Create a method named **display_details()** that displays all the student information.

# ### Requirements

# * Create **3 Student objects**.
# * Store different values for each student.
# * Display the details of all students.

# ### Expected Output Format

# ```
# ---------------------------------
# Student Details
# ---------------------------------

# Student ID      : 101
# Student Name    : Rahul
# Course          : Python Full Stack

# ---------------------------------

# Student ID      : 102
# Student Name    : Priya
# Course          : Java Full Stack

# ---------------------------------

# Student ID      : 103
# Student Name    : Sai
# Course          : Data Science
# ``