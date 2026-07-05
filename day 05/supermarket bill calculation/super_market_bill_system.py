products = ["Rice", "Milk", "Sugar", "Oil", "Bread"]
prices = [60, 30, 45, 120, 40]
print(f"============================== BENGLURU SUPERMARKET ================================ \n Available products : \n 1.{products[0]} = ₹{prices[0]} \n 2.{products[1]} = ₹{prices[1]} \n 3.{products[2]} = ₹{prices[2]} \n 4.{products[3]} = ₹{prices[3]} \n 5.{products[4]} = ₹{prices[4]} \n ---------------------------------------- ")
cart = ['Rice', 'Sugar', 'Bread']
total_items = len(cart)
first_item =cart[0]
last_item = cart[-1]
print(f" Customer cart : \n Cart: {cart} \n First item: {first_item} \n Last_item: {last_item} \n Total number of items: {total_items} \n ----------------------------------------")
cart= ["Rice" , "Sugar" , "Bread"]
sorted_cart = sorted(cart)
reverse_cart= sorted(cart)
reverse_cart.reverse()
print(f" Sorting :\n Sorted cart= {sorted_cart} \n  Reverse :\n {reverse_cart} \n---------------------------------------- ")
cart=["Rice" , "Sugar" , "Bread"]
prices =[60 ,45 , 40]
total_bill = sum(prices)
print(f" Bill : \n  1.{cart[0]} = ₹{prices[0]} \n  2.{cart[1]} = ₹{prices[1]} \n  3.{cart[2]} = ₹{prices[2]} \n --------------------------\n  TOtal bill = ₹{total_bill} \n ------------------------- \n  Thank you for shopping! \n ================================================================")