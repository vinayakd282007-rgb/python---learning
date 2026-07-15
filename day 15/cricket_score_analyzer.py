def match_result(team_name, runs):
    if runs>=180:
        return ("Excellent score")
    elif runs>=150 and runs<=179:
        return("Competitive score")
    else:
       return("Low score")

result = match_result( team_name="Rcb" ,runs= 200)
print(result)
result = match_result(team_name="Mi" , runs =160)
print(result)
result =match_result(team_name="RR" ,runs= 120)
print(result)