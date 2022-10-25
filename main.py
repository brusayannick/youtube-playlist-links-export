import requests

apikey = '&key=' + 'YOUR API KEY'
playlisturl = 'YOUR PLAYLIST URL'

playlisturl = 'https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=10000&playlistId=' + playlisturl + apikey
videourl = 'https://youtube.googleapis.com/youtube/v3/videos?part=snippet&id='
ytvidurl = 'https://www.youtube.com/watch?v='

def getvideourl(id):
    return videourl + id + apikey

response = requests.get(playlisturl)
data = response.json()

items = []

for item in data['items']:
    item = item['snippet']['resourceId']['videoId']
    items.append(item)

for item in items:
    print(ytvidurl + item)
