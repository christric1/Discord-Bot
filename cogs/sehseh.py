import discord
import requests
import json
import re

from discord.ext import commands 
from config import settings


class Sehseh(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # async def seh(self, ctx, name="紅村"):
    #     """搜尋本本 (紳士漫畫)"""

    #     r = requests.get(settings["root"] + f"getHentai?name={name}")
    #     data = json.loads(r.text)

    #     embed=discord.Embed(title=name, color=0x118845)
    #     for index, i in enumerate(data):
    #         embed.add_field(name=str(index+1)+". "+i["title"], value=i["src"], inline=False)
    #     embed.set_thumbnail(url="https://i.imgur.com/5cDx2fG.png")
    #     embed.set_footer(text="NTRの戦士")
    #     await ctx.send(embed=embed)

    @commands.command()
    async def random(self, ctx):
        """隨機本子 (nhentai)"""

        await ctx.send("https://nhentai.net/random")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        """神の數字"""

        # 排除自己的訊息，避免陷入無限循環
        if message.author == self.bot.user or message.content.startswith("https"):
            return

        # 找所有數字
        pattern = r'(w|n|jm)(\d{5,8})'
        matches = re.findall(pattern, message.content, re.I)
        for match in matches:
            prefix, num = match
            prefix = prefix.lower()
            
            if prefix == 'w':
                await message.channel.send(f'https://www.wnacg.com/photos-index-aid-{num}.html')
            elif prefix == 'jm':
                await message.channel.send(f'https://18comic.vip/album/{num}')
            elif prefix == 'n':
                await message.channel.send(f'https://nhentai.net/g/{num}')
        

async def setup(bot):
    await bot.add_cog(Sehseh(bot))
