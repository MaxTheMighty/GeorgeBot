import json

fixed = {}
with open("gameInfo.json",encoding="utf8",mode="r+") as jsonFile:
    broken = json.load(jsonFile)

broken = broken['applist']['apps']

for item in broken:
    gameID = item["appid"]
    gameName: str = item['name']
    gameName = gameName.lower().replace(" ","").replace("-","")
    #print(fixedDict)
    fixed.update({gameName:gameID})


print(fixed.__len__())
with open("fixed.json",encoding="utf8",mode="w+") as fixedJsonFile:
    json.dump(fixed,fixedJsonFile,indent=1)