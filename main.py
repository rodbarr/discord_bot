import discord
from discord.ext import commands
import config as conf
import codewarsapi as api

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)

@bot.command(help = "This command displays the stats of the specified user", usage = "<codewars username>")
async def user(ctx, *, arg):
    cw = api.getUser(arg)
    await ctx.send(f"User: {arg}\n Honor: {cw['honor']}\n Rank: {cw['ranks']['overall']['name']}")
    
bot.run(conf.DISCORD_TOKEN)