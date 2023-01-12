import discord
from discord.ext import commands
import os
import re


# client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='$', intents=intents)

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

    # 隨機本子
    if message.content.startswith('$random'):
        await message.channel.send('https://nhentai.net/random')


client.change_presence(status=discord.Status.idle, activity="reading papers")
client.run(os.environ["DISCORD_TOKEN"]) 