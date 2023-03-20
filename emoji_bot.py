import nextcord
import bot_secrets
import re
import emoji
from nextcord.ext import commands

SERVER_ID = 639700575339937792

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@bot.event
async def on_message(message):
    msg = message.content
    print(f'Initial Message:\n {msg}')
    
    # BOT BEHAVIOR QUESTIONS
    #   Remove photos?
    #   Remove gifs?
    #   Remove stickers?
    #   Remove mentions?
    
    # Custom Emoji Handler
    custom_emojis = re.findall(r'<:\w*:\d*>', message.content)
    print(f'Custom Discord Emojis:\n {custom_emojis}')
    for emote in custom_emojis:
        msg = msg.replace(emote,'')
    print(f'Custom Emojis Removed:\n {msg}')
    
    # Unicode Emoji Handler
    text = emoji.demojize(msg)
    text = re.findall(r'(:[^:]*:)', text)
    unicode_emojis = [emoji.emojize(x) for x in text]
    print(f'Unicode Emojis:\n {unicode_emojis}')
    for emote in unicode_emojis:
        msg = msg.replace(emote,'')
    print(f'All Emojis Removed:\n {msg}')
    
    # Check if message still there
    msg = msg.strip()
    print("Final Message Verdict:")
    if msg == "":
        print("Keep")
    else:
        print("Delete")
    

bot.run(bot_secrets.TOKEN)