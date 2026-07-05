original_marks = [85 , 72 , 96 , 64 , 88 , 91]
marks = [85, 72, 96, 64, 88, 91]
sorted_marks = sorted(marks)
reverse_marks = sorted(marks)
reverse_marks.reverse()
total_sum = sum(marks)
total_students = len(marks)
average_marks =(total_sum/total_students)


print(f"==================== STUDENT MARK ANALYZER ====================== \n Original marks: {original_marks} \n Highest marks = {sorted_marks[-1]} \n Lowest marks: {sorted_marks[0]} \n Total marks: {total_sum} \n Average marks: {average_marks} \n Sorted marks: {sorted_marks} \n Reverse: {reverse_marks} \n  Total students: {total_students} \n =====================================================")