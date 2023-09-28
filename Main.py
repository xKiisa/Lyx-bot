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


status = discord.Status.dnd
activity = discord.Activity(type=discord.ActivityType.listening, name="!help | Lyx Bot  ")


intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents, status=status, activity=activity)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name="dice", help="Enter amount of rolls and sides")
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(", ".join(dice))


@bot.command(name="coinflip", help="Flip a coin")
async def coin(ctx):
    coinflip = [
        random.choice(("Heads", "Tails"))
    ]
    await ctx.send("".join(coinflip))


bot.run(TOKEN)
