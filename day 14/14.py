d={
    "friend_1":{
        "name": "vishwa",
        "fav_sport": "cricket",
        "fav_food": "Biryani"
        
    },
    "friend_2":{
        "name":"vinayak",
        "fav_sport":"football",
        "fav_food": "Pizza"

    }
}
print(d["friend_1"]["fav_food"])

i=0
while i<=20:
    if i%2!=0:
        print(i)
    i+=1

seat =8
while seat>0:
    s = input("Do you want to book seat: Yes/No?  ").lower()
    if s=="yes":
        print("your seat confirmed")
    else:
        print("you not selected seat")
    seat-=1
print("All seats are booked!")

import time
t=10
while t>0:
    print(t)
    time.sleep(1)
    t-=1
print(" 'Happy new year' ")

for i in range(1,11):
    for j in range(1,11):
        print(f"{i}X{j} = {i*j}")

number = 3
counter =1 
while counter<=10:
    total = number*counter
    print(f"{number} X {counter} = {total}")
    counter+=1

total =0
for sum in range(1,11):
    total+=sum
    print(total)

name = input("Enter your name: ")
for letter in name:
    print(letter)

vowels = "aeiou"
counter = 0
s= input("Enter a sentence: ")
for letter in s:
    if letter in vowels:
        counter+=1
print(counter)      

products ={
    "Pen": 10,
    "Pencils":5,
    "Papaer":20,
    "sharpner":5
}
total=0
for  _, price in products.items(): #if we dont want key value use '_'
    total+=price
print(total)
print(sum(list(products.values())))

l = [
    {
        "name":"vinayak",
        "Age":18,
    },
    {
        "name":"soumya",
        "Age":17
        }
]
for student in l:
    print(student["name"], "-" , student["Age"])

#Nested list 
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
matrix =[]
for i in range(rows):
    row=[]
    for j in range(columns):
        x = int(input("Enter the element: "))
        row.append(x)
    matrix.append(row)
print(matrix)