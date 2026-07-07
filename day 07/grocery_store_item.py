items ={
      "product": input("Enter product name: "),
       "quantity":int(input("Enter quantity: ")),
       "price": int(input("Enter price: ")),
        "category" : input("Enter category: ")    }
items["discount"] =int(input("Enter discount percentage: "))
items.pop("category")
discounting= items["Price"] * items["discount"]/100
new_price = items["Price"] - discounting
items["new_price"] = new_price
keys=items.keys()
values = items.values()
print(f"====================================== GROCERY STORE INFORMATION ========================================= \n Product name: {items['product']} \n Price: ₹{items['Price']} \n Quantity: {items['quantity']} \n -------------------------------------------------------------------------------------- \n Discount: {items['discount']}% \n New price: ₹{new_price} \n Total = ₹{new_price} \n Items: {items} \n  keys: {keys} \n values: {values} \n ===============================================================================")