import os

import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bro = {'bruh', 'bro', 'breh', 'bruv'}

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '~help':
        await message.channel.send('chup!')
    
    for x in bro:
        if x.lower() in message.content.lower():
            await message.channel.send('bruh')
            break

client.run(TOKEN)