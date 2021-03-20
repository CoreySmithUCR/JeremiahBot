import discord
import os
import datetime
import re

client = discord.Client()
doodie = '^![Dd]\s{0,}?[Nn&]\s{0,}?[Dd]$'
dndDays = [int(1), int(5)]


@client.event
async def on_ready():
    print('Logged in and ready to go')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if re.match(doodie, message.content):
      if str(message.author) == "Corey#5281":
        await message.channel.send('Master why have you called on me again')
      if str(message.author) == "Glacies#1660":
        await message.channel.send("Thank you Owlek, you always brighten my day with your questions, and for that I am forever in your debt, also")
      today = datetime.datetime.today().weekday()
      if today in dndDays:
        await message.channel.send('Hold onto your butts, There is DND today')
      else:
        await message.channel.send("There is no DND today, I'm also slightly disappointed you asked.")
  
        


client.run(os.getenv('DISCORD_JERETOKEN'))
