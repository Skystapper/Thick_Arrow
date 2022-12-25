import logging
import logging.config

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

import os
import pyrogram
from config import Config
from pyrogram import Client
from plugins.database import db 


# changing to urlup

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# main content

class Bot(Client):
   
   def __init__(self):
       super().__init__(
            name="md-rename-bot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins={"root": "plugins"},
        )
      
   async def start(self):
      await super().start()
      self.log = logging
      if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
      banned_users = await db.get_banned_users()
      Config.BANNED_USERS = banned_users
      logging.info(f"{self.me.first_name} is Successfully started")
   
   async def stop(self):
      await super().stop()
      logging.info(f"{self.me.first_name} is stopped...")

# bot = Bot()
# bot.run()

# change to urlup

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from config import Config
else:
    from config import Config


logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "X-URL-Uploader",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    Config.AUTH_USERS.add(958850850)
    app.run()


# change to rename
bot = Bot()
bot.run()

