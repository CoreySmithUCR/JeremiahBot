import discord
import os
import re
from datetime import datetime
from pytz import timezone
import pytz



client = discord.Client()
doodie = '^![Dd]\s{0,}?[Nn&]\s{0,}?[Dd]$'
dndDays = [int(1), int(5)]


def get_pst_time():
  print("starting get_pst_time")
  date_format='%m_%d_%Y_%H_%M_%S_%Z'
  date = datetime.now(tz=pytz.utc)
  date = date.astimezone(timezone('US/Pacific'))
  pstDateTime=date.strftime(date_format)
  print(pstDateTime)
  print(date.weekday())
  return date;



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
        await message.channel.send("Why have you summoned me today Owlek?")
      today = get_pst_time().weekday()
      if today in dndDays:
        await message.channel.send('Get Hype, There is DND today')
      if today == 1:
        await message.channel.send("We are starting at 8:30 today")
      if today == 5:
        await message.channel.send("We are starting at 9:30 today")
        
      else:
        await message.channel.send("There is no DND today, now I must get back to my business in Saltmarsh.")
      

# Programmers: Corey
# Contributor  Alex
# Contributor  Alec

client.run('DISCORD_JERETOKEN')
