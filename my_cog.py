from redbot.core import commands
from .my_cog_helper import say_hi_helper


class MyCog(commands.Cog):
    """This file is dedicated to making a custom cog called my MyCog.
    This is where you can define the functionality of your cog."""

    """
    if you want to learn some quick little things you can do with the bot here is a nice little page 
    https://github.com/Redjumpman/Jumper-Plugins/wiki/Red-Coding-Guide-V3#vocabulary

    the official documentation for the bot package is found here:
    https://docs.discord.red/en/stable/index.html 

    here is the discord that red wraps around that will be helpful to understand how to use things:
    https://docs.discord.red/en/stable/index.html

    The bot already incorporates threading into it from the base package, if you dont know what threading is dont 
    worry too much about it. Just know that every command you make will have to have the async keyword in front of def.
    :param ctx stands for context. This param will contain all the possible information you could ever want to know 
    about any command context. 
    """

    @commands.command()  # this sets the bellow function as a bot command
    async def myCom(self, ctx: commands.Context):  # this will be the name of you command that you will use in discord
        """This does stuff!"""
        # Your code will go here

        # whenever you want to the bot to preform an action that will require its full attention, you need to use await
        # in the documentation, it will specifically specify if you need to use await.
        await ctx.send("I can do stuff!")

    """Remember this is just regular python, so you can call other packages and files that you make."""

    @commands.command()
    async def sayHi(self, ctx: commands.Context, *arg):  # '*args' allows you to take in as many params as are passed in
        # Calls helper method from another file
        await ctx.send(say_hi_helper(*arg))
