
# # Question 1: Student Marks Management System

# ### Problem Statement

# A college wants to develop a Student Marks Management System.

# Create a class named **Student** with the following attributes:
class InvalidDataTypeException :
    pass

class Student:
    # def __init__(self, student_id, student_name, marks):
    #     self.student_id = student_id
    #     self.student_name = student_name
    #     self.marks = marks

    def add_student(self):
            self.student_id = (input("Enter a Student Id : "))
            self.student_name = input("Enter a Studemt Name : ")
            try:
                self.marks = int(input("Enter a Student Marks : "))
                if self.marks < 0 or self.marks > 100:
                    raise InvalidDataTypeException("Marks should be between 0 and 100.")
            except ValueError:
                    print("Error: Invalid data type entered for marks.")
        

    def display_student(self):
        print("         Student Details             ")
        print("Student Id       :        ",self.student_id)
        print("Student Name     :        ",self.student_name)
        print("Student Marks    :     ",self.marks)
        # print("Student Grade : ",self.student_grade)

    def student_grade(self):
        if self.marks >= 90 :
            print("Student Grade        :  A")
        elif self.marks >=70 :
            print("Student Grade        :  B")
        elif self.marks >= 50:
            print("Student Grade        :  C")
        else:
            print("Student Grade        :  Fail")




s = Student()
s.add_student()
s.display_student()
s.student_grade()

# * Student ID
# * Student Name
# * Marks

# Create the following methods:

# * add_student()
# * display_student()
# * calculate_grade()




# Handle the following exceptions:

# * Marks less than 0
# * Marks greater than 100
# * Invalid data type entered for marks

# ### Requirements

# * Raise an exception for invalid marks.
# * Handle all exceptions gracefully.
# * Display student details and grade only if the data is valid.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Student Details
# -----------------------------------------

# Student ID      : ST101
# Student Name    : Sai Ram
# Marks           : 92
# Grade           : A
# ```

# **Invalid Input Example**

# ```text
# Error: Marks should be between 0 and 100.
# ```