import json
summoner_url = 'https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
chest_url = 'https://oc1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/'
league_summoner_url = "https://oc1.api.riotgames.com/lol/league/v4/entries/by-summoner/"
match_by_id_url = 'https://oc1.api.riotgames.com/lol/match/v4/matches/'
match_by_account_url = 'https://oc1.api.riotgames.com/lol/match/v4/matchlists/by-account/'
champ_rotation_url = 'https://oc1.api.riotgames.com/lol/platform/v3/champion-rotations'



LEAGUE_API_TOKEN = ''
DISCORD_TOKEN = ''
with open("./config.json", "r+") as f:
    config = json.load(f)
    API_KEY = config["LEAGUE_API_TOKEN"]
    DISCORD_TOKEN = config["DISCORD_TOKEN"]