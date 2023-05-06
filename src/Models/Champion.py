import requests
import LConst
class Champion:
    def __init__(self, name: str):
        champion_req = requests.get(f"{LConst.CHAMPION_JSON_URL}/{name}.json")
        self.name: str = name
        self.is_valid: bool = champion_req.ok
        if champion_req.ok:
            json_res = champion_req.json()
            data = list(json_res["data"].values())[0]
            self.id = data["id"]
            self.title = data["title"]
            self.name = data["name"]
            self.image = data["image"]
            self.skins = data["skins"]
            self.lore = data["lore"]
            self.blurb = data["blurb"]
            self.allytips = data["allytips"]
            self.enemytips = data["enemytips"]
            self.tags = data["tags"]
            self.partype = data["partype"]
            self.info = data["info"]
            self.stats = data["stats"]
            self.spells = data["spells"]
            self.passive = data["passive"]
    
    def get_splash_screen_image(self):
        if self.is_valid:
            return f'{LConst.CHAMPION_SPLASH_URL}/{self.name}_0.jpg'
        return 'Champion not found'

    # def getSkins(self):
    #     if not self.checkValid():
    #         skins = []
    #         for i in self.info[3]:
    #             skins.append({i['name']:i['num']})
    #         return skins
    #     return 'Champion not found'