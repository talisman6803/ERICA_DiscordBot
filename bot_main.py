import discord
import apscheduler
import time
import asyncio
import os
import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

client = discord.Client()
sched = AsyncIOScheduler()
sched.start()
msg_ch = None

@client.event
async def on_ready():
    print('You \'ve logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("ERICA Discord Bot"))
    print('Operation is started.')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('#operation test'):
        await message.channel.send('정상')
    elif message.content.startswith('#help'):
        await message.channel.send('사용법\nhttps://github.com/talisman6803/ERICA_DiscordBot/wiki')

    elif message.content.startswith('#alarm'): #alarm YYYY-MM-DD HR:MN for
        y = str(message.content[7:11])
        m = str(message.content[12:14])
        d = str(message.content[15:17])
        hr = str(message.content[18:20])
        mn = str(message.content[21:23])
        text = str(message.content[27:])
        sch(y, m, d, hr, mn, text, message)
        print("alarm job reserved, " + y + m + d + hr + mn + " for " + text)

async def job1(msg, message):
    await message.channel.send('@here' + msg)
    print("alarm job processing")

def sch(y, m, d, hr, mn, text, message):
    sched.add_job(job1, 'cron', year = y, month = m, day = d, hour = hr, minute = mn, args = [text, message])
    print('launch!')

client.run('NjQyOTI2OTA3MjA5NTQ3Nzkx.Xc1XYA.JSF6rC9gEKgcI5afy1rdjMNNNww')