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



# Run the bot
bot.run(DISCORD_BOT_TOKEN)

