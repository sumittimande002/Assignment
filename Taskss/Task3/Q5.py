# # Question 5: Hospital Management System (Advanced)

# ### Problem Statement

# A hospital wants to maintain patient records.

# Declare the following **Global Variable**

# ```python
# HOSPITAL_NAME = "City Care Hospital"
# ```

# Create a class named **Patient**.

class Patient:
    Hospital_Name = "City Care Hospital"
    Doctor_Name = "Dr Kivi"

    def __init__(self,Patient_ID,Patient_Name,Age,Disease,Consultation_fee):
        self.Patient_Name = Patient_Name
        self.Patient_ID = Patient_ID
        self.Age = Age 
        self.Disease = Disease
        self.Consultation_fee = Consultation_fee

    def display_patient(self):
        room_charge = 1000
        print(f"Patient Name     : {self.Patient_Name}")
        print(f"Patient ID       : {self.Patient_ID}")
        print(f"Age              : {self.Age}")
        print(f"Disease          : {self.Disease}")
        print(f"Room Charge      : {room_charge}")


    def display_hospital(self):
        print("          Hospital Details ")
        print(f"Hospital Name    :  {self.Hospital_Name}")
        print(f"Dr Name          :  {self.Doctor_Name}")
        print(f"Consultation Fee : {self.Consultation_fee}")


p1 = Patient(101,"Arvind",52,"Cancer",500)
p1.display_hospital()
p1.display_patient()

p2 = Patient(101,"Arvind",52,"Cancer",500)
p2.display_hospital()
p2.display_patient()

p3 = Patient(101,"Arvind",52,"Cancer",500)
p3.display_hospital()
p3.display_patient()

p4 = Patient(101,"Arvind",52,"Cancer",500)
p4.display_hospital()
p4.display_patient()

p5 = Patient(101,"Arvind",52,"Cancer",500)
p5.display_hospital()
p5.display_patient()


# Use:

# ### Instance Variables

# * Patient ID
# * Patient Name
# * Age
# * Disease
# * Consultation Fee

# ### Class Variable

# ```text
# Doctor Name = Dr. Sharma
# ```

# Create the following methods:

# * **display_patient()**
# * **display_hospital()**

# Inside **display_patient()**, create a **Local Variable**

# ```text
# Room Charge = ₹1000
# ```

# Display:

# * Hospital Name
# * Doctor Name
# * Patient Details
# * Consultation Fee
# * Room Charge

# ### Requirements

# * Create **5 Patient objects**.
# * Display all patient records.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Hospital Details
# -----------------------------------------

# Hospital Name      : City Care Hospital
# Doctor Name        : Dr. Sharma

# Patient ID         : P101
# Patient Name       : Ramesh
# Age                : 42
# Disease            : Viral Fever

# Consultation Fee   : ₹700
# Room Charge        : ₹1000
