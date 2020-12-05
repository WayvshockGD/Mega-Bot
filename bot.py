import discord
from discord.ext import commands
import os

from config import token, prefix

client = commands.Bot(command_prefix= prefix)
client.remove_command("help")

@client.event
async def on_ready():

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'the prefix {prefix}'))

    print("Logged in :D")

for filename in os.listdir('./cogs'):
       if filename.endswith('.py'):
          client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)