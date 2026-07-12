prices = (input("Enter a prices: ")).split()
total = 0 
for price in prices:
    total+=int(price)
print(total)