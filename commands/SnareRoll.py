import discord 
from discord.ext import commands 
import os
from discord.ext.commands.cooldowns import BucketType

class SnareRoll(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def SnareRoll(self, ctx): 
        with open(r'D:\AndrewBot\AndrewBot\snare-role_G_minor.wav', 'rb') as fp:
            await channel.send(file=discord.File(fp, 'snare-role_G_minor.wav'))
    
    
def setup(client):
    client.add_cog(SnareRoll(client))