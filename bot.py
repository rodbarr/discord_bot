import os
import discord
import time
from dotenv import load_dotenv
from datetime import datetime
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix="/", intents=discord.Intents.default())


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name="add_meeting", help="Use this command to set up a meeting on the shared calendar")
async def add_meeting(ctx, arg):
    # d = datetime.strptime(dateInput, '%Y-%m-d')
    # t = time.strptime(timeInput, '%H:%M')
    # print('date: ' + d, 'time: ' + t)
    # await ctx.send("Metting "set up for " + dateInput + " at " + timeInput)
    await ctx.channel.send('Wenas noches')

bot.run(TOKEN)
