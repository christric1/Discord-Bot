import discord
import os
import asyncio

from config import settings
from discord.ext import commands, tasks
from cogs import fun, sehseh, update, help


# client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=settings["prefix"], intents=intents)

# module starting
asyncio.run(fun.setup(client))
asyncio.run(help.setup(client))
asyncio.run(sehseh.setup(client))
asyncio.run(update.setup(client))

print("Starting a bot. It may take a few seconds")

client.run(settings["token"]) 