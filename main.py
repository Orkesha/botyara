import os
import re
import asyncio
import random
import discord
from discord.ext import commands
from discord.utils import get
import ffmpeg
from googleapiclient.discovery import build
import urllib.parse, urllib.request
import googletrans 
from googletrans import Translator

client = commands.Bot(command_prefix="")
api_key = "AIzaSyBL2ZBVoHzU43wgmF36PTdcFie25Cg140g"

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandomColor2(): 
    randcolor2 = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor2

@client.command()
async def Нагадить(ctx, member : discord.Member):
  userid = ctx.author.id
  if userid == 485489979796226089:
    try:
        channel = member.voice.channel
        if channel: # If user is in a channel
            vc = await channel.connect() # Connect
            await ctx.send("Ща братан...")
        else:
            await ctx.send("Уже там...") # If the bot is already connected
        vc.play(discord.FFmpegPCMAudio("yamete.mp3"), after=lambda e: print('done', e))
        await asyncio.sleep(15)
        await vc.disconnect()
    except AttributeError:
        return await ctx.send("Его нету...") # Error message
  else:
    await ctx.send('Е не знаю такого..')

@client.command(brief='Переводит текст. Использование транслит [язык] [текст]')
async def транслит(ctx, lang, *, args):
  t = Translator()
  a = t.translate(args, dest=lang)
  await ctx.send('На ебат, перевод на `' + lang + '` язык: `' + a.text + '`')

@client.command(aliases=["show"], brief='Ищет в гугле картинку по тексту')
async def гуглпик(ctx, *, search):
  userid = ctx.author.id
  if userid == 485489979796226089 or userid == 852609539497000960 or userid == 479953230554726420 or userid == 672658552409686037:
    ran = random.randint(0, 9)
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    result = resource.list(
        q=f"{search}", cx="4af447e250bf2abd0", searchType="image"
    ).execute()
    url = result["items"][ran]["link"]
    embed1 = discord.Embed(title=f"Дэржи босс: {search.title()}")
    embed1.set_image(url=url)
    await ctx.reply(embed=embed1)
  else:
    await ctx.reply('Е кетш сасымай, стемим на')

@client.command(brief='Ищет видос на ютубе по тексту')
async def чекютуб(ctx, *, search):
    query_string = urllib.parse.urlencode({
      'search_query': search
    })
    html_content = urllib.request.urlopen(
      'http://www.youtube.com/results?' + query_string
    )
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    await ctx.reply('Дэржи ебат:')
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])

@client.command(brief='Позвать бота')
async def харакири(ctx):
  userid = ctx.author.id
  if userid == 485489979796226089:
    await ctx.reply('Мой повелитель, что вы желаете со мной делать?')
    await asyncio.sleep(1)
    await ctx.send('Господин, нежнее!!')
    await asyncio.sleep(1)
    await ctx.send('Аааах.. Господин...')
    await ctx.send(file=discord.File('anime.jpg'))
  elif userid == 852609539497000960 or userid == 479953230554726420:
    await ctx.reply('О господин, добро пожаловать в элитный гей клуб')
    await asyncio.sleep(1)
    await ctx.send('Проходите!')
    await ctx.send(file=discord.File('gayclyb.jpg'))
  else:
    await ctx.reply('Чё надо лох?')
    await asyncio.sleep(1)
    await ctx.send('Аааа ты же гей..')
    await asyncio.sleep(1)
    await ctx.send('Добро пожаловать в гей клуб ебат')
    await ctx.send(file=discord.File('gayclyb.jpg'))

@client.command(brief='Гейская радуга для Всех!')
async def радуга(ctx, roleid, *, slp):
  userid = ctx.author.id
  if userid == 485489979796226089 or userid == 852609539497000960 or userid == 479953230554726420:
    await ctx.reply('Харашо мой повелитель!')
    await asyncio.sleep(1)
    await ctx.send('Гейская радуга включена для роли '+roleid)
    rolid = int(re.search(r'\d+', roleid).group(0))
    slpp = int(re.search(r'\d+', slp).group(0))
    member = ctx.author
    role = discord.utils.get(member.guild.roles, id=rolid)
    while True:
        await role.edit(colour=RandomColor())
        await asyncio.sleep(slpp)
  else:
    await ctx.reply('Бля чел пошёл нахуй')

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

client.run('ODU3NTYxODk4MTgxNzIyMTIy.YNRYwQ.Odc54SADOSA4zPn9ecXa8B3PT1w')
