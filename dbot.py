# Import Discord Package
import discord
import os
import requests
import json
import random
import replit 

# Client (our bot)
client = discord.Client()

hello_words = ["Hey", "Sup", "Heyy", "heyyy", "hey", ":grin:", ":wave: heya", "how are ya", "heya", "what's up", "hi"]
# Part Of hello words in response to you
converstaion_words = ["how are you", ""]

love_words = ["love you", "luv u", ">3"]

sad_words = ["sad", "depressed", "unhappy", "angry", "sorrow", "saaad", "dead", "death", "mourning", "miserable", "depressing", "suffer", "down"]

starter_greetings = [
   "Hey", 
   "Sup", 
   "Heyy", 
   "heyyy", 
   "hey", 
   ":grin:", 
   ":wave: heya",
   "how are ya", 
   "heya", 
   "what's up",
   "hi"
]

starter_love = [
    ":Kissing_heart: You're always so nice to me",
    ":smiling_face_with_3_hearts: how's your day been going",
    ":smiling_face_with_3_hearts: love you too",
    "I'm grateful for you!",
    "https://tenor.com/view/hug-virtual-hug-hug-sent-gif-5026057 lucky you",
    ":heart_eyes: we should stream a movie together!"
]

starter_converstaion = [
    "I've been doing good, busy as always!",
    "Same as always what's new with you?",
    "Really?!"
    "That's pretty cool!",
    "Watching any new shows?"
    
]

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
    ":sob: I'm here!",
    "Don't say that!",
    "You can talk to me!"
]

# Insprational Quotes
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

def get_gif():
    apikey = "0ML4KXVQP4HS"
    lmt = 8
    search_term = "love"
    response = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))
    json_data = json.loads(response.content)



# Bot
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content
    
    # Greetings
    if message.content.startswith('$hello'):
        await message.channel.send(random.choice
                                   (starter_greetings))
      
    # Random insiparation  
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    
    if any(word in msg for word in love_words):
        await message.channel.send(random.choice
                                   (starter_love))
    
    if any(word in msg for word in hello_words):
        await message.channel.send(random.choice
                                   (starter_greetings))
    
    # Encouragement
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice
                                   (starter_encouragements))

# Run the client on the server
client.run('ODA1MTkxMDY3ODk2Nzc0NjU3.YBXSng.MBQwYTUIZFeT8snholEImM6rSYo')