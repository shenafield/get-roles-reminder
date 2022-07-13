import json
import os

import discord
from discord.ext import commands
from dotenv import find_dotenv
from dotenv import load_dotenv

from .remind import RemindCog


def main():
    load_dotenv(find_dotenv(usecwd=True))

    TOKEN = os.getenv('DISCORD_TOKEN')
    REMINDER_MESSAGE = os.getenv('REMINDER_MESSAGE')
    ALLOWED_CHANNELS = json.loads(os.getenv('ALLOWED_CHANNELS', "null"))

    bot = commands.Bot(command_prefix='!')

    bot.add_cog(RemindCog(bot, REMINDER_MESSAGE, ALLOWED_CHANNELS))
    bot.run(TOKEN)


if __name__ == '__main__':
    main()

