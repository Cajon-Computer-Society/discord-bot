import asyncio
import discord

from .utils import checks
from discord.ext import commands

class Moderation:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True, aliases=["purge", "delete", "remove"])
    @checks.mod_or_permissions(manage_messages=True)
    async def cleanup(self, ctx):
        """Removes messages from the current channel"""
        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid parameter passed "{0.subcommand_passed"'.format(ctx))

    @cleanup.command(pass_context=True, name='all')
    async def _all(self, ctx, ammount : int = 50):
        try:
            await self.bot.purge_from(ctx.message.channel, limit=ammount)
        except discord.errors.NotFound:
            pass

        await self.bot.say("Deleted {} messages".format(ammount), delete_after=5)
    
    #@commands.command(pass_context=True)
    #async def rekt(self, ctx):
    #    """The best command in the world"""
    #    user = ctx.message.author.name
    #    await self.bot.say("{e}\N{PISTOL} ".format(e=user))
    #    await self.bot.say("{} just got rekt".format(user))

def setup(bot):
    bot.add_cog(Moderation(bot))