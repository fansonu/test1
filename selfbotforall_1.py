import discord
from discord.ext import commands
import asyncio
SELF_BOT_TOKEN = "NTkwMzk2Mjg2NjkyNDkxMjY2.XbOggg.1H0TSojfD44Mvqv3A-F6RitmSuE"
selfbot = commands.Bot(command_prefix='$$$$$$')



@selfbot.event
async def on_ready():
    print("ONLINE")
    while True:
        await selfbot.change_presence(game=discord.Game(name='members of server name',type = 1,url = "https://twitch.tv/myname"))
        await asyncio.sleep(10)
        await selfbot.change_presence(game=discord.Game(name='members of server name',type = 1,url = "https://twitch.tv/myname"))
        await asyncio.sleep(10)
        await selfbot.change_presence(game=discord.Game(name='members of server name',type = 1,url = "https://twitch.tv/myname"))
        await asyncio.sleep(10)
        await selfbot.change_presence(game=discord.Game(name='members of server name',type = 1,url = "https://twitch.tv/myname"))
        await asyncio.sleep(10)
        await selfbot.change_presence(game=discord.Game(name='members of server name',type = 1,url = "https://twitch.tv/myname"))
        await asyncio.sleep(10)
        await selfbot.change_presence(game=discord.Game(name='members of server name',type = 1,url = "https://twitch.tv/myname"))
        await asyncio.sleep(10)
        await selfbot.change_presence(game=discord.Game(name='members of server name',type = 1,url = "https://twitch.tv/myname"))
        await asyncio.sleep(10)



selfbot.run(SELF_BOT_TOKEN,bot=False)
