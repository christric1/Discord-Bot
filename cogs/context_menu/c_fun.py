import discord
from discord import app_commands
from discord.ext import commands

import requests
from requests.exceptions import RequestException
import json
from config import settings
from urllib.parse import quote


class CFun(commands.Cog):
    """Fun"""

    def __init__(self, bot) -> None:
        self.bot = bot
        self.ctx_menu = app_commands.ContextMenu(
            name="sehseh",
            callback=self.quote,
        )
        self.bot.tree.add_command(self.ctx_menu)

    async def quote(self, interaction: discord.Interaction, message: discord.Message) -> None:
        await interaction.response.defer()  # 延遲互動回應以延長時間限制

        if message.attachments:
            for attachment in message.attachments:
                if attachment.content_type.startswith('image/'):
                    encoded_url = quote(attachment.url, safe='') 
                    try:
                        r = requests.get(settings["root"] + f"getImageHentai?url={encoded_url}")
                        r.raise_for_status()
                        data = json.loads(r.text)
                        
                    except RequestException as e:
                        print(f"請求失敗: {e}")
                        await interaction.followup.send("處理圖片失敗。")
                        data = None

                    embed=discord.Embed(title="馬哥の草", color=0x118845)
                    for index, i in enumerate(data):
                        embed.add_field(name=str(index+1)+". "+i["title"], value=i["src"], inline=False)
                    embed.set_thumbnail(url="https://i.imgur.com/HtLNVb8.png")
                    embed.set_footer(text="NTRの戦士")
                    await interaction.followup.send(embed=embed)
            return
        
        await interaction.followup.send("It's not a image.")


async def setup(bot):
    await bot.add_cog(CFun(bot))