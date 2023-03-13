class student:    
    def __init__(self, name):    
        self.name = name    
    def __init__(self, name, email):    
        self.name = name    
        self.email = email    
         
# This line will generate an error    
#st = student("rahul")    
    
# This line will call the second constructor    
st = student("rahul", "rahul@gmail.com")    
print("Name: ", st.name)  
print("Email id: ", st.email)  