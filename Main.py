import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
print(TOKEN)
print(GUILD)

client = discord.Client(intents=discord.Intents.all())
intents = discord.Intents.all()

# Profile status
status = discord.Status.dnd
activity = discord.Activity(type=discord.ActivityType.listening,
                            name="!help | Lyx Bot  ")


bot = commands.Bot(command_prefix="!",
                   intents=intents,
                   status=status,
                   activity=activity)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# Bot commands
@bot.command(name="dice",
             help="Enter amount of rolls and sides")
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(ctx.message.author.mention + " rolled " + ", ".join(dice) + "!")


@bot.command(name="coinflip",
             help="Flip a coin")
async def coin(ctx):
    coinflip = [
        random.choice((" Heads", " Tails"))
    ]
    await ctx.send(ctx.message.author.mention + "".join(coinflip) + "!")


@bot.command(name="rate",
             help="Rate your cuteness")
async def rate(ctx, *, member: discord.Member = None):
    if member is None:
        member = ctx.author
    ratecuteness = [
        str(random.choice(("a 1", "a 2", "a 3", "a 4", "a 5", "a 6", "a 7", "an 8", "a 9", "a 10")))
    ]
    await ctx.send(member.mention + " is " + "".join(ratecuteness) + " on the cuteness scale!")

bot.run(TOKEN)
