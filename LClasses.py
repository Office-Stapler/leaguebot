import json, requests
import LConst

''' 
info infomation:
0 = Name
1 = title
2 = image
3 = skins
4 = lore
5 = allytips
6 = enemytips
7 = tags
8 = partytype
9 = info
10 = stats
11 = abilities
12 = passive
'''
class champion:
    def __init__(self, name):
        json_file = f'data/maindata/champion/{name}.json'
        try:
            with open(json_file) as f:
                info = json.loads(f.read())
            f.close()
            nInfo = []
            try:
                self.name = info['data'][name]['name']
                self.filename = name
                for i in info['data'][name]:
                    if i == 'key' or i == 'id':
                        continue
                    nInfo.append(info['data'][name][i])
                del nInfo[4]
                self.info = nInfo
            except KeyError:
                print('Champion not found')
                self.info = []
        except FileNotFoundError:
            print('Champion not found')
            self.info = []
    
    def checkValid(self):
        if self.info == []:
            return True
        return False

    def getTitle(self):
        if not self.checkValid():
            return self.info[1]
        return 'Champion not found'
    
    def getImage(self):
        if not self.checkValid():
            return f'data/maindata/img/champion/{self.info[2]["full"]}'
        return 'Champion not found'

    def getSkins(self):
        if not self.checkValid():
            skins = []
            for i in self.info[3]:
                skins.append({i['name']:i['num']})
            return skins
        return 'Champion not found'
    
class summoner:
    def __init__(self, name):
        self.url = f'{LConsts.summoner_url}{name}?api_key={LConsts.APIKey}'
        