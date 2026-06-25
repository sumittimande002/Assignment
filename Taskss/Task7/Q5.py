# Question 5: Hospital Management System (Hybrid Inheritance)

# ### Problem Statement

# A hospital wants to manage doctor and patient information for generating medical reports.

# Create the following classes:

# **Person**

# Attributes:

# * Name
# * Age


class Person:   
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

    def person_details(self):
        print(f"Name: {self.Name}")
        print(f"Age: {self.Age}")

# Methods:

# * person_details()

# **Doctor** (inherits Person)

class Doctor(Person):
    def __init__(self,Name,Age,Doctor_ID,Specialization):
        Person.__init__(self,Name,Age)
        self.Doctor_ID = Doctor_ID
        self.Specialization = Specialization

    def doctor_details(self):
        self.person_details()
        print(f"Doctor ID   : {self.Doctor_ID}")
        print(f"Specility   : {self.Specialization}")




# Additional Attributes:

# * Doctor ID
# * Specialization

# Method:

# * doctor_details()

# **Patient** (inherits Person)

class Patient(Person):
    def __init__(self,Name, Age,Patient_ID,Disease):
        Person.__init__(self,Name, Age)
        self.Patient_ID = Patient_ID
        self.Disease = Disease
    
    def patient_details(self):
        print(f"Patient Name  : {self.Name}")
        print(f"Patient Age   : {self.Age}")
        print(f"Patient ID    : {self.Patient_ID}")
        print(f"Disease       : {self.Disease}")


# Additional Attributes:

# * Patient ID
# * Disease

# Method:

# * patient_details()

# **MedicalReport** (inherits Doctor and Patient)

# Additional Attribute:

class MedicalReport(Doctor, Patient):
    def __init__(self, Name, Age, Doctor_ID, Specialization, Patient_ID, Disease, Report_Status):
        Doctor.__init__(self, Name, Age, Doctor_ID, Specialization)
        Patient.__init__(self, Name, Age, Patient_ID, Disease)
        self.Report_Status = Report_Status

    def report_details(self):
        print("-----------------------------------------")
        print("Medical Report")
        print("-----------------------------------------")
        self.doctor_details()
        print()
        self.patient_details()
        print(f"Report Status : {self.Report_Status}")


m = MedicalReport("Dr. Sharma", 45, "D101", "Cardiology", "P501", "Heart Disease", "Completed")
m.report_details()


# * Report Status

# Method:

# * report_details()

# ### Requirements

# * Demonstrate **Hybrid Inheritance**.
# * Display doctor, patient, and report details.
# * Use constructors and `super()` wherever applicable.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Medical Report
# -----------------------------------------

# Doctor Name        : Dr. Sharma
# Doctor ID          : D101
# Specialization     : Cardiology

# Patient Name       : Ravi Kumar
# Patient ID         : P501
# Disease            : Heart Disease

# Report Status      : Completed
# ```


# Some Mistake is thare i will update it in next commit