## 1. Program to Create a Student Management System

# **Problem Statement:**
# Write a program to create a `Student` class. The constructor should initialize student
#  name, roll number, and marks. Create methods to display student details and calculate grade 
# based on marks.

class Students:
        def __init__(self,student_name,roll_number,marks):
            self.student_name = student_name
            self.roll_number =roll_number
            self.marks = marks

        def display(self):
            print("Name : ",self.student_name)
            print("Roll_Number : ",self.roll_number)
            # print("Grade : ",self.grade())
        
        def grade(self):
            if(self.marks >= 90):
                print("Grade : A")
            elif(self.marks >= 80):
                print("Grade : B")
            elif(self.marks >= 70):
                print("Grade : C")
            else:
                print("Grade : Fail")


s = Students("Sumit",101,75)
s.display()
s.grade()
s = Students("Ravi",102,95)
s.display()
s.grade()
s = Students("Anu",103,40)
s.display()
s.grade()

        