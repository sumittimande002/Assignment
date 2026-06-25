# # Question 4: Notification System (Method Overriding)

# ### Problem Statement

# A software application sends notifications through different communication channels.

# Create a **Parent Class** named **Notification** with the method:

# * send_notification()

class Notification:
    def send_notification():
        pass

# Create the following child classes:

# * EmailNotification
# * SMSNotification
# * WhatsAppNotification

class EmailNotification(Notification):
 def send_notification(self):
        print("------------------------")
        print("   Notification Details ")
        print("-------------------------")
        print("Email Notification.")
        print("Status :  Successfully")


class SMSNotification(Notification) :
    def send_notification(self):
        print("---------------------------")
        print("Type   :  SMS Notification.")
        print("Status :  Successfully")


class WhatsAppNotification(Notification):
    def send_notification(self):
        print("-------------------------")
        print("Whats Notification.")
        print("Status :  Successfully")


e = EmailNotification()
e.send_notification()

w = WhatsAppNotification()
w.send_notification()

s = SMSNotification()
s.send_notification()

# Each child class should override the method and display the notification details.

# ### Requirements

# * Create objects for all notification types.
# * Call the same method for each object.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Notification Details
# -----------------------------------------

# Notification Type : Email
# Status            : Sent Successfully

# -----------------------------------------

# Notification Type : SMS
# Status            : Sent Successfully

# -----------------------------------------

# Notification Type : WhatsApp
# Status            : Sent Successfully
