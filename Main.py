import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
owner_id = os.getenv("OWNER")
print(TOKEN)
print(GUILD)
print(owner_id)

client = discord.Client(intents=discord.Intents.all())
intents = discord.Intents.all()

# Profile status
status = discord.Status.dnd
activity = discord.Activity(type=discord.ActivityType.listening,
                            name="!help | Lyx Bot  ")

bot = commands.Bot(command_prefix="!",
                   case_insensitive=True,
                   intents=intents,
                   status=status,
                   activity=activity)

extensions = [
    "commands.fun",
    "commands.games",
    "commands.misc",
]


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")
    for extension in extensions:
        await bot.load_extension(extension)


bot.run(TOKEN)
