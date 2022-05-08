import json

with open('scores.json') as f:
    jsondata=json.load(f)



for game in jsondata['events']:
    league= game['tournament']['name']
    hometeam= game['homeTeam']['name']
    awayteam= game['awayTeam']['name']
    homescore=game['homeScore']['current']
    awayscore=game['awayScore']['current']
    print(league,"|", hometeam, homescore, " - ",awayscore,awayteam)












