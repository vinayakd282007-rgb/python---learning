#Dictionary
#A dictionary in Python is a collection of key-value pairs. Each key in a dictionary is associated with a value, and you can retrieve or manipulate data using the key. Unlike lists and tuples, dictionaries are unordered and mutable (changeable)

birthday ={ 
           "vinayak": "02-08-2007",
            "vishwa": "29-07-2006",
             "soumya": "30-03-2009"
}
#accessing dictionary elements 
print(birthday["vinayak"]) #output = 02-08-2007
"""can also use the get() method to access values, 
 which is safer because it doesn’t throw an error if the key doesn’t exist.
"""
print(birthday.get("shreeyan" , "Not found"))

#Adding and Updating Dictionary Elements
birthday["veeresh"] = "31-03-2009"
print(birthday) #output={'vinayak': '02-08-2007', 'vishwa': '29-07-2006', 'soumya': '30-03-2009', 'veeresh': '31-03-2009'}
birthday["vinayak"] = "02-08-2008" #updating
print(birthday)

#removing elements
#pop:Removes the specified key and returns the associated value
birthday.pop("vinayak")
print(birthday)
x=birthday.pop("soumya")
print(x) #output =30-03-2009
del birthday["veeresh"]
print(birthday)

#birthday.clear = empties the dictionary

# Dictionary Methods
#keys(): Returns all the keys in the dictionary
print(birthday.keys())
#values(): Returns all the values in the dictionary
print(birthday.values())
#items(): Returns key-value pairs as tuple
print(birthday.items()) #dict_items([('vishwa', '29-07-2006')])
#update(): Updates the dictionary with another dictionary or iterable
dishes ={"bengaluru": "bisi bele bath", 
         "mysuru": "mysuru pak",
         "dharwad": "dharwad sweets"}
birthday.update(dishes)
print(birthday)

item1 = {
      "name":"milk",
       "weight": 1,
       "price": 50
}
item2 = {
       "name": "sugar",
       "weight": 2,
        "price": 99.9
}
items= [item1 , item2]
print(f"Total weight: {item1["weight"] + item2["weight"]}") #output = Total weight: 3