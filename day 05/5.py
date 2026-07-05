# lists 
'''A list is a collection of items that are ordered, mutable (changeable), and allow duplicate elements. Lists can hold items of different data types, such as integers, strings, or even other list'''
items=["bru", "milk" , "sugar" , "4" , "chicken"]
print(items)
print(items[0]) 

# pop(): Removes the element at a specific index (or the last item if no index is provided).
items.pop() #removes last itme from list
print(items)
items.pop(0) #removes 1st item
print(items)

#append
items.append("mom's magic") # to add items
print(items) 

#remove
items.remove("4") 
print(items)

#insert
items.insert(1 , "spoon")
print(items)
items[0] = "coffe powder"
print(items)
'''clear(): Removes all elements from the list.
fruits.clear()
print(fruits)  # Output: []'''

#slicing list
l = [100 ,200 ,300 ,400 ,500]
l2 = (l[1:4])
print(l2)

# list functions and method
v = [1 , 3 , 9 , 4, 23 , 0]
print(len(v))
print(sum(v))
print(v.index(1))
print(v.count(3)) #counts how many times repeated
v.sort()
print(v)
m = [89,50,3,60,0,1]
print(sorted(m))
m.reverse()
print(m) 
# nesting 
n = [[1,2] , [3,4]]
print(n[0][1])