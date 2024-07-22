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
# dotenv module, OS is very important here to take token from .env file
import os
from dotenv import load_dotenv

from discord.ext import commands
# remember to download discord.py's extensions, time py module and dotenv before running

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

# Welcome message for new members, remember to set 'channel' to the channel id you want the message to be broadcast in.
@bot.event
async def on_member_join(ctx):
    channel = ctx.guild.get_channel(channel)
    embed = discord.Embed(title="Welcome to hell :)" ,description=f"{ctx.mention} just joined the destruction.")
    await channel.send(embed=embed)

# the help cmd
# just typing !help displays all the commands without any info, so this is just a display to a txt manual I made, feel free to replace and modify this one.
@bot.command()
async def helpr(ctx):
    await ctx.send("I'm much too lazy to figure out how to make an embed...")
    sleep (2)
    await ctx.send("Here's a .txt instead.")
    sleep (1)
    await ctx.send("https://rentry.co/rizza")

# Credits command, please do not remove!
# You may add yourself in if you have any added modifications but do not remove the original credit, thanks!
@bot.command()
async def credits(ctx):
    await ctx.send("Rizza by A2rae #7889")
    sleep(1)
    await ctx.send("Socials: https://a2rae2.carrd.co/#socials")


# Rolegiving command
# Change the guild id to whichever server you are going to use this bot in
# if someone manages to be able to fetch guild id automatically, please branch to my git, thanks
# feel free to also change role message!!

# This one is an example of a static role giving cmd, delete this one if you want.
# But if you want to keep it, remember to change role id
# Remember to also remove the @has_permissions line if you want the perm requirement to be gone-- or modify it if you want higher permission level
@has_permissions(manage_roles=True)
async def anarchy(ctx):
    user = ctx.message.author 
    role = ctx.guild.get_role(roleid)
    if role in user.roles:
      await user.remove_roles(role) #removes the role if user already has
      await ctx.send(f"Removed {role} from {user.mention}, demodded L.")
    else:
      await user.add_roles(role) #adds role if not already has it
      await ctx.send(f"Added {role} to {user.mention}. Welcome!") 
# Error message for insufficient permissions, I used this one for all the other perm-required cmds too.
@anarchy.error
async def anarchy_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text6 = "Sorz mate, access denied."
        await ctx.send(text6)
# Here's an example of a rolegiving cmd that gives roles based on server and on rolename
# There are two levels of responses to this command: role verify and applying the role
# Role verify is basically making sure the role exists in the server you're using it in, and if not it'll notify you
# Role giving is basically what it is, unless if you had a role and you reran the cmd for that role again it'll remove it instead.
@bot.command()
@has_permissions(manage_roles=True)
async def role(ctx,message, member: discord.Member):

    user = ctx.message.author
    role2 = f"{message}"
    idr = ctx.message.guild.id
    guild = bot.get_guild(idr)
    role3 = discord.utils.get(guild.roles, name=role2)
    if role3 is not None:
        await ctx.send(f"Confirmed existence of {role2}")
    else:
        await ctx.send(f"Role {role2} does not exist yet, sorry dude.")
    if role3 in member.roles:
        await member.remove_roles(role3)
        await ctx.send(f"Removed {role2} from {member.mention}")
    else:
        await member.remove_roles(role3)
        await ctx.send(f"Added {role2} to {member.mention}")
@role.error
async def role_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text5 = "Sorz mate, access denied."
        await ctx.send(text5)

# fun cmds
# remove and modify as you like!

# Tupperbox-esque echo command.
# can use without any brackets securing the message, and deletes your command message right after
@bot.command()
async def speak(ctx,*,message):
    await ctx.send(f"{message}")
    await ctx.message.delete()

# hello echo message

@bot.command()
async def hi(ctx, name: str = None):
    name = ctx.author.name
    await ctx.send(f"sup {name}")

@bot.command()
async def tower(ctx):
    await ctx.send("TOWER OF BABEL!!")

# bee movie at your disposal, the time module is really here just for this

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
# this line fetches an .env file by the name of "token"
# so if you want to input another .env file, switch out "token" with your filename
# or if you want to run a token directly, take out everything within the first bracket and leave in bot.run() and input your token right into the bracket
bot.run(os.getenv("token"))
