import discord
import os
import re
import time
import datetime
from pytz import timezone
from collections import OrderedDict

client = discord.Client()
#regex for the !DnD command
dnDCommandregex = '^![Dd]\s{0,}?[Nn&]\s{0,}?[Dd]$'

#an ordered dict that defines the days & time for games
#for ease, we assume these are defined here in order (Monday is first day of week)
dnDSchedule = OrderedDict([
  ("Tuesday", "20:30"), 
  ("Saturday", "21:00")
])

def getNextGameDateTime():
  onDay = lambda dt, day: dt + datetime.timedelta(days=(day-dt.weekday())%7)
  date = datetime.datetime.now().astimezone(timezone('US/Pacific'))
  todaysWeekday = date.weekday()
  for day, timeOfDay in dnDSchedule.items():
    scheduledWeekday = time.strptime(day, "%A").tm_wday
    if scheduledWeekday >= todaysWeekday:
      timeSplit = timeOfDay.split(":")
      return onDay(date, scheduledWeekday).replace(hour=int(timeSplit[0]), minute=int(timeSplit[1]), second = 0)
  
  #if we hit this line, then there are no upcoming games for this week
  #the next game will be the first game of next week
  firstGameOfWeek = next(iter(dnDSchedule.items())) #get the first game out of the OrderedDict
  timeSplit = firstGameOfWeek[1].split(":")
  return onDay(date, time.strptime(firstGameOfWeek[0], "%A").tm_wday).replace(hour=int(timeSplit[0]), minute=int(timeSplit[1]), second = 0)

def getUnixTime(toUnixTime):
  return int(toUnixTime.timestamp())

@client.event
async def on_ready():
    print('Logged in and ready to go')


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  elif re.match(dnDCommandregex, message.content):
    if str(message.author) == "Corey#5281":
      await message.channel.send('Good to see you again.')
    if str(message.author) == "Glacies#1660":
      await message.channel.send("Why have you summoned me today Owlek?")
    if str(message.author) == "piece#3523": 
      await message.channel.send("Good to see you again, campaign manager")
    nextGameDateTime = getNextGameDateTime()
    await message.channel.send("The next game will be at <t:{0}>".format(getUnixTime(nextGameDateTime)))
      
# Programmers: Corey
# Contributor  Alex
# Contributor  Alec

client.run(os.getenv('TOKEN'))
