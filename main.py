import discord.ext.commands.bot
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.ext.commands.bot.Bot(command_prefix='?', intents=discord.Intents.all(),
                                   owner_ids=[742976057761726514, 849939032410030080])

@bot.event
async def on_ready():
    await bot.load_extension('jishaku.cog')

bot.run(os.getenv("DISCORD_TOKEN"))
