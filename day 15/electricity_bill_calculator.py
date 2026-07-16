def electricity_bill(customer_name , unit_consumed):
    if unit_consumed<=100:
        return unit_consumed*5
    elif unit_consumed>=101 and unit_consumed<=200:
        return unit_consumed*7
    else:
        return unit_consumed*10
            
running=True
while running:
    name =input("Enter customer name: ")
    units = int(input("Enter units consumed: "))
    bill=electricity_bill(name,units)
    print(f"{name}: ₹{bill}")
    choice = input("if you want to continue:(Yes/No) ").lower()
    if choice=="no":
        running=False