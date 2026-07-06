#Tuple and sets

# A tuple is a collection of items that is ordered and immutable (unchangeable). Tuples are similar to lists, but once a tuple is created, you cannot modify it. They are often used to group related data together.
genders = ("male" , "female" , "others")
print(type(genders)) #<class 'tuple'>
print(genders[1]) # 'female'

#To create a tuple with only one element, include a trailing comma:
single_element_tuple = ("apple",)

#Tuple Operations
#Tuple Concatenation:
tuple1 = (1,2,3)
tuple2 = (4,5,6)
combined_tuple =tuple1 + tuple2
print(combined_tuple)
#tuple repetition
tuple3 = (3 , 4) *3
print(tuple3)
#Checking Membership
fruits = ("apple" , "cherry" , "grapes")
print( "apple" in fruits) #true 

# Tuple Methods
#count:
my_tuple = (1, 2, 3, 1, 1)
print(my_tuple.count(1))  # Output: 3
#index:
my_tuple = ("apple", "banana", "cherry", ("carrot" , "cucumber"))
print(my_tuple.index("banana"))  # Output: 1
print(my_tuple[3].index("carrot")) #output: 0
print(my_tuple[3][0]) #output: carrot

#sets
#A set is a collection of unique items that is unordered and unindexed. Sets do not allow duplicate values. Sets are useful for performing operations like union, intersection, and difference.
fruits_set = {"apple", "banana", "cherry"}
numbers_set = {1, 2, 3, 4, 5}
s2 = set((1,2,3))
print(type(s2)) # output: <class 'set'>
print(s2) #output: {1, 2, 3}
#empty set: 
empty_set = set()

#set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Output: {1, 2, 3, 4, 5}
intersection_set = set1 & set2  # Output: {3}
difference_set = set1 - set2  # Output: {1, 2}
print(union_set)
print(intersection_set)
print(difference_set)
#Symmetric Difference:
#The symmetric difference returns elements that are in either of the sets but not in both
sym_diff_set = set1 ^ set2  # Output: {1, 2, 4, 5}

#set methods
#add.()
fruits_set.add("orange")
print(fruits_set)  # Output: {'apple', 'banana' , 'cherry' , 'orange'}
#remove.()
fruits_set.remove("banana")
print(fruits_set)  # Output: {'apple', 'cherry'}