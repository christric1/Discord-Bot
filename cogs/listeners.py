import random
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound, MissingPermissions, MemberNotFound, MissingRequiredArgument
from config import settings


class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()

        print('[b green]Bot is ready! Just type d.help to see all bot commands.')
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game("reading paper.."))


async def setup(bot):
    await bot.add_cog(OnReady(bot))