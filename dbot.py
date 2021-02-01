# Import Discord Package
import discord
import os
import requests
import json
import random
import replit from db

# Client (our bot)
client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "sorrow", "saaad", "dead", "death", "mourning", "miserable", "depressing", "suffer"]

starter_encouragements = [
    "Cheer Up, I'm here for!",
    "Hang in there!",
    "Don't give up!",
    "We're all here for you!",
    "Wipe those tears away!",
    "Go eat some icecream!",
    ":kissing_heart:",
    ":sob:",
    ":cry:",
    ":cry: Don't say that!",
    ":sob: I'm here!"
]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():

# Bot
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content
    
    # Hello 
    if message.content.startswith('$hello'):
        await message.channel.send('Hello !')
      
    # Random insiparation  
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
        
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice
                                   (starter_encouragements))

# Run the client on the server
client.run('ODA1MTkxMDY3ODk2Nzc0NjU3.YBXSng.snoOjClxQcQz32FJQ5xnK5WEc20')