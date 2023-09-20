import os
import config
from bot import bot

debug = config.DEBUG

if debug:
    command_prefix="§"
else :
    command_prefix = "s!"

sbr = bot.SbrBot(command_prefix=command_prefix)

os.system(f"mkdir {config.TMP_PATH}")

for file in os.listdir("./bot/cogs"):
    if(file.endswith(".py")):
        sbr.load_extension(f"bot.cogs.{file[:-3]}")


sbr.run(config.SBR_TOKEN)