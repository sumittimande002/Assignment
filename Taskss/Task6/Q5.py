# Question 5: Hospital Management System (Advanced)

# ### Problem Statement

# A multi-specialty hospital wants to generate consultation details for different departments.

# Create an **Abstract Class** named **Doctor**.

# Create the following abstract methods:

# * doctor_details()
# * consultation_fee()
# * available_timings()
# * treatment()

# Create the following child classes:
from abc import ABC ,abstractmethod

class Doctor(ABC):
    @abstractmethod
    def doctor_details():
        pass

    @abstractmethod
    def consultation_fee():
        pass

    @abstractmethod
    def available_timings():
        pass

    @abstractmethod
    def treatment():
        pass

# * Cardiologist
class Cardiologist(Doctor):
    def doctor_details(self):
        print("--------------------------------")
        print("       Doctor Details ")
        print("--------------------------------")
        print(f"Department      : Cardiologist")

    def consultation_fee(self,fees):
        print(f"Fees            : {fees}")

    def available_timings(self,time):
        print(f"Available Time  : {time}")

    def treatment(self):
        print("Treatment        : Heart Diseases")
     

class Neurologist(Doctor):
    def doctor_details(self):
        print("--------------------------------")
        print("       Doctor Details ")
        print("--------------------------------")
        print(f"Department      : Neurologist")

    def consultation_fee(self,fees):
        print(f"Fees            : {fees}")

    def available_timings(self,time):
        print(f"Available Time  : {time}")

    def treatment(self):
        print("Treatment        : Heart Diseases")

class Orthopedic(Doctor):
    def doctor_details(self):
        print("--------------------------------")
        print("       Doctor Details ")
        print("--------------------------------")
        print(f"Department      : Orthopedic")

    def consultation_fee(self,fees):
        print(f"Fees            : {fees}")

    def available_timings(self,time):
        print(f"Available Time  : {time}")

    def treatment(self):
        print("Treatment        : Heart Diseases")

n = Neurologist()
o = Orthopedic()
c = Cardiologist()
n.doctor_details()
n.consultation_fee(500)
n.available_timings(10)
n.treatment()


o.doctor_details()
o.consultation_fee(5500)
o.available_timings(10)
o.treatment()

c.doctor_details()
c.consultation_fee(1500)
c.available_timings(10.05)
c.treatment()
# * Neurologist
# * Orthopedic

# Each department should implement the abstract methods differently.

# ### Requirements

# * Create one object for each department.
# * Display doctor details.
# * Display consultation fee.
# * Display available timings.
# * Display treatment specialization.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Doctor Details
# -----------------------------------------

# Department          : Cardiology

# Doctor Name         : Dr. Sharma

# Consultation Fee    : ₹1,500

# Available Time      : 10:00 AM - 2:00 PM

# Treatment           : Heart Diseases

# -----------------------------------------

# Department          : Neurology

# Doctor Name         : Dr. Rao

# Consultation Fee    : ₹1,800

# Available Time      : 2:00 PM - 6:00 PM

# Treatment           : Brain & Nervous System Disorders
# ```