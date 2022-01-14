import discord
import os
import re
import time
import datetime
from pytz import timezone
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz


client = discord.Client()
#regex for the !DnD command
dnDCommandregex = '^![Dd]\s{0,}?[Nn&]\s{0,}?[Dd]$'

#a map that defines the days & time for games
dnDschedule = {
  "Tuesday": "20:30", 
  "Saturday": "21:00"
}

def getNextGameDateTime():
  onDay = lambda dt, day: dt + datetime.timedelta(days=(day-dt.weekday())%7)
  date = datetime.datetime.now().astimezone(timezone('US/Pacific'))
  todaysWeekday = date.weekday()
  for day in dnDschedule:
    scheduledWeekday = time.strptime(day, "%A").tm_wday
    if scheduledWeekday >= todaysWeekday:
      timeSplit = dnDschedule[day].split(":")
      return onDay(date, scheduledWeekday).replace(hour=int(timeSplit[0]), minute=int(timeSplit[1]), second = 0)

def getUnixTime(dateTime):
  return int(dateTime.timestamp())

#async def roleCall():
  #await message.channel.send("Please emote if you are in for D&D tonight.")

@client.event
async def on_ready():
    print('Logged in and ready to go')

#@client.event
#async def Rolecall():
  #scheduler = AsyncIOScheduler()
  #if today in dndDays:
    #if today ==5:
          #scheduler.add_job(roleCall, CronTrigger(second="0, 10, 20, 30, 40, 50")) 


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if re.match(dnDCommandregex, message.content):
      if str(message.author) == "Corey#5281":
        await message.channel.send('Master why have you called on me again')
      if str(message.author) == "Glacies#1660":
        await message.channel.send("Why have you summoned me today Owlek?")
      #if str(message.author) == "piece#3523": 
        #await message.channel.send("Good to see you again")
      nextGameDateTime = getNextGameDateTime()
      await message.channel.send("The next game will be at <t:{0}>".format(getUnixTime(nextGameDateTime)))
      
# Programmers: Corey
# Contributor  Alex
# Contributor  Alec

client.run(os.getenv('TOKEN'))
