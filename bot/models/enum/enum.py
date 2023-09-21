from bot.models.enum.sanitize import Sanitize

class Enum():

    def __init__(self,ip):

        self.ip = Sanitize.ip(ip)