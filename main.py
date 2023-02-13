import discord
from discord.ext import commands
import requests
import os
import re
import json


# client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='$', intents=intents)

# root website
root = "https://fastapi-selenium-production-8ccc.up.railway.app/"

# 馬哥吃草
@client.command(name='馬哥')
async def _list(ctx):
    await ctx.send("馬哥吃草")

# 隨機本子
@client.command()
async def random(ctx):
    await ctx.send("https://nhentai.net/random")

# 唬爛造句
@client.command()
async def hulan(ctx, topic="馬哥", len="100"):
    try:
        r = requests.get(root + f"hulan?topic={topic}&len={len}")
        data = json.loads(r.text)
        await ctx.send(data['text'])
    except:
        await ctx.send("something went wrong.")

# 抽神籤
@client.command()
async def drawLots(ctx):
    try:
        r = requests.get(root + "drawLots")
        data = json.loads(r.text)
        await ctx.send(data['src'])
    except:
        await ctx.send("something went wrong.")

# 想澀澀
@client.command()
async def sehseh(ctx, name="紅村"):
    try:
        r = requests.get(root + f"getHentai?name={name}")
        data = json.loads(r.text)

        embed=discord.Embed(title=name, color=0x118845)
        for i in data:
            embed.add_field(name=i["title"], value=i["src"], inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("something went wrong.")

@client.event
async def on_ready():
    print("Bot in ready")

# 當有訊息時
@client.event
async def on_message(message):
    # 排除自己的訊息，避免陷入無限循環
    if message.author == client.user or message.content.startswith("https"):
        return

    # 找所有數字  
    numbers = re.findall(r"\d+", message.content)
    for num in numbers:
        if len(num) == 6:
            await message.channel.send('https://nhentai.net/g/' + num)

    await client.process_commands(message)

client.run(os.environ["DISCORD_TOKEN"]) 