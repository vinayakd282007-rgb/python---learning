#functions
'''A function is a reusable block of code that performs a specific task when called. 
Functions are useful to organize code, make it reusable, and reduce redundancy.
'''
'''def greet():
    print("Hello, Good Morning!")

greet()

def marriage(boy , girl): #Parametes
    print(f"Boy is {boy}")
    print(f"Girl is {girl}")
    print(f"{boy} married {girl}")

marriage("Ram" , "sita") #positional argument

marriage(boy = "Ram" , girl="Sita") # keyword argument

def tables(num):
    for i in range(1,11):
        print(f"{num} X {i} = {num*i}")

tables(90)

#Default Parameter Values
def greet(name="Student"):
    print(f"Hello, {name}! Welcome to the Python course.")

greet()  # Uses default value "Student"
greet("Vinayak")  # Uses passed value "Vinayak"

#Returning Values from a Function
def func(num):
    return int(str(num)*2)
a=10
b = func(3)
c=a+b
print(c)'''

def func():
    x = "Vinayak" #local variable
    print(f"{x} , Hello ")
    print(f"{y} , Hello ")
    

y = "vishwa" # global variable

func()
