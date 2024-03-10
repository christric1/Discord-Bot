import requests
import json
import pytz
import datetime

from config import settings
from discord.ext import commands 


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hulan(self, ctx, topic="馬哥", len="100"):
        """唬爛造句"""

        r = requests.get(settings["root"] + f"hulan?topic={topic}&len={len}")
        data = json.loads(r.text)
        await ctx.send(data['text'])

    @commands.command()
    async def drawLots(self, ctx):
        """抽淺草寺籤"""

        r = requests.get(settings["root"] + "drawLots")
        data = json.loads(r.text)
        await ctx.send(data['src'])

    @commands.command()
    async def checkTime(self, ctx):
        """軍人對錶"""

        # 獲取當下台灣時間
        taiwan_timezone = pytz.timezone('Asia/Taipei')
        current_time_taiwan = datetime.datetime.now(taiwan_timezone)
        
        # 格式化時間為 HH:mm
        formatted_time = current_time_taiwan.strftime("%H:%M")

        # 定義軍中數字映射
        military_numbers = {'0': '洞', '1': '夭', '2': '兩', '3': '三', '4': '四', '5': '五', '6': '六', '7': '拐', '8': '八', '9': '勾'}
        formatted_time_military = ''.join([military_numbers[char] for char in formatted_time if char != ':'])

        await ctx.send(f"現在時間: {formatted_time_military}")
    
    @commands.command(name='馬哥')
    async def _list(self, ctx):
        """馬哥吃草"""
        
        await ctx.send("馬哥吃草")

async def setup(bot):
    await bot.add_cog(Fun(bot))