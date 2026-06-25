# # Question 4: College Management System (Multiple Inheritance)

# ### Problem Statement

# A college wants to maintain student academic and sports records.

# Create the following classes:

# Class 1:

# Academic

class Academic:
    def __init__(self,Student_Name,Roll_Number,Marks):
        self.Student_Name = Student_Name
        self.Roll_Number = Roll_Number
        self.Marks = Marks

    def academic_details(self):
        print("-----------------------------------------")
        print("          Student Report    ")
        print("-----------------------------------------")
        print(f"Student Name    : {self.Student_Name}")
        print(f"Roll_Number     : {self.Roll_Number}")
        print(f"Marks           : {self.Marks}")
        

# Attributes:

# * Student Name
# * Roll Number
# * Marks

# Method:

# * academic_details()

# Class 2:

# Sports

class Sports:
    def __init__(self,Sport_Name,Medal_Won):
        self.Sport_Name = Sport_Name
        self.Medal_Won = Medal_Won

    def sport_details(self):
        print(f"Sport Name      : {self.Sport_Name}")
        print(f"Medal Won       : {self.Medal_Won}")

# Attributes:

# * Sport Name
# * Medal Won

# Method:

# * sports_details()

# Create a child class named:

# Student

class Student(Academic,Sports) :
    def __init__(self,Student_Name,Roll_Number,Marks,Sport_Name,Medal_Won,Grade):
        Academic.__init__(self,Student_Name,Roll_Number,Marks)
        Sports.__init__(self,Sport_Name,Medal_Won)
        self.Grade = Grade

    def student_report(self):
        self.academic_details()
        self.sport_details()
        print(f"Grade           : {self.Grade}")


s = Student("Ankur",101,70,"Swiming",2,"A")
s.student_report()
        

# Additional Attribute:

# * Grade

# Method:

# * student_report()

# ### Requirements

# * Demonstrate **Multiple Inheritance**.
# * Display complete student information.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Student Report
# -----------------------------------------

# Student Name     : Arjun
# Roll Number      : 21EC101
# Marks            : 92

# Sport            : Cricket
# Medal            : Gold

# Grade            : A+
# ```
