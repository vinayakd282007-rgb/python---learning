#USERNAME ANALYZER
name = input("Original username: ")
uppercase =name.upper()
lowercase =name .lower()
length = len(name)
first_character =name[0]
last_character = name[-1]
first_three_characters = name[:3]
last_three_characters= name[-3:]
middle_characters =name[2:-2]
repeated_twice=name*2
print(f"======================= USERNAME ANALYZER ================== \n original name: {name} \n Uppercase: {uppercase} \n Lowercase: {lowercase} \n Length: {length} \n First character: {first_character} \n Last character: {last_character} \n First three characters: {first_three_characters} \n Last three characters: {last_three_characters} \n Middle characters: {middle_characters} \n Repeated twice: {repeated_twice} \n ===================================================================")
