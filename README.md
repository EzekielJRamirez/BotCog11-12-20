# Template Cog Repository

## Welcome!!
HELLO TEAM! This repository is for anyone that wants to learn [how to make a cog](https://github.com/ACM-CBU/template_cog/blob/master/README.md#make-a-cog) for the HatBot or [learn what a cog is](https://github.com/ACM-CBU/template_cog/blob/master/README.md#what-is-a-cog).
There is a [verification process](https://github.com/ACM-CBU/template_cog/blob/master/README.md#verification-process) that __every__ cog has to go through. 


## Bot Information
There is a some pieces of information that may prove useful when messing around with HatBot. HatBot is a product of a 
python package bot called [RedBot](https://docs.discord.red/en/stable/index.html). RedBot is a really cool open-source python package that is dedicated to making bots 
extremely easy to use and give you a base foundation to launch your discord bot. With that being said we have modified the
source code of the python package to our liking and needs. The core process are the same but keep in mind we altered some 
permissions of commands.
 


## What Is A Cog?
A cog is a fancy name for a piece of functionality that discord bots have. These ___cogs___ are usually made up of python modules.
If you would like to see an example off a cog here is a link to the [guide from RedBot](https://docs.discord.red/en/stable/guide_cog_creation.html#creating-a-cog).


## Making A Cog
Making a cog can look pretty confusing and convoluted, **but this is not the case!**
At its core, a cog is just a python module where you can make any functionality as long as it is possible with python commands.
If you would like to see an example off a cog here is a link to the [guide from RedBot](https://docs.discord.red/en/stable/guide_cog_creation.html#creating-a-cog), if you would like to see a video then stay here and look bellow.
If you would like to follow written instructions explaining things as you go along in your code then go ahead and dive into the python files there will be comments there to help you through the creation process.
A few things before you take off to make your cog:
1. Remember that the bot is in python, you can use any python package as long as it is safe. Everything the bot uses is just a python package. 
2. The best way to learn what the bot can do is take a look at the [discord.py API documentation](https://discordpy.readthedocs.io/en/latest/index.html). It is really nice and easy to use.
3. We currently do not have a database setup for any of the bots, so your commands will have to do without for a while 
until we see the need for one.



## Verification Process
1. Every cog will first be tested on one of the TestBots in the CBU-ACM discord server.
    * This allows for everyone to have the ability to test their various cog mechanics before it is "released" 
    on the TheHatBot.
    * This also gives moderators and officers the ability to ensure that the cog is safe and nothings ___fishy___ is 
    happening.
2. The source code of the cog will be looked over by a moderator or officer to ensure that the cog, and the creator is honest.  
    * if you have questions about what is considered unsafe, check the discord server rules for information or contact a moderator or officer.
3. If the cog is approved, the cog will be added to the HatBot repository where you can use the cog however much you want.


## When you start implementing make sure you change this README