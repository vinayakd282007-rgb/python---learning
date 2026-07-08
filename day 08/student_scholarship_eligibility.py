name = input("Enter a student name: ")
marks = int(input("Enter marks scored: "))
annual_income = int(input("Enter annual income of family: "))
if marks>=85 and annual_income< 30000:
    print("Scholarship approved")
elif marks>=85 and annual_income>= 30000: 
    print("Not eligible due to income")
else: 
    print("Not eligible")    