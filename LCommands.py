import requests, json
import LConst as const
import LClasses
import os, re
from PIL import Image

# returns the champions name with a given champion id
def findNamebyId(champid, champions):
    for i in champions['data']:
        if champid == int(champions['data'][i]['key']):
            return champions['data'][i]['name']
# returns the URL used to get information about a summoner
def getSummonerURL(summonerName):
    return f'{LConsts.summoner_url}{summonerName}?api_key={const.APIKey}'

# returns a champion class with a given champion name

def getChampInfo(name):
    name = name.replace(' ', '')
    path = 'data/maindata/champion/'
    list_champs = os.listdir(path)
    for file in list_champs:
        if str(file).lower().replace('.json', '') == name.lower():
            champ = LClasses.champion(str(file).replace('.json',''))
            return champ
    return None

# finds the skin requested, returns the data URL
def fSkin(name, find = None):
    if name == None:
        return name
    champ = getChampInfo(name)
    if champ == None:
        return None
    skins = champ.getSkins()
    # if what they're finding is an integer
    if isinstance(find, int):
        if find >= len(skins) or find < 0:
            return None
        dic = skins[find]
        a = list(dic.keys())[0]
        print(f'Sending {a}')
        return f'data/champion/splash/{champ.filename}_{dic[a]}.jpg'
    else:
        counter = 0
        string = ''
        for i in skins:
            string += f'{counter} = {list(i)[0].capitalize()}\n'    
            counter += 1
        return string

# finds the champ info 
def fChampInfo(name):
    champ = getChampInfo(name)
    if champ == None:
        return ''
    adict = {}
    intro = [f'About {champ.name}: {champ.info[1]}']
    adict['intro'] = intro
    tFor = []
    counter = 1
    for i in champ.info[5]:
        tFor.append(f'{counter}: {i}')
        counter += 1
    adict[f'Tips as {champ.name}:'] = tFor
    tAgainst = []
    counter = 1
    for i in champ.info[6]:
        tAgainst.append(f'{counter}: {i}')
        counter += 1
    adict[f'Tips versing {champ.name}:'] = tAgainst

    Type = [(f'Type:')]
    counter = 1
    for i in champ.info[7]:
        Type.append(f'{counter}: {i}')
        counter += 1
    adict['What Abilities Use:'] = [f'{champ.info[8]}']
    sinfo = []
    stats = champ.info[10]
    keys = list(stats.keys())
    for i in keys:
        sinfo.append(f'{i.capitalize()} = {stats[i]}')
    adict['Stats'] = sinfo
    return adict

def fAbilities(name):
    champ = getChampInfo(name)
    if champ == None:
        print('Champion not found, usage is +listskin {champion}')
        return []
    return champ
    

def rankedInfo(summonerName):
    pass