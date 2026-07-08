# if-elif and else
x=10
if x==10:
    print("yes x is 10")
v = 3
if v%2==0:
    print("v is even")
else:
    print("v is odd")
signal = input("what's the colour of signal: ")
if signal== "red": 
    print("STOP")
elif signal== "yellow": 
    print("READY")
else: 
    print("GO")
#logical operators
attendence = int(input("Enter your attendence percentage: "))
is_teacher_freind = input("Enter you are teacher freind or not: ")
if attendence>=75 or is_teacher_freind==True:
    print("You can attend exam")
else:
    print("You cannot attend exam")
#Nested if Statements:
day = input("Enter which day it is : ")
is_raining = input("Enter it is raining or not: ")

if day == "Saturday" or day == "Sunday":
    if not is_raining:
        print("Let's visit Mysuru!")
    else:
        print("It's raining, let's stay home.")
else:
    print("It's a weekday, let's wait for the weekend.")