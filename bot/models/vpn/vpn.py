import config
import os

VPN_FILE_PATH = "vpn.ovpn"

class Vpn():

    def __init__(self,bot):
        self.bot = bot
        self.running = False
        self.ovpn_set = False

    async def start(self,interaction):
        if self.running:
            await interaction.followup.send(f"vpn already started")
        else :
            if self.ovpn_set :
                self.running = True
                code = os.system(f"openvpn {VPN_FILE_PATH} &")
                if code == 0 :
                    await self.update_vpn_status(interaction)
                else :
                    self.running = False
                    await interaction.followup.send(f"error in vpn start")

            else :
                await interaction.followup.send(f"no open vpn file setup (/set_vpn)")

    async def stop(self,interaction = None):
        if not self.running:
            await interaction.followup.send("No vpn running")
        else :
            self.running = False
            os.system(f"killall openvpn")
            await self.update_vpn_status(interaction)
    
    async def setup(self,interaction,vpn_file):
        try :
            with open(VPN_FILE_PATH,'w') as f:
                data = await vpn_file.read()
                f.write(data.decode())
            self.ovpn_set = True
            await interaction.followup.send(f"vpn file setup succes")
        except : 
            await interaction.followup.send(f"vpn file setup failed")

    async def update_vpn_status(self,interaction = None):
        if interaction :
            await interaction.followup.send(f"VPN has {'START' if self.running else 'STOP'}")
        await self.bot.change_status(f"VPN : {'ON' if self.running else 'OFF'}")