import json, requests
import LConst

class Champion:
    def __init__(self, name: str):
        champion_req = requests.get(f"{LConst.CHAMPION_JSON_URL}/{name}.json")
        self.name: str = name
        self.is_valid: bool = champion_req.ok
        self.data: dict = {}
        if champion_req.ok:
            json_res = champion_req.json()
            self.data = list(json_res["data"].values())[0]
    def get_title(self):
        if self.is_valid:
            self.data["title"]
        return 'Champion not found'
    
    def get_splash_screen_image(self):
        if self.is_valid:
            return f'{LConst.CHAMPION_SPLASH_URL}/{self.data["name"]}_0.jpg'
        return 'Champion not found'

    # def getSkins(self):
    #     if not self.checkValid():
    #         skins = []
    #         for i in self.info[3]:
    #             skins.append({i['name']:i['num']})
    #         return skins
    #     return 'Champion not found'

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
# class summoner:
#     def __init__(self, name):
#         self.url = f'{LConst.summoner_url}{name}?api_key={LConst.APIKey}'
#         self.details = json.loads(requests.get(self.url).text)
#         print(name)
#         self.icon = f'data/maindata/img/profileicon/{self.details["profileIconId"]}.png'

#     def find_most_recent_match(self):
#         match_url = LConst.match_by_account_url + self.details['accountId'] + f'?api_key={LConst.APIKey}'
#         match_recent_id = json.loads(requests.get(match_url).text)['matches'][0]['gameId']
#         match_url = LConst.match_by_id_url + str(match_recent_id) + f'?api_key={LConst.APIKey}'
#         match_details = json.loads(requests.get(match_url).text)
#         return match_details


