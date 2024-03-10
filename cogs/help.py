import discord
from discord.ext import commands
from config import settings


class HelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        self.no_category = None
        destination = self.get_destination()

        for page in self.paginator.pages:
            embed = discord.Embed(color=0xffcd4c, title='幫助', description=page)
            embed.set_thumbnail(url="https://i.imgur.com/hl9iTQB.png")
            embed.set_footer(text="CCSUE, the best professor, from NCKU")
            await destination.send(embed=embed)

    def get_opening_note(self) -> str:
        return (
            f"**📙 前綴: `{settings.get('prefix')}`**\n"
            f"📙 使用 `{settings.get('prefix')}help` 以顯示命令列表\n"
            f"📙 使用 `{settings.get('prefix')}help` `命令名稱` 以獲取命令的詳細說明")

async def setup(bot):
    bot.help_command = HelpCommand()
