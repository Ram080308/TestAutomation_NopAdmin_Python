
import configparser

config = configparser.RawConfigParser()
config.read("E:\pythonProject\Framefork1\Configurations\config.ini")

class ReagConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get("common info" , "baseurl")
        return url

    @staticmethod
    def getUserName():
        username = config.get("common info" , "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info" , "password")
        return password

    @staticmethod
    def getfrontend_url():
        frontURL = config.get("frontend details" , "front_baseurl")
        return frontURL

