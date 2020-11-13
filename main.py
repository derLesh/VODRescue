import json, requests, urllib, os

TWITCH_HELIX = "https://api.twitch.tv/helix"
TWITCH_KRAKEN = "https://api.twitch.tv/kraken"
CLIENT_ID = ""
OAUTH = ""
PATH = os.path.dirname(os.path.abspath(__file__)) + '\VODRescue\\'

downloader = urllib.request

with open('login.json') as json_file:
    data = json.load(json_file)
    for p in data['twitch']:
        CLIENT_ID = p['client_id']
        OAUTH = p['oauth']
    HEADER = {'Client-Id': CLIENT_ID, 'Authorization': 'Bearer ' + OAUTH}
    print(CLIENT_ID)
    print(OAUTH)

def connect_to():
    url = TWITCH_HELIX + '/clips/AlluringIgnorantDonutDeIlluminati'
    response = requests.get(url, headers=HEADER).json()
    print(response)
    
def get_all_clips():
    print("Soon")

def get_clip():
    url = TWITCH_HELIX + '/clips?id=AlluringIgnorantDonutDeIlluminati'
    clip_response = requests.get(url, headers=HEADER).json()
    print(clip_response)
    clip_thumbnail = clip_response['data'][0]['thumbnail_url']
    clip_file = clip_thumbnail.split("-preview",1)[0] + ".mp4"
    clip_filename = clip_response['data'][0]['title'] + "_" + clip_response['data'][0]['id'] + ".mp4"
    print(f"URL: {clip_file} | Filename: {clip_filename}")
    save_clip(clip_file, clip_filename)

def save_clip(url, filename):
    downloader.urlretrieve(url, PATH + filename)

get_clip()