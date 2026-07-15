def resturant_bill(food_price , gst=5):
    total_price = food_price+(food_price *gst/100)
    return (total_price)

bill = resturant_bill(520)
print(bill)

    
