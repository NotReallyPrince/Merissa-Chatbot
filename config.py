import os

class Config(object):
      BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
      OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "") 
      BOT_USERNAME = os.environ.get("BOT_USERNAME", "")     
