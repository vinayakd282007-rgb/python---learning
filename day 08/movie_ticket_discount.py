age= int(input("Enter your age: "))
is_today_a_weekend =input("Enter yes or no: ")
if age<12:
    print("50% discount")
elif age>=60:
    print("40% discount")
else:
     print("No age discount")
if is_today_a_weekend == "yes":
      print("Weekend price applies")
else:
      print("Weekday price applies")