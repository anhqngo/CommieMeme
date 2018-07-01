import requests
import json
import urllib2

def check():
    headers = {
        "Authorization": "lzaCvprV-UIUR9vVZePY6dEg388", 
        "User-Agent": "CommieMeme/0.1 by jdagod",
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        }
    url = "https://www.reddit.com/r/FULLCOMMUNISM/top/.json"
    req = urllib2.Request(url, headers=headers)
    text_data = urllib2.urlopen(req).read()
    data = json.loads(text_data)
    pic_url = data["data"]["children"][0]['data']['url']
    print pic_url

check()