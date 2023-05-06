import json, requests

CHAMPION_JSON_URL = "http://ddragon.leagueoflegends.com/cdn/13.9.1/data/en_AU/champion"
CHAMPIONS_JSON_URL = "http://ddragon.leagueoflegends.com/cdn/13.9.1/data/en_US/champion.json"
CHAMPION_SPLASH_URL = "http://ddragon.leagueoflegends.com/cdn/img/champion/splash"
SUMMONOR_URL = 'https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
CHEST_URL = 'https://oc1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/'
LEAUGE_SUMMONER_URL = "https://oc1.api.riotgames.com/lol/league/v4/entries/by-summoner/"
MATCH_BY_ID_URL = 'https://oc1.api.riotgames.com/lol/match/v4/matches/'
MATCH_BY_ACCOUNT_URL = 'https://oc1.api.riotgames.com/lol/match/v4/matchlists/by-account/'
CHAMPION_ROTATION_URL = 'https://oc1.api.riotgames.com/lol/platform/v3/champion-rotations'

LEAGUE_API_TOKEN = ''
DISCORD_TOKEN = ''
with open("./config.json", "r+") as f:
    config = json.load(f)
    API_KEY = config["LEAGUE_API_TOKEN"]
    DISCORD_TOKEN = config["DISCORD_TOKEN"]

CHAMPIONS = list(requests.get(CHAMPIONS_JSON_URL).json()["data"].keys())
