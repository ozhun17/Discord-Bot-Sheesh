import discord
import os
import time
from discord.ext import commands
from discord import FFmpegPCMAudio

client = commands.Bot(command_prefix='')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.command()
async def sheesh(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await ctx.send("Sheesh")
        voice = await channel.connect()
        source = FFmpegPCMAudio('Sheesh.wav')
        player = voice.play(source) 
        time.sleep(9)
        await ctx.send("join")
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("Can't connect to server")


@client.command(pass_context = True)
async def lesgo(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await ctx.send("Lesgo")
        voice = await channel.connect()
        source = FFmpegPCMAudio('lezgo.wav')
        player = voice.play(source) 
        time.sleep(4)
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("Can't connect to server")


@client.command(pass_context = True)
async def leave(ctx):
    #if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("left voice chat")
    #else:
    #   await ctx.send("not in a voice chat")

f = open("token", "r")
token = f.readline()
f.close()
client.run('token')

