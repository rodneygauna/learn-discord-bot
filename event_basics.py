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


# Run the bot
bot.run(DISCORD_BOT_TOKEN)

