from discord import Interaction, slash_command
from nextcord.ext import commands
from bot.models.enum.nmap import Nmap

class Enum(commands.Cog):
    """Enum cmd"""
    def __init__(self,bot):
        self.bot = bot
        self.enable = False

        self.cmd_dict = {"nmap" : self.__nmap}
    
    @commands.is_owner()
    @commands.command()
    async def enable_enum(self,ctx : commands.Context,enable : bool):
        self.enable = enable

    async def __check_authorization(self,interaction,cmd,args = None):
        if not self.enable :
            await interaction.response.send_message("Enum cmd not enable")
        else :
            await self.cmd_dict[cmd](interaction,args)

    @slash_command(name='nmap',description="perform a nmap scan",dm_permission=False )
    async def nmap_cmd(self,interaction : Interaction, ip : str):
        await self.__check_authorization(interaction, "nmap",ip)      

    async def __nmap(self,interaction,ip):
        try :
            nmap = Nmap(ip)
            await interaction.response.defer(with_message=True)
            await nmap.scan(interaction)

        except TypeError:
            await interaction.response.send_message("Error in IP")

        
        
  

def setup(bot):
    bot.add_cog(Enum(bot))