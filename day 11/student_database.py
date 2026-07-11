students = input("Enter student names: ").split()
marks = input("Enter student marks: ").split()

# Part 1
student_report_card = {
    students[i]: int(marks[i])
    for i in range(len(students))
}

# Part 2
passed_marks = [
    students[i]
    for i in range(len(marks))
    if int(marks[i]) > 50
]

# Part 3
square_dictionary = {
    int(marks[i]): int(marks[i]) ** 2
    for i in range(len(marks))
}

# Part 4
total = 0
for mark in marks:
    total += int(mark)

# Part 5 (Printing)
print("\n================ STUDENT DATABASE SYSTEM ================\n")

print("Part 1: Student -> Marks Dictionary")
print(student_report_card)

print("\nPart 2: Marks Above 50")
print(passed_marks)

print("\nPart 3: Marks -> Square Dictionary")
print(square_dictionary)

print("\nPart 4: Total Marks")
print(total)

print("\nPart 5: Student Report")
for i in range(len(students)):
    print(f"{students[i]} - {marks[i]}")