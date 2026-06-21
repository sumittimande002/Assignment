
# # Question 5: Hotel Room Booking System (Advanced)

# ### Problem Statement

# A hotel wants to generate booking details during room reservation.

# Create a class named **HotelBooking**.

class HostelBooking:
    def __init__(self,Booking_ID,Customer_Name,Room_Type,Number_of_Days,Rent_Per_Day):
        self.Booking_ID = Booking_ID
        self.Customer_Name = Customer_Name
        self.Room_Type = Room_Type
        self.Number_of_Days = Number_of_Days
        self.Rent_Per_Day = Rent_Per_Day
        

    def display_booking(self):
        print("------------------------------------")
        print("     Hostel Booking Details ")
        print("------------------------------------")
        print(f"Booking ID      : {self.Booking_ID}")
        print(f"Customer Name   : {self.Customer_Name}")
        print(f"Room Type       : {self.Room_Type}")
        print(f"Number Of Boys  : {self.Number_of_Days}")
        print(f"Rent Per Day    : {self.Rent_Per_Day}")

    def calculate_bill(self):
        total_bill = self.Number_of_Days * self.Rent_Per_Day
        print(f"Total Bill      : {total_bill}")


h1 = HostelBooking(100,"Rakesh","Normal",5,1500)
h1.display_booking()
h1.calculate_bill()


h1 = HostelBooking(101,"Rahul","Normal",2,2500)
h1.display_booking()
h1.calculate_bill()


h1 = HostelBooking(102,"Ramesh","Luxary",3,1000)
h1.display_booking()
h1.calculate_bill()


h1 = HostelBooking(103,"Kavii","Extra Luxary",3,2500)
h1.display_booking()
h1.calculate_bill()
# Initialize the following information using the constructor:

# * Booking ID
# * Customer Name
# * Room Type
# * Number of Days
# * Rent Per Day

# Create the following methods:

# * **display_booking()**
# * **calculate_bill()**

# The total bill should be calculated as:

# ```text
# Total Bill = Number of Days × Rent Per Day
# ```

# ### Requirements

# * Create **5 HotelBooking objects**.
# * Display booking details.
# * Display the total bill for each customer.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Hotel Booking Details
# -----------------------------------------

# Booking ID         : B101
# Customer Name      : Sai
# Room Type          : Deluxe
# Number of Days     : 3
# Rent Per Day       : ₹2,500

# Total Bill         : ₹7,500
# ```