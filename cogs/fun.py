import discord

from .utils import checks
from discord.ext import commands

class Fun:
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Fun(bot))