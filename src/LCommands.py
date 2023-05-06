import requests, json
from PIL import Image
import os

from Models.Champion import Champion


# returns the champions name with a given champion id
# def findNamebyId(champid):
#     with open('data/maindata/champion.json') as f:
#         info = json.loads(f.read())
#     for i in info['data'].keys():
#         if champid == int(info['data'][i]['key']):
#             return info['data'][i]['name']

# returns the URL used to get information about a summoner
# def getSummonerURL(summonerName):
#     return f'{const.SUMMONOR_URL}{summonerName}?api_key={const.APIKey}'

# finds the skin requested, returns the data URL
# def fSkin(name, find = None):
#     if name == None:
#         return name
#     champ = getChampInfo(name)
#     if champ == None:
#         return None
#     skins = champ.getSkins()
#     # if what they're finding is an integer
#     if isinstance(find, int):
#         if find >= len(skins) or find < 0:
#             return None
#         dic = skins[find]
#         a = list(dic.keys())[0]
#         print(f'Sending {a}')
#         return f'data/champion/splash/{champ.filename}_{dic[a]}.jpg'
#     else:
#         counter = 0
#         string = ''
#         for i in skins:
#             string += f'{counter} = {list(i)[0].capitalize()}\n'    
#             counter += 1
#         return string

# finds the champ info 
def fChampInfo(champion: Champion):
    if not champion.is_valid:
        return ''
    a_dict = {}
    
    tips_for = []
    for idx, tip in enumerate(champion.allytips):
        tips_for.append(f'{idx + 1}: {tip}')
    a_dict[f'Tips as {champion.name}:'] = tips_for

    tips_against = []
    for idx, tip in enumerate(champion.enemytips):
        tips_against.append(f'{idx + 1}: {tip}')
    a_dict[f'Tips versing {champion.name}:'] = tips_against

    tags = [(f'Type:')]
    for idx, tag in enumerate(champion.tags):
        tags.append(f'{idx + 1}: {tag}')

    a_dict['Abilities use:'] = [f'{champion.partype}']
    stats_info = []
    stats = champion.stats
    keys = list(stats.items())
    for [stat_type, stat_value] in keys:
        stats_info.append(f'{stat_type.capitalize()} = {stat_value}')
    a_dict['Stats'] = stats_info
    return a_dict

# def fAbilities(name):
#     champ = getChampInfo(name)
#     if champ == None:
#         print('Champion not found, usage is +listskin {champion}')
#         return []
#     return champ
    

def rankedInfo(summonerName):
    pass