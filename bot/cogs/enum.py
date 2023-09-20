from discord import Interaction, slash_command
from nextcord.ext import commands
from bot.models.enum.nmap import Nmap
from bot.models.enum.sanitize import Sanitize

class Enum(commands.Cog):
    """Enum cmd"""
    def __init__(self,bot):
        self.bot = bot

    @slash_command(description="perform a nmap scan" )
    async def nmap(self,interaction : Interaction, ip : str):
        try :
            ip_san = Sanitize.ip(ip)
            await interaction.response.defer(with_message=True)
            await Nmap(ip_san).scan(interaction)
        except TypeError:
            await interaction.response.send_message("Error in IP")
        
        
  

def setup(bot):
    bot.add_cog(Enum(bot))