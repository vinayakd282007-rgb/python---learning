"""j = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{j} x {i} = {i*j}")"""

i = int(input("Enter a number: "))
counter=1
total=1
while counter<=10:
    total=i*counter
    print(f"{i}X{counter} = {total}")
    counter+=1