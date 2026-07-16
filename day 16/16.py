# *args and **kwargs to accept a variable number of arguments in a function.
def add(*numbers):
    print(type(numbers))#<class 'tuple'>
    return sum(numbers) 


c= add(1,2,4,500)
print(c)

def student_info(**details):
    print(type(details))#<class 'dict'>
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Anand", age=22, course="Python")

'''Lambda Functions
A lambda function is a small anonymous 
function that can take any number of arguments but has only one expression.'''

add = lambda a,b :a+b
print(add(1,2))

students=[
        {"name":"vinayak" , "marks":40},
        {"name":"vishwa" , "marks":100},
        {"name":"soumya" , "marks":70}
]
students.sort(key = lambda x:x ["marks"])
print(students)

#Recursion
'''Recursion occurs when a function calls itself.
It's used to solve problems that can be broken down into smaller, similar problems.'''
def factorial(n):
    if n==1:
        return 1
    return n *factorial(n-1)

x= factorial(4)
print(x)

#nested functions
def outer_function(name):
    def inner_function():
        print(f"Hello, {name}!")
    inner_function()

outer_function("Anand") #Hello, Anand!

def calculate(a,b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mult():
        print(a*b)
    add()
    sub()
    mult()

calculate(10,2)