student = {
        "name": input("Enter your name: "),
        "Age": int(input("Enter your age: ")),
        "course" : input("Enter course selected: " ),
        "college": input("Enter college name: ")
}
student["city"]= input("Enetr city name: ")
all_keys = (student.keys())
values = (student.values())
print(f" ===================================== STUDENT INFORMATION ===================================== \n Student name: {student['name']} \n Age: {student['Age']} \n Course: {student['course']} \n College: {student['college']} \n City: {student['city']}\n ---------------------------------------------------------------- \n {" "} \n All keys: {all_keys} \n All values: {values} \n  Student: {student} \n ===========================================================================================================")
