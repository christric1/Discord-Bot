from discord.ext import commands


class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def update(self, ctx):
        """更新日誌"""

        update_list_str = """```
**112/7/22**
- 新增更新日誌 
- 被動指令的 jim 改成 jm, 且不分大小寫

**112/8/15**
- 修復 sehseh 功能 (之前紳士漫畫網域更換)

**113/2/3**
- 增加洞六洞洞起床
- 增加對錶報時間

**113/5/31**
- 增加搜圖APP```"""

        await ctx.send(update_list_str)


async def setup(bot):
    await bot.add_cog(Update(bot))