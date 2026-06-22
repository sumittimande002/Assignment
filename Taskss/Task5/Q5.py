# Question 5: Hospital Patient Record System (Advanced)

# ### Problem Statement

# A hospital wants to protect confidential patient records.

# Create a class named **Patient**.

# Store:

# * Patient ID
# * Patient Name
# * Age
# * Disease

class Patient:
    def __init__(self,Patient_ID,Patient_Name,Age,Disease,Medical_History,Consultation_fee):
        self.Patient_ID = Patient_ID
        self.Patient_Name = Patient_Name
        self.Age = Age
        self.Disease = Disease
        self.__Medical_History = Medical_History
        self.__Consultation_fee = Consultation_fee

    def __calculate_discount(self):
        if self.__Consultation_fee >= 1000:
            discount = self.__Consultation_fee *0.10
        else :
            discount = 0
        return discount

    def set_medical_history(self,Medical_History):
        self.__Medical_History = Medical_History

    def get_medical_history(self):
        print(f"Medical History   : {self.__Medical_History}")

    def display_patient(self):
        print("-----------------------------------------")
        print("      Patient Details")
        print("-----------------------------------------")
        print(f"Patient ID        : {self.Patient_ID}")
        print(f"Patient Name      : {self.Patient_Name}")
        print(f"Age               : {self.Age}")
        print(f"Disease           : {self.Disease}")

    def final_bill(self):
        discount = self.__calculate_discount()
        final_amount = self.__Consultation_fee - discount
        print(f"Consultation Fee  : {self.__Consultation_fee}")
        print(f"Discount          : {discount}")
        print(f"Final Bill        : {final_amount}")

p1 = Patient("P101","Ramesh",42,"Viral Fever","Available",1500)
p1.display_patient()
p1.get_medical_history()
p1.final_bill()

p2 = Patient("P102","Suresh",35,"Bacterial Infection","Available",2000)
p2.display_patient()
p2.get_medical_history()
p2.final_bill()

p3 = Patient("P103","Priya",28,"Allergy","Not Available",800)
p3.display_patient()
p3.get_medical_history()
p3.final_bill()

p4 = Patient("P104","Ramesh",42,"Viral Fever","Available",1500)
p4.display_patient()
p4.get_medical_history()
p4.final_bill()

p5 = Patient("P105","Ramesh",42,"Viral Fever","Available",1500)
p5.display_patient()
p5.get_medical_history()
p5.final_bill()


# Private Variables

# * Medical History
# * Consultation Fee

# Private Method

# * **calculate_discount()**

# Rules

# * If Consultation Fee is greater than ₹1,000, provide a 10% discount.
# * Otherwise, no discount.

# Public Methods

# * **set_medical_history()**
# * **get_medical_history()**
# * **display_patient()**
# * **final_bill()**

# ### Requirements

# * Create **5 Patient objects**.
# * Medical history should never be accessed directly.
# * Consultation fee should be processed using the private method.
# * Display the final bill after discount.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Patient Details
# -----------------------------------------

# Patient ID          : P101
# Patient Name        : Ramesh
# Age                 : 42
# Disease             : Viral Fever

# Medical History     : Available

# Consultation Fee    : ₹1,500
# Discount            : ₹150

# Final Bill          : ₹1,350
# `