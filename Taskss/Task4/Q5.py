# # Question 5: Movie Ticket Booking System (Advanced)

# ### Problem Statement

# An online movie ticket booking company wants to automate ticket booking.

# Create a class named **MovieTicket**.

class MovieTicket:
    def __init__(self,Booking_ID,Customer_Name,Movie_Name,Number_of_Tickets,Ticket_Price):
        self.Booking_ID = Booking_ID
        self.Customer_Name = Customer_Name
        self.Movie_Name = Movie_Name
        self.Number_of_Ticket = Number_of_Tickets
        self.Ticket_Price = Ticket_Price
    
    def display_booking(self):
        print(f"Booking ID       : {self.Booking_ID}")
        print(f"Customer Name    : {self.Customer_Name}")
        print(f"Movie Name       : {self.Movie_Name}")
        print(f"Number of Ticket : {self.Number_of_Ticket}")
        print(f"Ticket Price     : {self.Ticket_Price}")

    def calculate_bill(self):
        total_amount = self.Number_of_Ticket * self.Ticket_Price
        print(f"Total Bill       : {total_amount}")

    @classmethod
    def theatre_name(cls):
        
        print("-------------------------------------")
        print("          Booking Details")
        print("-------------------------------------")
        print("Theatre Name     : PVR Cinemas")

    @staticmethod
    def booking_Rules():
        print("        Booking Rules")
        print("Carry a valid ID proof.")
        print("Tickets cannot be cancelled after the show starts.")
        print("Entry is not allowed after 30 minutes from the movie start time.")

m1 = MovieTicket(1001,"Arjun","Shera",2,450)
m1.theatre_name()
m1.display_booking()
m1.calculate_bill()
m1.booking_Rules()

# Store

# * Booking ID
# * Customer Name
# * Movie Name
# * Number of Tickets
# * Ticket Price

# Create the following methods.

# ### Instance Method

# **display_booking()**

# Display booking information.

# ### Instance Method

# **calculate_bill()**

# Calculate

# ```text
# Total Amount = Number of Tickets × Ticket Price
# ```

# ### Class Method

# **theatre_name()**

# Display

# ```text
# PVR Cinemas
# ```

# ### Static Method

# **booking_rules()**

# Display the following rules:

# * Carry a valid ID proof.
# * Tickets cannot be cancelled after the show starts.
# * Entry is not allowed after 30 minutes from the movie start time.

# ### Requirements

# * Create **5 MovieTicket objects**.
# * Display booking details.
# * Calculate the total bill.
# * Display theatre name.
# * Display booking rules.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Movie Ticket Details
# -----------------------------------------

# Theatre Name      : PVR Cinemas

# Booking ID        : B101
# Customer Name     : Sai
# Movie Name        : Leo
# Tickets           : 3
# Ticket Price      : ₹250

# Total Amount      : ₹750

# Booking Rules

# • Carry a valid ID proof.

# • Tickets cannot be cancelled after the show starts.

# • Entry is not allowed after 30 minutes from the movie start time.

