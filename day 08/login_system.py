username= input("Enter your name: ")
password = (input("Enter your password: "))
if username!= "admin":
    print("username not found")
else: 
    if password == "python123":
        print("Login successful") 
    else:
        print("Incorrect password")   
