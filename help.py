import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command(name="help", aliases=["h"])
    async def help(self, ctx):
        helpembed = discord.Embed(title="Help Embed", color=discord.Color(0x27cc9a))
        helpembed.add_field(name='Command Info', value='To get more information on a command do t*help <command>', inline=False)
        helpembed.add_field(name='Misc', value='Ping', inline=False)
        helpembed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=helpembed)

def setup(client):
    client.add_cog(Help(client))