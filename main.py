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

# 馬哥吃草
@client.command(name='馬哥')
async def _list(ctx):
    await ctx.channel.send("馬哥吃草")

# 隨機本子
@client.command()
async def random(ctx):
    await ctx.channel.send("https://nhentai.net/random")

# 唬爛造句
@client.command()
async def hulan(ctx, topic, len):
    try:
        r = requests.get("https://fastapi-selenium-production-8ccc.up.railway.app/hulan?topic={topic}&len={len}")
        data = json.loads(r.text)
        await ctx.channel.send(data['text'])
    except:
        await ctx.channel.send("something went wrong.")

@client.event
async def on_ready():
    print("Bot in ready")

# 當有訊息時
@client.event
async def on_message(message):
    # 排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return

    # 找所有數字
    numbers = re.findall(r"\d+", message.content)
    for num in numbers:
        if len(num) == 6:
            await message.channel.send('https://nhentai.net/g/' + num)

client.run(os.environ["DISCORD_TOKEN"]) 