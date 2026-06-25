# # Question 4: Hospital Management System (Public, Protected & Private Members)

# ### Problem Statement

# A hospital wants to store doctor and patient information with different levels of access.

# Create a class named **Patient**.

# Create the following members:

class Patient:
    def __init__(self,patient_name,doctor_name,medical_history):
        self.patient_name = patient_name
        self._doctor_name = doctor_name
        self.__medical_history = medical_history


    def display(self):
        print(f"Patient Name    : {self.patient_name}")
        print(f"Doctor Name     : {self._doctor_name}")
        print(f"Medical History : {self.__medical_history}")


p = Patient("Guruuu","Dr Viruu","NA")
p.display()

print(p.patient_name)
print(p._doctor_name)
# print(p.__medical_history)

# ### Public

# * patient_name

# ### Protected

# * _doctor_name

# ### Private

# * __medical_history

# Create methods to display all information safely.

# ### Requirements

# * Demonstrate the accessibility of public, protected, and private members.
# * Explain which members can and cannot be accessed directly.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Patient Details
# -----------------------------------------

# Patient Name       : Arjun

# Doctor Name        : Dr. Sharma

# Medical History    : Diabetes
# ```
