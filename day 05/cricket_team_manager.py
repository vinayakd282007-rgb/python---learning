original_team = ["Virat", "Rohit", "Gill", "Rahul", "Hardik", "Jadeja"]
players = ["Virat", "Rohit", "Gill", "Rahul", "Hardik", "Jadeja"]
players.append("surya")
players.insert(2, "Pant")
players.remove("Rahul")
players.pop()
sort_players = sorted(players)
reverse_players = sorted(players)
reverse_players.reverse()
total_players =len(players)
print(f"============================== CRICKET TEAM MANAGER =========================== \n Original team: {original_team} \n Final team: {players} \n First player: {players[0]} \n Last player: {players[-1]} \n Total players: {total_players} \n Sorted order: {sort_players} \n Reverse order: {reverse_players} \n =====================================================================================")