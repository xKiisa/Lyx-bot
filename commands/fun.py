import discord
import random
from discord.ext import commands


class Fun(commands.Cog):
    def _init_(self, bot):
        self.bot = bot

    @commands.command()
    async def coinflip(self, ctx):
        ''' "Flips a coin" '''
        coinflip = [
            random.choice((" Heads", " Tails"))
        ]
        await ctx.send(f"ctx.message.author.mention  {"".join(coinflip)} !")

    @commands.command()
    async def dice(self, ctx, number_of_dice: int, number_of_sides: int):
        ''' "Enter amount of rolls and sides (e.g. 6 or 20)" '''
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]
        await ctx.send(f"{ctx.message.author.mention} rolled {", ".join(dice)} !")

    @commands.command()
    async def rate(self, ctx, *, member: discord.Member = None):
        """ Rates how cute you are"""
        if member is None:
            member = ctx.author
        ratecuteness = [
            str(random.choice(("a 1", "a 2", "a 3", "a 4", "a 5", "a 6", "a 7", "an 8", "a 9", "a 10")))
        ]
        await ctx.send(f"{member.mention} is {"".join(ratecuteness)} on the cuteness scale!")


async def setup(bot):
    await bot.add_cog(Fun(bot))
