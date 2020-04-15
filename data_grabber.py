import urllib.request
import os
import json

def grab_image(mode='loading'):
    base_url = 'data/maindata/champion/'
    download_url = f'data/champion/{mode.replace("/", "")}/'
    for i in os.listdir(base_url)[29:]:
        with open(base_url + i) as fread:
            data = json.load(fread)
        name = i.replace('.json', '')
        skins = data['data'][name]['skins']
        base_id = 0
        for j in skins:
            rq_name = name + f'_{int(j["num"])}.jpg'
            full_path = download_url + rq_name + '.jpg'
            if rq_name not in os.listdir(download_url):
                try:
                    urllib.request.urlretrieve(f'http://ddragon.leagueoflegends.com/cdn/img/champion/{mode.replace("/", "")}/' + rq_name, download_url + rq_name)
                    print(f'Finished dumping {rq_name}...')
                except:
                    print(f'Error for {rq_name}')
# grab_image(input())
url1 = 'data/champion/tiles/'
url2 = 'data/champion/loading'
for x,y in zip(os.listdir(url1), os.listdir(url2)):
    if x != y:
        print(x,'!=', y)
        break
