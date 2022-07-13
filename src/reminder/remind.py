import discord
from discord.ext import commands
from functools import lru_cache
from asyncio import sleep
import datetime

class RemindCog(commands.Cog):
    def __init__(self, bot, reminder_text, allowed_channels=None):
        self.bot = bot
        self.reminder_text = reminder_text
        self.allowed_channels = allowed_channels
        self.have_posted = []
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            print(f"{message.author}: Is a bot")
            return
        if self.allowed_channels is not None:
            if message.channel.id not in self.allowed_channels:
                print(f"{message.author}: Is not in the allowed channels")
                return
        author = await message.guild.fetch_member(message.author.id)
        if isinstance(author, discord.User):
            print(f"{message.author}: Wasn't able to retrieve member info")
            return
        if len(author.roles) > 1:
            print(f"{message.author}: Has roles")
            return
        if author.joined_at < message.created_at - datetime.timedelta(minutes=30):
            print(f"{message.author}: Joined too long ago")
            return

        has_posted = await self.has_posted(message.author.id, message.guild.id, author.joined_at)
        if has_posted:
            print(f"{message.author}: Has posted")
            return

        message = await message.channel.send(f"{message.author.mention} {self.reminder_text}")
        print(f"{message.author}: Sent reminder")
        await sleep(10)
        await message.delete()

    async def has_posted(self, author_id, guild_id, joined_at):
        if author_id in self.have_posted:
            return True
        messages = 0
        guild = await self.bot.fetch_guild(guild_id)
        channels = await guild.fetch_channels()
        for channel in channels:
            if isinstance(channel, discord.TextChannel):
                async for message_in_channel in channel.history(limit=None, after=joined_at):
                    if message_in_channel.author.id == author_id:
                        messages += 1
                        if messages > 1:
                            self.have_posted.append(author_id)
                            return True
        return False
