import discord
import os
from discord import *
from discord.ext import commands
from discord import Embed

client = commands.Bot(command_prefix='t*')

@client.remove_command("help")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
    

client.run('ODI2NTcwNTQ4NzgzMDg3NjI3.YGOZzw.XG5iPIoyR37CK438TR5tjND9smw')   