#while loop 
'''A loop is a programming structure that repeats a set of instructions as long as a specified condition is True.
 In Python, the while loop allows you to repeatedly execute a block of code as long as the condition is True'''
'''is_failed = True
i = 1
while is_failed and i<=100:
    print(f"Tr {i}")
    i =i+1

print("It's better to give up!")'''

'''is_failed = True
i = 1
while is_failed:
    if i%2!=0: 
       i =i+1
       continue
    print(f"Try {i}")
    i = i+1
    if i>100:
        break'''

'''i = 0 
while i<=10:
    x= 0
    while x<i:
        print("vinayak", end= " ")
        x+=1
    print("")
    i+=1'''
#atm pin
pin = "1234"
trails = 1
while trails<=3:
 input_pin = input(f" Trail- {trails} | pin >> ")
 trails+=1
 if input_pin == pin:
  print("success")
  break
 else:
  print("INCORRECT")