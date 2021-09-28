import discord
import os
import itertools
import time
import keep_alive
from discord.ext.commands import Bot
from discord.ext import commands
import random
import secrets

bot = commands.Bot(command_prefix='!')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
intents.members = True


@client.event
async def on_ready():
    activity = discord.Game(name="With my dick", type=3)
    await client.change_presence(activity=discord.Game(name=activity))



@client.event
async def on_member_join(member):
  while True:
    foo = ["do you like beans? \n", "I need to know if you like beans \n", "please \n", "you have to tell me if you like beans \n", "I am asking very kindly, do you like beans?", "beans?", "look, you have to tell me if you like dem beans"]
    await member.send(secrets.choice(foo))
    time.sleep(5)


@client.event
async def on_message(message):
  if message.author == client.user:
   return
   
  if "no" in message.content:
    with open('wrong.png', 'rb') as f:
      picture = discord.File(f)
      await message.channel.send(file=picture)

  if "yes" in message.content:
    with open('thumbsup.png', 'rb') as f:
      picture = discord.File(f)
      await message.channel.send(file=picture)

  if message.content.startswith("beans"):
    message = await message.channel.send("do you like beans?", tts=True)
    with open('beans.jpeg', 'rb') as f:
      picture = discord.File(f)
      await message.channel.send(file=picture)

    


#@client.event
#async def on_message(message):
 # if message.author == client.user:
  # return
   #
  #if "no" in message.content:
  #  while True:
    #  msg = "do you like beans? \n" 
     # await message.channel.send(msg)
     # time.sleep(5)

    
keep_alive.keep_alive()
client.run(os.getenv("token"))