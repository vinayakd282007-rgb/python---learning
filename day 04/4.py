#operator of python

# commom assignment operators
x = 100
x += 10
print(x) # 100 + 10 = 110
x -= 10
print(x) #110-10 = 100
x *=10
print(x) #100 *10 =1000
x /=10
print(x) #1000 / 10 =100
x %=2
print(x) #modulus operator (%) gives the remainder after division.

# comparison operators
a=10
b=20
print(a==b)
print(a!=b) # not equal to
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#logical operator
'''
print(true and true) # true
print(true and false) # false 
print(true or false) # true
print(not(true and true)) # false 
'''
print(1>2 and 2>1) #false
print(1>2 or 2>1) #true 
print(not(1>2 and 2>1))

#membership operator
s = "vinayak"
print("i" in s)
print("z" not in s)
print("v" not in s)
