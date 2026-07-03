# concatenation
first_name = "vinayak"
last_name = "devappa"
full_name = first_name + " " + last_name
print("Full name is : " , full_name)

# repetition
message = " warning! "
print(message*10)

# string methods
print(message . upper()) # upper case
print (message . lower()) # lower case
print (message .strip()*2) # strip removes leading and trailing spaces
message =  "This is a warning! "
print(message .replace("warning" , "Error")) # replace  method

Name = ''' vinayak wished "good morning" to vishwa
            vishwa replied and said "good morning" 
           ''' # use triple ''' for multiple lines 
print (Name)
print (len(Name)) #length
# accessing string characters 
a = "vinayak"
print(a[2]) # index starts from 0 , index = position -1 

#slicing strings
print(a[2:8]) # at end position = index 
print(a[2:])
print(a[:5])
print(a[-3]) # negative index starts from -1
print(a[::2])

# Escape sequnce
b = "vinayak is \n a goodboy"
c = "vinayak is \t a goodboy"
print(b)
print(c)