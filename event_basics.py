'''
Learning the basics of building a Discord bot.
'''


# Imports
import os
import discord
from dotenv import load_dotenv


# Load discord bot's token
load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_TOKEN')


# Discord "Message Content Intent"
intents = discord.Intents.default()
intents.message_content = True
intents.members = True


# Global Variables
bot = discord.Client(intents=intents)


# Let the server know the bot is online
@bot.event
async def on_ready():
    print('Bot is online')


# Respond with "Hello" when a user sends "Hello"
@bot.event
async def on_message(msg):
    username = msg.author.display_name
    if msg.author == bot.user:
        return
    else:
        if msg.content == "Hello":
            await msg.channel.send(f"Howdy there, {username}!")


# DM member that joined the server
@bot.event
async def on_member_join(member):
    guild = member.guild
    guildname = guild.name
    dmchannel = await member.create_dm()

    await dmchannel.send(f"Welcome to {guildname}!")


# Add role based on reaction
@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    member = payload.member
    message_id = payload.message_id
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)

    if message_id == 1088201588448968846:
        if emoji == '🥷':
            role = discord.utils.get(guild.roles, name='Ninja')
            await member.add_roles(role)
            print('Ninja role added')
        elif emoji == '🏴‍☠️':
            role = discord.utils.get(guild.roles, name='Pirate')
            await member.add_roles(role)
            print('Pirate role added')


# Remove role based on reaction
@bot.event
async def on_raw_reaction_remove(payload):
    emoji = payload.emoji.name
    message_id = payload.message_id
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)
    member = guild.get_member(payload.user_id)

    if message_id == 1088201588448968846:
        if emoji == '🥷':
            role = discord.utils.get(guild.roles, name='Ninja')
            await member.remove_roles(role)
            print('Ninja role removed')
        elif emoji == '🏴‍☠️':
            role = discord.utils.get(guild.roles, name='Pirate')
            await member.remove_roles(role)
            print('Pirate role removed')


# Run the bot
bot.run(DISCORD_BOT_TOKEN)
