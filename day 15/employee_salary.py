def employee_salary(employee_name , salary = 25000):
    return f"{employee_name}: ₹{salary}"

employee_1 = employee_salary("vinayak")
print(employee_1)
employee_2 = employee_salary("vishwa" , 50000)
print(employee_2)