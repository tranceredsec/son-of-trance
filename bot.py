import discord
import asyncio
import time

client = discord.Client()


@client.event
async def on_ready():
    print('[+] Username: ' + str(client.user.name))


@client.event
async def on_message(message):
    if message.content.startswith("$ping"):
        await client.send_message(message.channel, "Pong! :ping_pong:")
        
@client.event
async def on_message(message):
    if message.content.startswith("$info"):
        await client.send_message(print(discord.AppInfo))
        
@client.event
async def on_message(message):
    if message.content.startswith("$whoisskelly"):
        await client.send_message(message.channel, "https://i.pinimg.com/originals/e1/46/d0/e146d0ef3cad5e6ede22901c2107412d.jpg")
        
        
client.run('NDEwMjQxNTQ5NjE2Njc2ODc1.DVrDYQ.ysPEDq-A32Ai-GtoeZ_bIvkjAVM')
