import discord
from discord.exe import commands
import random
import math
import qrcode
import asyncio
import requests
import io
import json
import java
import datetime
from datetime import datetime

client = discord.Client()
version = '1.0.0.0'
botid = ''
comm1 = '//1qr'
comm2 = ''
comm3 = ''
comm4 = ''
@client.event
async def on_ready():
    print('Ready to Use', client.user)
    embed = discord.Embed(
        title='{0.user} ist jetzt online!'.format(client),
        description='Bin da',
        color=0xff6000)
    channel = client.get_channel(int(830475080404303882))
    msg = await channel.send(embed=embed)

@client.event
async def on_message(message):
    if message.author == client.user:
        return




    #Create Qr code   
    if message.content.startswith(Comm1):
        arr = message.content.split(' ')
        text = ' '.join(arr[1:])
        img = qrcode.make(text)
        img.save('qr.png')
        await message.channel.send(file=discord.File('qr.png'))
