#Revising
# #swaping two variable using third
a=10
b=20
temp =a
a=b
b= temp
print("a", a)
print("b" , b)
#swaping two variable without  using third
a=10
b=20
a,b=b,a
print("a", a)
print("b" , b)

x="Hello world"
text = x.replace(" ", "")
print(len(text))

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print("Both number are greater than 10" , a>10 and b>10)
print("either of number is  less than 5" ,a<5 or b<5)
print("The first number is not greater than the second" , not(a>5))


l = [11, 24 , 35 ,78]
l.sort(reverse=True)#descending order
print(l)#[78, 35, 24, 11]
print(l[::-1])#to reverse order
      