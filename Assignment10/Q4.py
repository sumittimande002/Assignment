# 4. database connection class (inheritance + constructor overriding)

class DatabaseConnection:
    def __init__(self,host,port):
        self.host = host
        self.port = port

class MySQLDatabase(DatabaseConnection):
    def __init__(self, host, port, Username,Password):
        super().__init__(host,port)
        self.Username = Username
        self.Password = Password
    def methodMysql(self):
        print("MySql Database Connection ")
        print(f" Host : {self.host} \n Port Number : {self.port}  \n User Name : {self.Username} \n Password : {self.Password} \n")

class PostgreSQL(DatabaseConnection):
    def __init__(self, host, port,Username,Password):
        super().__init__(host, port)
        self.Username = Username
        self.Password = Password

    def MethodPost(self):
        print("PostgreSQL Database Connection")
        print(f" Host : {self.host} \n Port Number : {self.port}  \n User Name : {self.Username} \n Password : {self.Password} \n")

class MongoDB(DatabaseConnection):
    def __init__(self, host, port,Username, Password):
        super().__init__(host, port)
        self.Username = Username
        self.Password = Password

    def methodMongo(self):
        print("MongoDB Database Connection")
        print(f" Host : {self.host} \n Port Number : {self.port}  \n User Name : {self.Username} \n Password : {self.Password} \n")


# d = DatabaseConnection()
m = MySQLDatabase("link",442200,"Sumit","Wardha@123")
m.methodMysql()

p = PostgreSQL("Win",10022,"Rohit","Kukuu@123")
p.MethodPost()

mm = MongoDB("Linux",5000,"Ankur","Anukuu@123")
mm.methodMongo()