
import pathlib
import json
import requests
import discord
from dotenv import load_dotenv
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
load_dotenv(dotenv_path=pathlib.Path("./keys.env"))

with open("staticGameData.json","r+") as jsonFile:
    jsonData = json.load(jsonFile)



POPULAR_GAME_IDS = []


@bot.command()
async def getPlayers(ctx):
    embedOut = discord.Embed()
    steamGameName = ctx.message.clean_content[12:]
    steamGameId = await getIDFromName(steamGameName)
    steamGameDataPack = (steamGameName,steamGameId)
    if(steamGameName==""):
        pass
        #embedOut = await createEmbedFromGames(popularGameIDs)
    else:
        steamGameId = await getIDFromName(steamGameName)
        embedOut = await createEmbedFromGames([steamGameDataPack])
        
    await ctx.send(embed = embedOut)



async def getPlayerCountForGame(steamId: str) -> str:
    request = requests.get(f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1?appid={steamId}")
    json = request.json()
    print(json)
    playerCount = json['response']['player_count']
    return playerCount




# TODO make the string creation neater
async def createEmbedFromGames(gameList: list) -> discord.Embed:
    embedOut = discord.Embed(title="Game stats")
    #gameStatsField = ""
    for gameDataPack in gameList:
        gameName = gameDataPack[0]
        gameId = gameDataPack[1]
        gameStat = await getPlayerCountForGame(gameId)
        #gameStatsField += f"{gameName}:{gameStat}\n"
        embedOut.add_field(name = gameName,value= gameStat)
    # \u200b is a zero width space. this is a crime
    #embedOut.add_field(name="\u200b",value = gameStatsField)
    return embedOut


async def getIDFromName(gameName: str) -> str:
    
    fixedGameName = gameName.lower().replace(" ","")
    return jsonData[fixedGameName]


bot.run(os.getenv("KEY"))




#if __name__ == '__main__':
  #  print("Bot active!")
  #  print(discord.__version__)
    
    