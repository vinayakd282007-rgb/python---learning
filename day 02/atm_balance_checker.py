balance=float(input("Enter your balance: "))
withdraw=float(input("Enter your withdraw amount: "))
if balance>=withdraw:
    balance=balance-withdraw
    print("Your remaining balance is: ",balance)
    print("Withdraw successful!")
else:
        print("Insufficient balance!")