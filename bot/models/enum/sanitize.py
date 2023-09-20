import re
class Sanitize():

    @staticmethod
    def ip(ip):
        match = re.fullmatch("([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)", ip)
        if match :
            return match.group()
        raise TypeError()
