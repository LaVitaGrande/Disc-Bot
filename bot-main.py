import discord
import os
from discord.ext import commands
from random import choice

import dice,text

""" Main loop for the DnD bot.

Will be for event and command tracking.  Anything more than a line or two will
be offloaded into modules to keep this clean.

List of modules:
dicord.py  -  imported from pip
dice.py    -  dice rolling functions
text.py    -  ugly way to store large text strings for importing here
"""

""" Loads .env in memory as os varials, used for local testing.
uncomment when running locally
from dotenv import load_dotenv
load_dotenv()"""


KEY = os.getenv("KEY")
CHANNELS = os.getenv("CHANNELS")

""" DM and CONTENT aren't used right now.  Forward looking for when there are DM specific
commands and a way to load remote content.  """
DM = os.getenv("DM")
CONTENT = os.getenv("CONTENT")

client = commands.Bot(command_prefix= '!')

@client.event
async def on_ready():
    print('Do you feel lucky?')

@client.command()
async def roll(ctx, *, query="1d20"):
    """Responds to dice roll query in XdY+Z format"""
    if str(ctx.channel) in CHANNELS or 'Direct Message' in str(ctx.channel):
        if query == "help":
            await ctx.send(f'{text.help[str(ctx.command)]}')
        else:
            await ctx.send(f'{ctx.author.name} rolled a {dice.request_reponse(query)}')
    else:
        await ctx.send(f'This is not an appropriate venue for playing games!')

@client.command()
async def advantage(ctx, *, query="0"):
    """Rolls 2 twenty sided dice and returns the higher value."""
    if str(ctx.channel) in CHANNELS or 'Direct Message' in str(ctx.channel):
        if query == "help":
            await ctx.send(f'{text.help[str(ctx.command)]}')
        else:
            await ctx.send(f'{choice(text.advantage)}')
            await ctx.send(f'{ctx.author.name} rolled a {max(dice.request_reponse(query), dice.request_reponse(query))}')
    else:
        await ctx.send(f'This is not an appropriate venue for playing games!')

@client.command()
async def disadvantage(ctx, *, query="0"):
    """Rolls 2 twenty sided dice and returns the lower value."""
    if str(ctx.channel) in CHANNELS or 'Direct Message' in str(ctx.channel):
        if query == "help":
            await ctx.send(f'{text.help[str(ctx.command)]}')
        else:
            await ctx.send(f'{choice(text.disadvantage)}')
            await ctx.send(f'{ctx.author.name} rolled a {min(dice.request_reponse(query), dice.request_reponse(query))}')
    else:
        await ctx.send(f'This is not an appropriate venue for playing games!')

@client.command()
async def dndhelp(ctx, *, query=''):
    """Outputs general help for DnD bot."""
    if str(ctx.channel) in CHANNELS or 'Direct Message' in str(ctx.channel):
        if query == "help":
            await ctx.send(f'{text.help[str(ctx.command)]}')
        else:
            await ctx.send(f'{text.help_text}')
    else:
        await ctx.send(f'This is not an appropriate venue for playing games!')

@client.command()
async def showcontext(ctx, *, query=''):  
    """Shows context of input from channel.
    
    Mostly used in troubleshooting code."""
    if str(ctx.channel) in CHANNELS or 'Direct Message' in str(ctx.channel):
        if query == "help":
            await ctx.send(f'{text.help[str(ctx.command)]}')
        else:
            await ctx.send(f'The author is:{ctx.author}')
            await ctx.send(f'The channel is:{ctx.channel}')
            await ctx.send(f'The command is:{ctx.command}')
    else:
        await ctx.send(f'This is not an appropriate venue for playing games!')

client.run(KEY)
