import discord
import apscheduler
import time
import asyncio
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler

client = discord.Client()
sched = AsyncIOScheduler()

client.run('token')
