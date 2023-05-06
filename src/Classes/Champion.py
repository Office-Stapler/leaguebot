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