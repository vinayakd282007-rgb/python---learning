profile= {
    "player_name": input("Enter a player name: "),
     "team_name": input("Enter team name: "),
     "matches_played": int(input("Enter matches played: ")),
     "runs_scored": int(input("Enter runs scored: ")),
     "innings_batted": int(input("Enter innings batted: ")),
     "not_outs": int(input("Enter not outs: ")),
     "league": "IPL"
 }

dismissals = profile["innings_batted"]-profile["not_outs"]
profile["dismissals"] = dismissals
profile["runs_scored_today's_match"] = int(input("Enter runs scored in today's match: "))
updated_runs =profile["runs_scored"] + profile["runs_scored_today's_match"] 
profile["updated_runs"]= updated_runs
balls_faced = int(input("Enter balls faced: "))
strike_rate = profile["updated_runs"] / balls_faced*100
profile["strike_rate"] = strike_rate
Average = profile["updated_runs"] / profile["dismissals"]
profile["Average"] = Average
keys = profile.keys()
values = profile.values()
print(f"==================================== CRICKET PLAYER PROFILE ======================================= \n Player name: {profile['player_name']} \n Matches played: {profile['matches_played']} \n Runs scored: {profile['runs_scored']} \n Updated runs scored: {profile['updated_runs']} \n Strike rate : {profile['strike_rate']}\n Average: {profile['Average']} \n {" "} \n ------------------------------------------------------------------------------------------ \n Keys: {keys}\n {" "} \n Values: {values}\n {" "} \n Profile: {profile} \n =================================================================================================== ")