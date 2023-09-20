
from discord import Interaction


class ChannelManager():

    @staticmethod
    async def purge_threads(interaction : Interaction):
        for thread in interaction.channel.threads:
            await thread.delete()

        await interaction.followup.send(content="done !",ephemeral=True)

    @staticmethod
    async def purge_enum_channel(interaction : Interaction):
        pass