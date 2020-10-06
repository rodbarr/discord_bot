import discord
import config as conf
import codewarsapi as api

client = discord.Client()

@client.event
async def on_message(m):
    m.content = m.content.lower()
    if m.author == client.user:
        return
    if m.content.startswith(f"{conf.TRIGGER}help"):
        await m.channel.send(f"{conf.TRIGGER}user <username> will get the data of the user")
    if m.content.startswith(f"{conf.TRIGGER}user"):
        await m.channel.send("user data")
        #user = m.content.remove(f"{conf.TRIGGER}user")
        #await m.channel.send(user)
client.run(conf.DISCORD_TOKEN)
