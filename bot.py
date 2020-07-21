
import discord 
from discord.ext import commands 
import os

client = commands.Bot(command_prefix = '.')

@client.event 
async def on_ready():
    print('Bot is ready')
    await client.change_presence(activity=discord.Activity(name="Breaking Bad", type=discord.ActivityType.watching))

@client.command()
@commands.is_owner()
async def load(ctx, extenstion):
    client.load_extension(f'commands.{extenstion}')

@client.command()
@commands.is_owner()
async def unload(ctx, extenstion):
    client.unload_extension(f'commands.{extenstion}')

@client.command()
@commands.is_owner()
async def reload(ctx, extenstion):
    client.unload_extension(f'commands.{extenstion}')
    client.load_extension(f'commands.{extenstion}')

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')

client.run('')
