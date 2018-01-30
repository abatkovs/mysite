'''
Created on 30 Jan 2018

@author: Arnolds
'''
import discord
import asyncio
from discord.ext import commands
import random

from lol.lol_rw import lol_summoner


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix=';', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

"""
c = 0
for i in e:
    if e[c]['queueType'] == 'RANKED_FLEX_SR':
        print('Queue type is solo')
    else:
        print('Queue type is ' + e[c]['queueType'])
    c += 1
c=0
"""


@bot.command(description='Registers your summoner ";summoner region summonername"')
async def summoner(region: str, *name: str):
    n = ''
    if(len(name)> 1):
        for i in name:
            n = n + " " + i
    else:
        n = name[0]
    print(n)
    if region == 'eune':
        region = 'eun1'
    lol = lol_summoner()
    lol.my_region = region
    answer = lol.rank(n)
    """Adds two numbers together."""
    
    await bot.say(answer)

bot.run('qq')