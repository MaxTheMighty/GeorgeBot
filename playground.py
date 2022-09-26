import json


with open("staticGameData.json",encoding="utf8",mode="r+") as jsonFile:
    database = json.load(jsonFile)



def findId(gameName):
    fixedGameName = gameName.lower().replace(" ","")
    return database[fixedGameName]


print(findId("blazblue crosstag battle"))
print(findId("tekken 7"))
print(findId("street fighter v"))
print(findId("STREET FIGHTER V"))