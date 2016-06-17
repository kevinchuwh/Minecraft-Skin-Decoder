import base64
import urllib.request
import json

def decodeB64(code):
    bas64text = base64.b64decode(code)
    baseUTF = bas64text.decode('utf-8')
    crop = baseUTF.split('\"url\":\"')[1]
    url = crop[:-4]
    print(url)

def getSkin(UUID):
    page = urllib.request.urlopen('https://sessionserver.mojang.com/session/minecraft/profile/' + UUID)
    content = page.read().decode('utf-8')
    json_obj = json.loads(content)
    list_d = json_obj['properties']
    return list_d[0]['value']

    
decodeB64(getSkin(input('Enter UUID > ')))
