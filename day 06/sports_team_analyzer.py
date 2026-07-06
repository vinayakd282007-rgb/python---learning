cricket_team_player_1 = input("Enter cricket player name: ")
cricket_team_player_2 = input("Enter cricket player name: ")
cricket_team_player_3 = input("Enter cricket player name: ")
cricket_team = set((cricket_team_player_1 , cricket_team_player_2 , cricket_team_player_3))
football_team_player_1 = input("Enter football player name: ")
football_team_player_2 = input("Enter football player name: ")
football_team_player_3 =input("Enter football player name: ")
football_team = set((football_team_player_1 , football_team_player_2 ,football_team_player_3))
union = cricket_team | football_team
intersection = cricket_team & football_team
diffrence = cricket_team - football_team
diffrence_2 = football_team - cricket_team 
symmetric_diffrence = cricket_team ^ football_team
print(f" ================================== SPORTS TEAM ANALYZER ============================== \n Cricket team: {cricket_team} \n {" " } \n Football team:  {football_team}\n {" "}\n ------------------------------------------------------- \n Players in both team: {intersection}\n All unique players: {union} \n Players only in cricket team: {diffrence}\n Players only in football team: {diffrence_2} \n Players playing only one sport:  {symmetric_diffrence} \n ================================================================================== ")