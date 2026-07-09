running = True
balance = int(10000)
while running:
    print(f"======================== ATM MENU ============================ \n Choose your choice \n 1. Check your balance \n 2. Deposite amount \n 3. Exit \n =======================================================")
    user = int(input("Enter your choice >>> "))
    if user == 1:
        print(f"Your balance is ₹{balance}")
    elif user==2:
        deposite = int(input("Enter deposite amount >>> "))
        balance+=deposite
        print(f"Your new balance {balance}")
    elif user==3:
        print("Thank you for using our ATM!")
        break
    else:
        print("Invalid choice . Please try again ")
        


    
