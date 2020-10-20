import requests
endpoint_url = "https://api.spotify.com/v1/recommendations?"
#filters
limit = 10
market ='US'
seed_genres ='Indie'
target_danceability=0.9
uris=[]

def Query(limit,market,seed_genres,target_danceability):
    query =f"'{endpoint_url}'limit='{limit}'&market ='{market}'&seed_genres='{seed_genres}'&target_danceability ='{target_danceability}'")
    response = requests.get(query, headers ={'Content-Type':'application/json','Authorisation':f"Bearer'{token}'"})
    json_response = response.json()
    for i in json_respoonse['tracks']:
        uris.append(i)
        print(f"\"{i['name']}\" by {i['artists'][0]['name']}")


