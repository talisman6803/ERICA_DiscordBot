import discord
import apscheduler
import time
import asyncio
import os
import datetime
import random
import re
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
    
    elif message.content.startswith('#vote'):
        await ex(message)
    
    elif message.content.startswith('#role_assign'):
        await ar(message)

    elif message.content.startswith('#echo'):
        target = message.content[6:]
        await message.channel.send(message.content)
        print(target.id)
    
async def job1(msg, message):

    await message.channel.send('@here' + msg)

    print("alarm job processing")

def sch(y, m, d, hr, mn, text, message):

    sched.add_job(job1, 'cron', year = y, month = m, day = d, hour = hr, minute = mn, args = [text, message])

    print('launch!')

async def ex(message):

    choices = {"✅": "Yes",
               "❎": "No"}

    vote = discord.Embed(title="**[찬반투표]**", description=" ", color=0xff00ff)

    value = "\n".join("- {} {}".format(*item) for item in choices.items()) 

    vote.add_field(name="메세지 하단의 이모지를 통해 찬반의사를 표시해주세요(기명)", value=value, inline=True)

    voteargs = await message.channel.send(embed=vote)

    k_lst = choices.keys()

    for key in k_lst:
        await voteargs.add_reaction(key)

    await asyncio.sleep(10)

    msg_id = voteargs.id

    voteargs = await message.channel.fetch_message(msg_id)

    await message.channel.send(str(voteargs.reactions[0].count - 1) + " votes in favor(:white_check_mark:).")
    await message.channel.send(str(voteargs.reactions[1].count - 1) + " votes in against(:negative_squared_cross_mark:).")
    
async def ar(message):

    trn = message.content[13:]
    tm = message.author

    for i in tm.guild.roles:
        if str(i) == trn:
            await tm.add_roles(i)
            await message.channel.send("Assigned the role successfully.")
            return 0
            
    await message.channel.send("There is some errors. Please check out your command.")    
    
client.run('NjQyOTI2OTA3MjA5NTQ3Nzkx.Xc51JQ.RueMNnPJXcHpiHSnxEj1o4bx9Lc')