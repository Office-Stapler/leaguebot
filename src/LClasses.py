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


