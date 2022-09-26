import os,discord
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#processes
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected!')

@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return 

    clean_content = message.content.split(' ')

    if clean_content[0] == "!ping": #respond command to test bot
        await message.reply("PONG")

    if clean_content[0] == "!help":
        f = open('./help.txt','r')
        help_text = f.read()
        client.loop.create_task(message.reply(help_text)) 
        f.close()
    
    if clean_content[0] == "!start":
        p = requests.post("http://localhost:3000/api/start?wait=true")
        client.loop.create_task(message.reply("Server started successfully!"))

    if clean_content[0] == "!stop":
        p = requests.post("http:localhost:3000/api/stop")
        client.loop.create_task(message.reply("Server stopped successfully!"))

    if clean_content[0] == "!quit":
        await client.close()

client.run(TOKEN)