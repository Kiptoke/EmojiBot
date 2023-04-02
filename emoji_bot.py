import nextcord
import bot_secrets
import re
import emoji
from nextcord.ext import commands

SERVER_ID = 639700575339937792

# WolverineSoft Specific Variables
CHANNEL_ID = 590591000708251648
BOT_TESTING = False  

WHITELIST = [
    1085740714853404723,    # EmojiSoft
]

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@bot.event
async def on_message(message):
    msg = message.content
    author = message.author

    # Bot Testing
    if BOT_TESTING and message.channel.id != CHANNEL_ID:
        return
    
    # Whitelist
    if BOT_TESTING == False and (author.id in WHITELIST):
        return
    
    print(f'------ Initial Message by {author}: ------\n {msg}')
    
    # Custom Emoji Handler
    custom_emojis = re.findall(r'<a?:\w*:\d*>', message.content)
    print(f'Custom Discord Emojis: {custom_emojis}')
    for emote in custom_emojis:
        msg = msg.replace(emote,'')
    
    # Unicode Emoji Handler
    text = emoji.demojize(msg)
    text = re.findall(r'(:[^:]*:)', text)
    unicode_emojis = [emoji.emojize(x) for x in text]
    print(f'Unicode Emojis: {unicode_emojis}')
    for emote in unicode_emojis:
        msg = msg.replace(emote,'')
    
    # Message Verdict
    print("Final Message Verdict:")
    keep_msg = True
    
    if msg.strip() != "":   # No Text
        print("Removed for text or GIF")
        keep_msg = False
        
    if len(message.attachments) != 0:   #  No images
        print("Removed for images")
        keep_msg = False
        
    if len(message.stickers) != 0:  # No stickers
        print("Removed for stickers")
        keep_msg = False
        
    if keep_msg:
        print("Message kept!")
    else:
        await delete_message(message)
    
@bot.event
async def on_message_edit(before, after):
    msg = after.content
    author = after.author

    # Bot Testing
    if BOT_TESTING and after.channel.id != CHANNEL_ID:
        return
    
    # Whitelist
    if BOT_TESTING == False and (author.id in WHITELIST):
        return
    
    print(f'------ Initial Message by {author}: ------\n {msg}')
    
    # Custom Emoji Handler
    custom_emojis = re.findall(r'<a?:\w*:\d*>', after.content)
    print(f'Custom Discord Emojis: {custom_emojis}')
    for emote in custom_emojis:
        msg = msg.replace(emote,'')
    
    # Unicode Emoji Handler
    text = emoji.demojize(msg)
    text = re.findall(r'(:[^:]*:)', text)
    unicode_emojis = [emoji.emojize(x) for x in text]
    print(f'Unicode Emojis: {unicode_emojis}')
    for emote in unicode_emojis:
        msg = msg.replace(emote,'')
    
    # Message Verdict
    print("Final Message Verdict:")
    keep_msg = True
    
    if msg.strip() != "":   # No Text
        print("Removed for text or GIF")
        keep_msg = False
        
    if len(after.attachments) != 0:   #  No images
        print("Removed for images")
        keep_msg = False
        
    if len(after.stickers) != 0:  # No stickers
        print("Removed for stickers")
        keep_msg = False
        
    if keep_msg:
        print("Message kept!")
    else:
        await delete_message(after)
    
async def delete_message(message):
    DELETION_DELAY = 0.0
    try:
        await message.delete(delay = DELETION_DELAY) 
        await message.author.send("You can only send emoji!")
    except nextcord.Forbidden as error:
        print("You don't have permissions to delete messages!")
        print(error)
    except nextcord.NotFound as error:
        print("Message already deleted!")
        print(error)
    except nextcord.HTTPException as error:
        print("OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working VEWY HAWD to fix this!")
        print(error)
    except:
        print("wait what the fuck did you do") 
    
bot.run(bot_secrets.TOKEN)