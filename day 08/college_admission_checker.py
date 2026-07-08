name = input("Enter student name: ")
kcet_rank = int(input("Enter kcet rank: "))
category = input("Enter your category: ").lower()
percentage_of_class_12th = int(input("Enter 12th percentage: "))
if percentage_of_class_12th < 45:
    print("Not eligible for admission: ")
else:
    if kcet_rank <=10000:
        print("Excellent chance")
    elif kcet_rank<=50000:
            print("Good chance")
    else:
            print("Low chances")
                    
    if category == "sc" or category=="st" :
                print("Reservation may improve your chances")
   
            