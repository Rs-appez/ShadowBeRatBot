from discord import Interaction, slash_command
from nextcord.ext import commands
from nextcord import Attachment
from bot.models.vpn.vpn import Vpn

class VPN(commands.Cog):
    """VPN cmd"""
    def __init__(self,bot):
        self.bot = bot
        self.vpn = Vpn(bot)

    @slash_command(description="set vpn connection" ,dm_permission=False)
    async def set_vpn(self,interaction : Interaction, vpn_file : Attachment):
        await interaction.response.defer(with_message=True)
        await self.vpn.setup(interaction,vpn_file)


    @slash_command(description="start vpn connection",dm_permission=False )
    async def start_vpn(self,interaction : Interaction):
            await interaction.response.defer(with_message=True)
            await self.vpn.start(interaction)

    @slash_command(description="stop vpn connection" ,dm_permission=False)
    async def stop_vpn(self,interaction : Interaction):
        await interaction.response.defer(with_message=True)
        await self.vpn.stop(interaction)


        
  

def setup(bot):
    bot.add_cog(VPN(bot))