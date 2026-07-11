employee = input("Enter employees name : ").split()
salary = input("Enter employess salary: ").split()
employee_salary = {employee[i]: int(salary[i]) for i in range(len(employee))}
print(employee_salary)
'''employee_salary= {}
for i in range (len (employee)):
    employee_salary[employee[i]]= int(salary[i])
print(employee_salary)
'''