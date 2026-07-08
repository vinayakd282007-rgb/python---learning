pin = int(input("Enter your atm pin: "))
withdrawal_amount =int(input("Enter withdrawal amount: "))
if pin!=1234:
    print("Access denied")
else:
     if withdrawal_amount<=5000:
        print("Transaction successfull")
     else :
        print(" Daily limit exceeded")

