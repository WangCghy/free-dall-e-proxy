from dotenv import load_dotenv
import os
from loguru import logger

class Config:
    # Load .env file
    if not load_dotenv(dotenv_path = os.path.join('data','.env')):
        logger.error("No data/.env file found. Please make sure you are in the root directory of the project.")

    if os.getenv('FASTAPI_SERVER_URL') is not None:
        logger.warning(f"the env 'FASTAPI_SERVER_URL' is deprecated, please remove it and set 'PORT' in your data/.env instead.(Default: PORT=8000)")
    PORT = int(os.getenv('PORT') or 8000)
    Timeout = float((os.getenv('TIMEOUT')) or 60)
    # telegram
    TELEGRAM = os.getenv('TELEGRAM')
    API_ID = int(os.getenv('API_ID') or -1)
    API_HASH = os.getenv('API_HASH')
    BOT_USERNAME = os.getenv('BOT_USERNAME')
    BOT_USERNAME = BOT_USERNAME if BOT_USERNAME.startswith('@') else '@'+BOT_USERNAME
    SESSION_NAME = os.getenv('SESSION_NAME')+'.session'
    # read session file if exists
    if os.path.exists(os.path.join('data',SESSION_NAME)):
        with open(os.path.join('data',SESSION_NAME),'r') as f:
            SESSION_STRING = f.read().strip()
    else:
        SESSION_STRING = ""

    # discord
    Discord = os.getenv('DISCORD')
    DiscordClientBotToken = os.getenv('DISCORD_ClIENT_BOT_TOKEN')
    DiscordChannelID = int(os.getenv('DISCORD_CHANNEL_ID') or -1)
    DiscordDalleBotID = int(os.getenv('DISCORD_DALLE_BOT_ID') or -1)

config = Config()