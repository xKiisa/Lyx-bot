import random
from discord.ext import commands


class Games(commands.Cog):
    def _init_(self, bot):
        self.bot = bot

    @commands.command()
    async def rps(self, ctx, *, member_choice=None):
        ''' "Rock Paper Scissors" '''
        choices = ["rock", "paper", "scissors"]
        bot_choice = random.choice(choices)
        member_choice = member_choice.lower()

        if member_choice == bot_choice:
            await ctx.send(f"{ctx.message.author.mention} it's a tie! we both got **{bot_choice}**.")

        elif member_choice == "rock" and bot_choice == "scissors" \
                or member_choice == "scissors" and bot_choice == "paper" \
                or member_choice == "paper" and bot_choice == "rock":
            await ctx.send(f"{ctx.message.author.mention} You picked **{member_choice}** "
                                                        f"and I picked **{bot_choice}**!\nYou won!")

        elif (member_choice == "scissors" and bot_choice == "rock") \
                or (member_choice == "paper" and bot_choice == "scissors") \
                or (member_choice == "rock" and bot_choice == "paper"):
            await ctx.send(f"{ctx.message.author.mention} You picked **{member_choice}** "
                                                        f"and I picked **{bot_choice}**!\nYou lost!")
        else:
            await ctx.send(f"{ctx.message.author.mention} Something went wrong. "
                                                        "Please enter one of the following\n"
                                                        "`rock`, `paper`, `scissors`")


async def setup(bot):
    await bot.add_cog(Games(bot))
