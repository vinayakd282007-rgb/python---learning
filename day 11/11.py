#sum in loop
l = [1, 23 , 43 , 56]
total =0
for num in l:
    total = total+num
print(total)

#Doubling each number in a list
l = [1, 2 , 3 , 4 , 19, 20 , 39]
dl = []
for num in l:
    dl.append(num*2)
print(dl) #o/p = [2, 4, 6, 8, 38, 40, 78]

#for Loops with range()

students = ["vinayak" , "vishwa" , "soumya"]
marks = [91 , 92 , 93]
student_marks = {}

for index , student in enumerate(students):
    student_marks[student] = marks[index]

print(student_marks) #o/p = {'vinayak': 91, 'vishwa': 92, 'soumya': 93}

name= ["vinayak" , "vishwa" , "soumya"]
dob = ["02-08-2007" , "29-07-2006" , "30-03-2009"]
name_dob = {}
for i in range(len(name)):
    name_dob[name[i]] =dob[i]
print(name_dob) #{'vinayak': '02-08-2007', 'vishwa': '29-07-2006', 'soumya': '30-03-2009'}

# List Comprehension
l= [num for num in range(1,6)] #l= [1,2,3,4,5]
dl =[num**2 for num in l] #new_list = [expression for item in collection(l) if condition]
print(dl) #[1, 4, 9, 16, 25]
edl = [num**2 for num in l if num%2==0]
print(edl) #o/p =[4, 16] even number

#dictionary comprehension
names = ["vinayak" , "vishwa" , "soumya"]
d = {name:len(name) for name in names}   
print(d) 

city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}
large_ciy = {city:pop for city, pop in city_population.items() if pop>10}
print(large_ciy) #{'Bengaluru': 84, 'Mysuru': 11}

s = "my-- name-- is-- vinayak"
v = s.split("--")# or v= s.split() if s ="my name is vinayak" it will split in space 
print(v) #['my', 'name', 'is', 'vinayak']

#list input practice
'''In Python, the split() method allows you to break a string into a list of words or elements 
based on a specified separator (like space, comma, etc.).
 This is very useful when you have data in string format and want to convert it into a list
 '''
  
l = [int(num) for num in input("Enter a integers: ").split()]
print(l)