from discord import Interaction, slash_command
from nextcord.ext import commands
from bot.models.housekeeper.scheduler import Scheduler

class Housekeeper(commands.Cog):
    """Housekeeper cmd"""
    def __init__(self,bot):
        self.bot = bot
        self.scheduler = Scheduler()

        
def setup(bot):
    bot.add_cog(Housekeeper(bot))