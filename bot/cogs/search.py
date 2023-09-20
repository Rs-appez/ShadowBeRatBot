from discord import Interaction, slash_command
from nextcord.ext import commands

EXPLOITDB_URL = "https://www.exploit-db.com/search?cve="

class Search(commands.Cog):
    """Search cmd"""
    def __init__(self,bot):
        self.bot = bot

    @slash_command(name='exploitdb_search_cve',description="Search the CVE on exploit db" )
    async def exploitdb_CVE(self,interaction : Interaction, cve : str):
        if cve.startswith("CVE-"):
            cve = cve[4:]
        await interaction.response.send_message(EXPLOITDB_URL + cve)
  

def setup(bot):
    bot.add_cog(Search(bot))