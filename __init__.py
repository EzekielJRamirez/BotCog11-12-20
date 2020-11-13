"""This file is dedicated to adding the cog to the bot.
This file should generally maintain this general structure.
The only thing that will change from cog to cog is what you import, which will be explained further down.
"""


from .my_cog import MyCog
"""This is a relative import, this allows you to reference files 
in a relative manor to the file that you importing in. The cog 
that you reference will be different for every cog as every 
cog needs to have a different name."""


def setup(bot):
    bot.add_cog(MyCog())
