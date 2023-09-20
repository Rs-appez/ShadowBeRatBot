import nextcord
from nextcord.ext import commands
import config
from nextcord import CustomActivity

class SbrBot(commands.Bot):

    def __init__(self, command_prefix):

        self.voice_client = None
        intents = nextcord.Intents.default()
        intents.members = True
        intents.voice_states = True
        intents.message_content = True
        super().__init__(command_prefix, intents=intents,activity=None)

    async def on_ready(self):
        print(f"{self.user.display_name} est pret")
        if not config.DEBUG :
            guild = self.get_guild(int(config.CELLAR_GUILD_ID))
            if guild :
                msg = await guild.get_channel(int(config.CHANNELBOT_LOG_ID)).send("UP !")

    async def change_status(self,status):
        await self.change_presence(activity=CustomActivity(name="Custom Status",state=status))
