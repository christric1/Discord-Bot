import discord
from discord import app_commands
from discord.ext import commands

import requests
import json
from config import settings


class CFun(commands.Cog):
    """Fun"""

    def __init__(self, bot) -> None:
        self.bot = bot
        self.ctx_menu = app_commands.ContextMenu(
            name="sehseh",
            callback=self.quote,
        )
        self.bot.tree.add_command(self.ctx_menu)

    async def quote(self, interaction: discord.Interaction, message: discord.Message):
        if message.attachments:
            for attachment in message.attachments:
                if attachment.content_type.startswith('image/'):
                    r = requests.get(settings["root"] + f"getImageHentai?url={attachment.url}")
                    data = json.loads(r.text)

                    embed=discord.Embed(title="馬哥の草", color=0x118845)
                    for index, i in enumerate(data):
                        embed.add_field(name=str(index+1)+". "+i["title"], value=i["src"], inline=False)
                    embed.set_thumbnail(url="https://i.imgur.com/5cDx2fG.png")
                    embed.set_footer(text="NTRの戦士")
                    await interaction.response.send_message(embed=embed)
            return
                  
        await interaction.response.send_message("It's not a image.")


async def setup(bot):
    await bot.add_cog(CFun(bot))