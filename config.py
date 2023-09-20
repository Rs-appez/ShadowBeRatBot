from decouple import config
from pathlib import Path
#debug
DEBUG=config('DEBUG',default=False)

#token
SBR_TOKEN=config('SBR_TOKEN')

#guild
CELLAR_GUILD_ID=config("CELLAR_GUILD_ID")

#channel
CHANNELBOT_LOG_ID=1110930833314938950

#tmp
TMP_PATH = f"{Path( __file__ ).parent.absolute()}/tmp"