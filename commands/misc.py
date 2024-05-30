import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
owner_id = os.getenv("OWNER")


class Misc(commands.Cog):
    def _init_(self, bot):
        self.bot = bot

    @commands.command()
    async def owner(self, ctx):
        ''' "Shows the bot owners ID" '''
        await ctx.send(f"{ctx.message.author.mention} The ID of the bot owner is: `{owner_id}`")


async def setup(bot):
    await bot.add_cog(Misc(bot))
