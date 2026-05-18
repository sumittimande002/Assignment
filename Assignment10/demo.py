# # 4. database connection class (inheritance + constructor overriding)

# # 4. Database Connection Class

# **Concepts Covered:**
# Inheritance, Constructor Overriding

# ### Problem Statement

# Most applications interact with databases such as MySQL, PostgreSQL, or MongoDB. To simplify connection management, developers often design base classes that provide common database connection functionality.

# Design a database connection system using inheritance.

# ### Requirements

# 1. Create a base class named `DatabaseConnection`.

class DatabaseConnection:
    def __init__(self,host,port):
        self.host = "Linux"
        self.port = 5000

# 2. The constructor should accept parameters such as:

#    * Host
#    * Port
# 3. Create a subclass named `MySQLDatabase`.

class MySQLDatabase(DatabaseConnection):
    def __init__(self, host, port,Username, Password):
        self.host = host
        self.port = port
        self.Username = Username 
        self.Password = Password

    def methodmysql(self):
        print(self.host)
        print(self.port)
        print(self.Username)
        print(self.Password)

m = MySQLDatabase("Linax",5000,"Sumit","Wardha@123") 
m.methodmysql()


# 4. Override the constructor in the subclass to include additional attributes such as:

#    * Username
#    * Password

# ### Implementation Guidelines

# * Use `super()` to call the parent constructor.
# * Demonstrate how child classes extend functionality from the base class.

# ### Expected Outcome

# The program should simulate connecting to a database using inherited properties and overridden constructors.


