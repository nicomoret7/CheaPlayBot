import os
import discord
from time import sleep
from dotenv import load_dotenv
from discord.ext import commands

from scraper.scraper import scrap

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('PREFIX')

client = discord.Client()
bot = commands.Bot(command_prefix=PREFIX)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='price')
async def price(ctx):
    # Build the message
    game = ' '.join(ctx.message.content.split(' ')[1:])
    embedMsg = discord.Embed(title="Prices for %s:" % game,
                             description="Waiting for results",
                             colour=0x4B0082)
    sent = await ctx.send(embed=embedMsg)

    # Retrieve the info
    data = '\n'.join(["- **%s**: %s" % (site["name"], site["price"]) for site in scrap(game)])
    embedMsg.description = data
    await sent.edit(embed=embedMsg)


bot.run(TOKEN)
