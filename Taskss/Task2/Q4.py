#  Question 4: Hospital Patient Registration System (Intermediate)

# ### Problem Statement

# A hospital wants to register patients at the time of admission.

# Create a class named **Patient**.

class Patient:
    def __init__(self,Patient_ID,Patient_Name,Age,Disease,Consultiation_Fee):
        self.Patient_ID = Patient_ID
        self.Patient_Name = Patient_Name
        self.Age = Age
        self.Disease = Disease
        self.Consultiation_Fee = Consultiation_Fee

    def display_patient(self):
        print("----------------------------------------")
        print("           Patient Details")
        print("----------------------------------------")
        print(f"Patient Id          : {self.Patient_ID}")
        print(f"Patient Name        : {self.Patient_Name}")
        print(f"Age                 : {self.Age}")
        print(f"Disease             : {self.Disease}")

    def display_fees(self):
        print(f"Consultiation Fees  : {self.Consultiation_Fee}")

p1 = Patient(101,"Rakesh",23,"Dangu",500)
p1.display_patient()
p1.display_fees()



p2 = Patient(102,"Rakesh",23,"Dangu",500)
p2.display_patient()
p2.display_fees()


p3 = Patient(103,"Rakesh",23,"Dangu",500)
p3.display_patient()
p3.display_fees()


p4 = Patient(104,"Rakesh",23,"Dangu",500)
p4.display_patient()
p4.display_fees()


p5 = Patient(105,"Rakesh",23,"Dangu",500)
p5.display_patient()
p5.display_fees()

# Initialize the following information using the constructor:

# * Patient ID
# * Patient Name
# * Age
# * Disease
# * Consultation Fee

# Create the following methods:

# * **display_patient()**
# * **display_fee()**

# ### Requirements

# * Create **5 Patient objects**.
# * Display patient details.
# * Display the consultation fee.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Patient Details
# -----------------------------------------

# Patient ID          : P101
# Patient Name        : Ramesh
# Age                 : 35
# Disease             : Viral Fever
# Consultation Fee    : ₹700
# `