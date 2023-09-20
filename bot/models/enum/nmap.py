import os
import config
from nextcord import File
import uuid
from bot.models.enum.sanitize import Sanitize

class Nmap():
    
    def __init__(self,ip):
        self.ip = Sanitize.ip(ip)

    async def scan(self,interaction):
        scan_name = uuid.uuid1()
        path = f"{config.TMP_PATH}/{scan_name}.txt"
        exit_code = os.system(f"nmap -A -v {self.ip} -oN {path} >/dev/null")
        if exit_code == 0:
            res = File(path,filename=f"nmap_{self.ip}.txt")
            await interaction.followup.send(file=res)
        else :
            await interaction.followup.send(content=f"Error -> code error {exit_code}")
