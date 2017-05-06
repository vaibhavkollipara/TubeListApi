import requests

youtube_api_key = 'YOUR_YOTUTBE_API_KEY'

default_thumbnail_url = 'https://www.googleapis.com/youtube/v3/videos?id={}&key={}&fields=items(snippet(title,thumbnails(default(url))))&part=snippet'

all_thumbnails_url = 'https://www.googleapis.com/youtube/v3/videos?id={}&key={}&fields=items(snippet(title,thumbnails))&part=snippet'


def grabCode(url):
    if url.startswith("https://www.youtube.com"):
        return url[32:]
    elif url.startswith('https://youtu.be'):
        return url[17:]
    else:
        return None


def grabVideoDetails(videoId):
    try:
        response = requests.get(default_thumbnail_url.format(videoId, youtube_api_key))
        if response.status_code != 200:
            raise ValueError('Something wrong..')
        item = response.json().get('items')
        if item[0] and item[0]['snippet']['title'] and item[0]['snippet']['thumbnails']['default']['url']:
            return (item[0]['snippet']['title'], item[0]['snippet']['thumbnails']['default']['url'])
    except:
        raise ValueError('A very specific bad thing happened')
