import os
from pathlib import Path
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random

#getting bot token from env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='~', description='This is an inside joke bot')

@bot.command()
async def test(ctx):
    await ctx.send('osterone')

@bot.event
async def on_ready():
    print('ready bot go')

bot.run(TOKEN)