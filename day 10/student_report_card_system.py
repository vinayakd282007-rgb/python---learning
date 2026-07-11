students = {
    "Rahul": 85,
    "Anjali": 92,
    "Kiran": 34,
    "Sneha": 76,
    "Amit": 49
}
print(f"=================== STUDENTS REPORT CARD =========================== ")
passed = 0
failed = 0
topper= " "
highest_marks=0
total_marks=0
for index, (student , marks )in enumerate  (students.items()) :
    print(f"{index+1}. {student} - {marks} " , end=" ")
    total_marks+=marks
    if marks>=35:
        print("- Pass")
        passed+=1
    else:
        print("-Fail")
        failed+=1
    if marks>highest_marks:
        highest_marks =marks
        topper= student       
total_students = len(students)
average_marks =total_marks/total_students 

print("----------------------------------------------------------")
print(f"Total students: {total_students}") 
print(f"Passed: {passed}") 
print(f"Failed: {failed}") 
print(f"Topper:{topper}")
print(f"Marks: {highest_marks}")
print(f"Average marks: {average_marks}")
print("==========================================================================================")

    
    


