import functools
import os
import re
import discord
import logging
from dotenv import load_dotenv
from discord.ext import commands
import typing
# from scraper.scraper import scrap # Not threaded
from scraper.scraperThreaded import scrap

# Logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Bot config
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('PREFIX')

client = discord.Client()
bot = commands.Bot(command_prefix=PREFIX)


@bot.event
async def on_ready():
    logging.info(f'%s has connected to Discord!' % bot.user.name)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = f"This command is in cooldown, try again in %.2f seconds" % error.retry_after
        logging.warning(msg)
        await ctx.send(msg)
        return


async def run_blocking(blocking_func: typing.Callable, *args, **kwargs) -> typing.Any:
    """Runs a blocking function in a non-blocking way"""
    # `run_in_executor` doesn't support kwargs, `functools.partial` does
    func = functools.partial(blocking_func, *args, **kwargs)
    return await client.loop.run_in_executor(None, func)


@bot.command(name='price')
@commands.cooldown(1, 15)
async def price(ctx):
    logging.info("User %s issued: %s" % (ctx.author, ctx.message.content))
    game = re.sub(r"[^a-zA-Z0-9\s]", "", ctx.message.content)  # Sanitize input
    game = re.sub(r"[^\s]+\s", "", game, count=1)  # Crop command

    # Build the embed message
    embedMsg = discord.Embed(title="Prices for %s:" % game,
                             description="Waiting for results",
                             colour=0x4B0082)
    sent = await ctx.send(embed=embedMsg)

    # Retrieve the info
    results = await run_blocking(scrap, game)
    data = '\n'.join(["- **%s**: %s" % (site["name"], site["price"]) for site in results])
    embedMsg.description = data
    await sent.edit(embed=embedMsg)


bot.run(TOKEN)
