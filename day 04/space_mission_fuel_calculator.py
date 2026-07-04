rocket_name =input("Enter rocket name: ")
fuel = int(input("enter rocket fuel: "))
fuel_used = int(input("Enter fuel used: "))
fuel_remaining = fuel - fuel_used 
distance_travelled = int(input("Enter distance travelled: "))
mission_code = input("Enter mission code: ")
print(f"=========================== SPACE MISSION FUEL INSPECTOR ============================= \n Rocket name: {rocket_name} \n Fuel remaining: {fuel_remaining} \n Distance travelled: {distance_travelled} \n Fuel used>Distance: {fuel_used>distance_travelled} \n Fuelused == Distance: {fuel_used==distance_travelled} \n Mission code: {mission_code} \n =============================================================================")
