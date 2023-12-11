# AUTHOR: A2rae #7889 
# This code is not to be distributed and used anywhere but for this bot.

# Discord.py module
import discord
import os 
from discord.utils import get
from time import sleep
from discord import Member
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
# dotenv module
from dotenv import load_dotenv

from discord.ext import commands

# Loads the .env file on the same folder level
# Note that this doesn't really work on my end but you might be able to make it work
load_dotenv("rizken.env")
DISCORD_TOKEN = os.getenv("rizken")

# Bot's prefix, switch it if you'd like
intents = "discord.Intents.all()"
bot = commands.Bot(command_prefix='!', intents = discord.Intents().all())
client = discord.Client(intents=discord.Intents.default() , activity = discord.Game(name="!help for cmds"))

# Message that appears in the command window when run on the console
@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(f" - {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1
    print("Rizzing " + str(guild_count) + " servers.")

# Welcome message for new members
# behind ctx.guild.get_channel, put your welcome message channel id in the brackets
@bot.event
async def on_member_join(ctx):
    channel = ctx.guild.get_channel()
    embed = discord.Embed(title="Welcome to hell :)" ,description=f"{ctx.mention} just joined the destruction.")
    await channel.send(embed=embed)

# the help cmd
# just typing !help displays all the commands without any info, so this is just a display to a txt manual I made
@bot.command()
async def helpr(ctx):
    await ctx.send("I'm much too lazy to figure out how to make an embed...")
    sleep (2)
    await ctx.send("Here's a .txt instead.")
    sleep (1)
    await ctx.send("https://rentry.co/rizza")

@bot.command()
async def credits(ctx):
    await ctx.send("Rizza by A2rae #7889")
    sleep(1)
    await ctx.send("Socials: https://a2rae2.carrd.co/#socials")

# Utilities and funky

@bot.command()
async def verify(ctx):
    user = ctx.message.author
    entryrole = ctx.guild.get_role(1119287152736473198)
    await user.add_roles(entryrole)
    await ctx.send(f"{user} is verified.") 

# Color roles
# Remember to edit the role IDs
# If someone is ever able to make it so that it identifies roles by the name instead, feel free to branch off the code here :)
@bot.command()
async def addrole_yellow(ctx):
    user = ctx.message.author 
    role = ctx.guild.get_role(1091749835155185674)
    if role in user.roles:
      await user.remove_roles(role) #removes the role if user already has
      await ctx.send(f"Removed {role} from {user.mention}")
    else:
      await user.add_roles(role) #adds role if not already has it
      await ctx.send(f"Added {role} to {user.mention}") 


@bot.command()
async def addrole_blue(ctx):
    user = ctx.message.author 
    role2 = ctx.guild.get_role(1091750069188960296)
    if role2 in user.roles:
      await user.remove_roles(role2) #removes the role if user already has
      await ctx.send(f"Removed {role2} from {user.mention}")
    else:
      await user.add_roles(role2) #adds role if not already has it
      await ctx.send(f"Added {role2} to {user.mention}") 

@bot.command()
async def addrole_green(ctx):
    user = ctx.message.author 
    role3 = ctx.guild.get_role(1092007342142390395)
    if role3 in user.roles:
      await user.remove_roles(role3) #removes the role if user already has
      await ctx.send(f"Removed {role3} from {user.mention}")
    else:
      await user.add_roles(role3) #adds role if not already has it
      await ctx.send(f"Added {role3} to {user.mention}") 

@bot.command()
async def addrole_purple(ctx):
    user = ctx.message.author 
    role4 = ctx.guild.get_role(1092007415538532454)
    if role4 in user.roles:
      await user.remove_roles(role4) #removes the role if user already has
      await ctx.send(f"Removed {role4} from {user.mention}")
    else:
      await user.add_roles(role4) #adds role if not already has it
      await ctx.send(f"Added {role4} to {user.mention}") 

@bot.command()
async def addrole_red(ctx):
    user = ctx.message.author 
    role5 = ctx.guild.get_role(1092007488825589820)
    if role5 in user.roles:
      await user.remove_roles(role5) #removes the role if user already has
      await ctx.send(f"Removed {role5} from {user.mention}")
    else:
      await user.add_roles(role5) #adds role if not already has it
      await ctx.send(f"Added {role5} to {user.mention}") 

@bot.command()
# Detects when a new message is sent to a channel
async def speak(ctx,*,message):
    await ctx.send(f"{message}")
    await ctx.message.delete()

# Checks if msg has hello

@bot.command()
async def hi(ctx, name: str = None):
    name = ctx.author.name
    await ctx.send(f"sup {name}")

@bot.command()
async def bzz(ctx):
    await ctx.send("Really, the bee movie?")
    sleep(2)
    await ctx.send("Humans really like old and overused things.")
    sleep(2)
    await ctx.send("Whatever. You asked for this.")
    sleep(1)
    await ctx.send("https://www.youtube.com/watch?v=QsGYNfagHlU")
    sleep(2)
    await ctx.send("What do you mean that's cheating? Ain't no way I'm reading all that out, I'm just Python code!")

    # More moderator-ish cmds
    # This one deletes your message with the cmd too, works like any other modbot.
@bot.command()
@has_permissions(manage_messages=True)
async def clr(ctx, num):
    msg = []
    async for x in ctx.channel.history(limit=int(num)):
        msg.append(x)
    await ctx.channel.delete_messages(msg)
    print(num + ' messages rizzed.')
    warning = await ctx.send(num + ' messages rizzed.')

    # Wait to remove the warning message
    sleep(3)
    await warning.delete()

    # Error message for the command, this is copied over to any other cmd needing admin permissions.
@clr.error
async def clr_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorz mate, access denied."
        await ctx.send(text)
                       
@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member):
    await user.ban()
    await ctx.send('A user just got rizzed permenantly.')
    print('A user has been banned')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text2 = "Sorz mate, access denied. What? Raging over how you can't ban someone? L."
        await ctx.send(text2)

@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
    await user.kick()
    await ctx.send('The user has been kicked out the server')
    print('A user has been kicked')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text3 = "Sorz mate, access denied. No kicking today."
        await ctx.send(text3)

@bot.command()
@has_permissions(kick_members=True)
async def mute(ctx, user: discord.Member, time):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await user.add_roles(role)
    await ctx.send(str(user) + ' has been muted, L.')
    print('A user has been muted')
    
    # Wait a certain time before unmuting
    sleep(int(time))
    await user.remove_roles(role)
    await ctx.send(str(user) + ' is unmuted, finally.')
    print('A user has been unmuted')

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text4 = "Sorz mate, access denied. You know you can block users, right?"
        await ctx.send(text4)

        # Spam command. Remove this if you don't want to blow up your server, or just give perms to it, like I did.
        # Preferably, set this to adminstrator perms, but imo its better to just delete this.
        # Be reminded due to discord api's message limit, there is going to be a few second interruption inbetween 5 messages
@bot.command()
@has_permissions(manage_messages=True)
async def spam(ctx, amount:int, *, message):
    for i in range(amount):
        await ctx.send(message)


# Executes prgm with a bot token
bot.run("Your token here")
