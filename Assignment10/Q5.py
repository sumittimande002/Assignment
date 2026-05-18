# 5. using *args and *kwargs for API request builder

def apiRequest(endpoint,*args,**keyargs):
    print("End Point : ",endpoint)
    print("*Args : ",args)
    print("**Key Args : ",keyargs)


apiRequest("Toto",4040,500, fname = "Sumit",Lname = "Timande")