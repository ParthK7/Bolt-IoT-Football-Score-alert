import json
import time
import requests
from boltiot import Bolt

api_key = "41329a1a-7459-4041-9239-27f8a1998f3f"
device_id  = "BOLT14000282"
mybolt = Bolt(api_key, device_id)


url = "https://api.sofascore.com/api/v1/sport/football/events/live"

payload = ""
headers = {
    "authority": "api.sofascore.com",
    "cache-control": "max-age=0",
    "sec-ch-ua": "^\^",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
response = requests.request("GET", url, data=payload, headers=headers)
jsondata = json.loads(response.text)


def setdata():
    league = game['tournament']['name']
    hometeam = game['homeTeam']['name']
    awayteam = game['awayTeam']['name']
    homescore = game['homeScore']['current']
    awayscore = game['awayScore']['current']
    return (league, hometeam, awayteam, homescore, awayscore)


for game in jsondata['events']:
    league, hometeam, awayteam, homescore, awayscore = setdata()
    print(league, "|", hometeam, homescore, " - ", awayscore, awayteam)

reqd_league = input("Enter name of League")
reqd_hometeam = input("Enter Hometeam name")
for game in jsondata['events']:
    league, hometeam, awayteam, homescore, awayscore = setdata()
    if (league == reqd_league and hometeam == reqd_hometeam):
        prev_homescore=homescore
        prev_awayscore=awayscore
        print(league, "|", hometeam, homescore, " - ", awayscore, awayteam)


while True:
    response = requests.request("GET", url, data=payload, headers=headers)
    jsondata = json.loads(response.text)

    for game in jsondata['events']:
        league, hometeam, awayteam, homescore, awayscore = setdata()
        if (league == reqd_league and hometeam == reqd_hometeam):
            new_homescore = homescore
            new_awayscore = awayscore
            if (new_homescore != prev_homescore or new_awayscore != prev_awayscore):
                print("The score has changed")
                response = mybolt.digitalWrite('0', 'HIGH')
                print(league, "|", hometeam, homescore, " - ", awayscore, awayteam)
                prev_homescore=new_homescore
                prev_awayscore=new_awayscore

            else:
                print("The scores are still the same")
                response = mybolt.digitalWrite('0', 'LOW')
                print(league, "|", hometeam, homescore, " - ", awayscore, awayteam)

    
    time.sleep(60)


            
    
