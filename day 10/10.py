#f for loops
'''In Python, a for loop is used to iterate over a sequence 
(like a list, tuple, string, or range) and execute a block of code repeatedly for each element in the sequence.'''
'''i=1
for i in range(1,11,2): #(start , stop ,step)
    print(i , end="  ")'''

'''bag = ["red", "green" , "blue"]
for ball in bag:
    print(ball)'''

"""name = "vinayak"
for index , letter in enumerate(name):
    print(letter*(index+1))"""

"""l = [12 , 32 , 42 , 52]
for  index , num in enumerate(l):
    print(f"{num} is in {index}th index")
    if num==42:
        print("Found 42")
else:
    print("All printed")"""

'''v = {"name": "vinayak" , "Age": "18" , "Height": "5.5"}
for key , values in v.items():
    print(key ," " , values)'''

#nested for loops
for i in range(2,11):
    for j in range(1 , 11):
        print(f"{i} X {j} = {i*j}")