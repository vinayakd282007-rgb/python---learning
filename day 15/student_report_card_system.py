def student_report_card(student_name, maths, science, english):

    total_marks = maths + science + english
    average_marks = total_marks / 3

    if maths < 35 or science < 35 or english < 35:
        result = "Fail"
    else:
        result = "Pass"

    if average_marks >= 90:
        grade = "A"
    elif average_marks >= 75:
        grade = "B"
    elif average_marks >= 60:
        grade = "C"
    else:
        grade = "D"

    return total_marks, average_marks, result, grade


running = True

while running:

    name = input("Enter student name: ")

    maths = int(input("Enter Maths marks: "))
    science = int(input("Enter Science marks: "))
    english = int(input("Enter English marks: "))

    total, average, result, grade = student_report_card(
        name, maths, science, english
    )

    print("\n================ STUDENT REPORT CARD ================")
    print(f"Student Name : {name}")
    print(f"Maths        : {maths}")
    print(f"Science      : {science}")
    print(f"English      : {english}")
    print(f"Total Marks  : {total}")
    print(f"Average      : {average:.2f}")
    print(f"Result       : {result}")
    print(f"Grade        : {grade}")
    print("====================================================")

    choice = input("Do you want to continue? (yes/no): ").lower()

    if choice != "yes":
        running = False