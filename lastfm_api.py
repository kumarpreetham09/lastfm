API_KEY = ""
USER = ""
USER_AGENT = ""

def lastfm_get(payload):
    # define headers and URL
    headers = {'user-agent': USER_AGENT}
    url = f'http://ws.audioscrobbler.com/2.0/?api_key={API_KEY}&format=json'

    # Add API key and format to the payload
    payload['api_key'] = API_KEY
    payload['format'] = 'json'

    response = requests.get(url, headers=headers, params=payload)
    return response

weekly_artist_chart = lastfm_get({
    'method': 'user.getweeklyartistchart',
    'user' : USER
})

weekly_album_chart = lastfm_get({
    'method': 'user.getweeklyalbumchart',
        'user' : USER
})

weekly_track_chart = lastfm_get({
    'method': 'user.getweeklytrackchart',
    'user' : USER
})

album_info = lastfm_get({
    'method': 'album.getinfo',
    'album' : 'Swimming',
    'artist' : 'Mac Miller',
    'user' : USER
})

def jprint(obj):
    text = json.dumps(obj)
    print(text)

i = 0

def print_list(list):

    for artist in list:
        print(artist)

weekly_artist_chart_list = [{"artist" : str(element["name"]), "playcount": int(element["playcount"])} for element in weekly_artist_chart.json()["weeklyartistchart"]["artist"] if int(element["@attr"]["rank"]) <= 5]
weekly_album_chart_list = [{"artist" : str(element["artist"]["#text"]) ,"album" : str(element["name"]), "playcount": int(element["playcount"])} for element in weekly_album_chart.json()["weeklyalbumchart"]["album"] if int(element["@attr"]["rank"]) <= 5]
weekly_track_chart_list = [{"artist" : str(element["artist"]["#text"]) ,"track" : str(element["name"]), "playcount": int(element["playcount"])} for element in weekly_track_chart.json()["weeklytrackchart"]["track"] if int(element["@attr"]["rank"]) <= 10]
print("TOP ARTISTS")
print_list(weekly_artist_chart_list)
print("")
print("TOP ALBUMS")
print_list(weekly_album_chart_list)
print("")
print("TOP TRACKS")
print_list(weekly_track_chart_list)
