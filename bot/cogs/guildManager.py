from discord import Interaction, slash_command
from nextcord.ext import commands

from bot.models.guildManager.channelManager import ChannelManager

class GuildManager(commands.Cog):
    """Guild manager cmd"""
    def __init__(self,bot):
        self.bot = bot

    @slash_command(description="Clean all enum channel",dm_permission=False )
    async def purge_enum_channel(self,interaction : Interaction):
        await ChannelManager.purge_enum_channel(interaction)
        await interaction.response.defer(with_message=True,ephemeral=True)

    @slash_command(description="Remove all threads in this channel",dm_permission=False )
    async def purge_threads(self,interaction : Interaction):
        await interaction.response.defer(with_message=True,ephemeral=True)
        await ChannelManager.purge_threads(interaction)

def setup(bot):
    bot.add_cog(GuildManager(bot))