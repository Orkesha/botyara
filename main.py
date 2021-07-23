import os
import asyncio
import random
import discord
from discord.ext import commands
import keep_alive

client = commands.Bot(command_prefix="")

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

@client.command()
async def harakiri(ctx):
  await ctx.reply('Чё надо лох')
  await asyncio.sleep(2)
  await ctx.send('Ааа, ты же гей')
  await asyncio.sleep(2)
  await ctx.send('Добро пожаловать в гей клуб ебат')
  await ctx.send(file=discord.File('gayclyb.jpg'))

@client.command()
async def overlord(ctx):
    await ctx.reply('Поздравляю, теперь ты гей ебат!')
    role = discord.utils.get(ctx.guild.roles, id=867366733051330581)
    while True:
        await role.edit(colour=RandomColor())
        await asyncio.sleep(10)


@client.command()
async def sosatt(ctx):
    await ctx.reply('Поздравляю, теперь ты гей ебат!')
    role = discord.utils.get(ctx.guild.roles, id=855112661824962581)
    while True:
        await role.edit(colour=RandomColor())
        await asyncio.sleep(10)

@client.command()
async def aboba(ctx):
    await ctx.reply('Далбаёб detected!!!')
    role = discord.utils.get(ctx.guild.roles, id=849630503803551754)
    while True:
        await role.edit(colour=RandomColor())
        await asyncio.sleep(10)

@client.event
async def on_ready():
  print(f"Бот запущен")
  while True:
     await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name="♂Gomo♂ SLAYER"))
     await asyncio.sleep(3)
     await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name="♂Gay club♂ 3"))
     await asyncio.sleep(3)
     await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name="♂Gay♂ Songs"))
     await asyncio.sleep(3)

keep_alive.keep_alive()
client.run('ODU3NTYxODk4MTgxNzIyMTIy.YNRYwQ.Odc54SADOSA4zPn9ecXa8B3PT1w')