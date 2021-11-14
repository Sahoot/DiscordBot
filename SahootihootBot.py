import os
from pathlib import Path
import discord
from discord.ext import commands
#from discord.ext import has_permissions
from dotenv import load_dotenv
import random

#getting bot token from env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='~', description='This is an inside joke bot')

@bot.command()
async def test(ctx):
    await ctx.send('osterone')

@bot.command()
async def quote(ctx):
   quote_file = open('quotes.txt', 'r') 
   quotes = quote_file.read().split(',')
   if len(quotes) < 1:
       await ctx.send('nothing here :(')
   else:
       await ctx.send(quotes[random.randint(0, len(quotes)-1)])

# @bot.command()
# async def clean_quotes(ctx):
#     await ctx.send('sab kam mehi karu?')

@bot.event
async def on_ready():
    print('ready bot go')

bot.run(TOKEN)