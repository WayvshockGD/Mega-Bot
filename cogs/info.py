import discord
from discord.ext import commands
from config import prefix

class info(commands.Cog): 
    def __init__(self, client):
        self.client = client
        
    @commands.command(aliases=["commands"])
    async def help(self, ctx):

        helpEmbed = discord.Embed(title = "Commands", description="Categorys:")

        helpEmbed.add_field(name="Core", value=f'`{prefix}help`', inline=True)

        await ctx.send(embed=helpEmbed)


def setup(client):
    client.add_cog(info(client))