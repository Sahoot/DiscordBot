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

@bot.command(brief='finishes the word')
async def test(ctx):
    await ctx.send('osterone')

@bot.command(breif='gives a famous quote')
async def quote(ctx):
   quote_file = open('quotes.txt', 'r') 
   quotes = quote_file.read().split('\n')
   quote_file.close()
   if len(quotes) < 1:
       await ctx.send('nothing here :(')
   else:
       await ctx.send(f'***{quotes[random.randint(0, len(quotes)-1)]}***')

@bot.command(brief='adds to the list of famous quotes')
@commands.has_permissions(administrator=True)
async def addquote(ctx, quote):
    if not quote:
        return
    quote = ctx.message.content.strip(bot.command_prefix + ctx.invoked_with + ' ')
    with open("quotes.txt", "a") as quote_file:
        quote_file.write("\n")
        quote_file.write(quote)
    await ctx.send(f'***{quote}*** added to list of quotes')

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    bruh_file = open('bruh.txt', 'r')
    bruh_list = bruh_file.read().split(',')
    bruh_file.close()
    if any(ext in message.content for ext in bruh_list):
        await message.channel.send('***bruh***', tts=True)

@bot.event
async def on_ready():
    print('ready bot go')

bot.run(TOKEN)