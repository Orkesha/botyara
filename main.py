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

@client.command(brief='Ищет картинку в гугле')
async def гуглпик(ctx, *, search):
   a = ["hentai", "хентай", "хентыч", "хентай хентай хентай хентай хентай хентай хентай", "hentai hentai hentai hentai hentai hentai", "хентыч хентыч хентай хентыч hentai", "hentai hentai хентыч хентай hentai хентыч хентыч"]
   b = ["порно", "прон", "порнуха","porn","pron", "pornhub", "порнхаб", "pornuha","nudes","adult","anal","нюдс","анал", "sex", "секс", "porns","порнухи", "порно порно порно порно порно порно прон прон порнуха porn порнхаб порнхаб анал анал анал anal anal анал секс секс секс нюдс порнхаб порнхаб порно прон порнуха порно pron хентай порно"]
   c = ["члены", "писька", "писюны", "письки", "члены члены писька писька писюны писюны письки письки pisun pisyn"]
   z = search
   x = z.casefold()
   if any(x in s for s in a):
      await ctx.reply("Не гугли такое, бьяка!((")
   elif any(x in s for s in b):
      await ctx.reply("Не гугли такое, бьяка!((")
   elif any(x in s for s in c):
      await ctx.reply("Ясен хуй, ты гей)))0)")
   else:
      await ctx.reply("Поздравляю ебат, твой запрос прошёл мощный фильтр.")
      ran = random.randint(0, 9)
      resource = build("customsearch", "v1", developerKey=api_key).cse()
      result = resource.list(
        q=f"{search}", cx="4af447e250bf2abd0", searchType="image"
      ).execute()
      url = result["items"][ran]["link"]
      embed1 = discord.Embed(title=f"Дэржи ебат: {search.title()}")
      embed1.set_image(url=url)
      await ctx.send(embed=embed1)

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

@client.command()
async def addid(ctx, *, a: str):
  userid = ctx.author.id
  if userid == 485489979796226089:
    a = a.replace("<","")
    a = a.replace(">","")
    a = a.replace("@","")
    a = a.replace("&","")
    a = a.replace("!","")
    my_file = open("allowedid.txt", "a+")
    my_file.write(a+"   ")
    my_file.close()
    await ctx.send("Ок, записал в бд")
  else:
    await ctx.send("Ты гей))0)")

@client.command()
async def checkid(ctx):
  userid = ctx.author.id
  if userid == 485489979796226089:
    my_file = open("allowedid.txt", "r")
    await ctx.send("Айди счастливчиков: "+my_file.read())
    my_file.close()
  else:
    await ctx.send("Даунов не обслуживаю")
    
@client.command(brief='Гейская радуга для Всех!')
async def радуга(ctx, roleid, *, slp):
 gid = ctx.message.guild.id
 open(str(gid)+'time.txt', 'a')
 open(str(gid)+'.txt', 'a')
 sfile = open(str(gid)+'.txt', 'r')
 if "" == str(sfile.read()):
    sfile = open(str(gid)+'.txt', 'w')
    sfile.write("1")
    sfile.close()
 stfile = open(str(gid)+'time.txt', 'r')
 if "" == str(stfile.read()):
    sfile = open(str(gid)+'time.txt', 'w')
    sfile.write("0")
    sfile.close()
 sfile = open(str(gid)+'.txt', 'r')
 if 1000 < int(sfile.read()):
   dbztime = open(str(gid)+'time.txt', 'r')
   dbtime = 86400 - int(dbztime.read())
   await ctx.send("К сожалению кулдаун настиг этот сервер. Ждите, "+str(datetime.timedelta(seconds=dbtime)))
   dbztime.close()
 else:
   my_file = open("allowedid.txt", "r")
   if str(ctx.author.id) in str(my_file.read()):
    sfile = open(str(gid)+'.txt', 'r')
    my_file.close()
    await ctx.reply('Харашо мой повелитель!')
    await asyncio.sleep(1)
    mess = await ctx.send('Гейская радуга включена для роли '+roleid+', Кулдаун: '+sfile.read()+'/1000')
    rolid = int(re.search(r'\d+', roleid).group(0))
    slpp = int(re.search(r'\d+', slp).group(0))
    sfile = open(str(gid)+'.txt', 'r')
    counta = int(sfile.read())
    member = ctx.author
    role = discord.utils.get(member.guild.roles, id=rolid)
    while True:
        await role.edit(colour=RandomColor())
        sfile = open(str(gid)+'.txt', 'r')
        counta = int(sfile.read()) + int(1)
        sfile.close()
        sfile = open(str(gid)+'.txt', 'w')
        sfile.write(str(counta))
        sfile.close()
        sfile = open(str(gid)+'.txt', 'r')
        await mess.edit(content='Гейская радуга включена для роли '+roleid+', Кулдаун: '+sfile.read()+'/1000')
        sfile.close()
        if counta > 1000:
          break
        await asyncio.sleep(slpp)
    await ctx.send('Действие радуги закончилась у роли '+roleid+'!')
    await asyncio.sleep(2)
    stfile = open(str(gid)+'time.txt', 'r')
    a = 0
    if int(stfile.read()) > 0:
      print(f's')
      stfile.close()
    else:
      stfile.close()
      while True:
       a = a + 1
       stfile = open(str(gid)+'time.txt', 'w+')
       stfile.write(str(a))
       stfile.close()
       await asyncio.sleep(1)
       if a == 86400:
        break
      zer = 0
      one = 1
      sfile = open(str(gid)+'.txt', 'w+')
      sfile.write(str(one))
      sfile.close()
      strfile = open(str(gid)+'time.txt', 'w+')
      strfile.wtite(str(zer))
      strfile.close()
      await ctx.reply("Радуга вновь доступна!")
   else:
    await ctx.reply("Далбаебам куни не делаю")
    my_file.close()

@client.event
async def on_ready():
  print(f"Бот запущен")
  while True:
     await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name="♂Gomo♂ SLAYER"))
     await asyncio.sleep(3)
     await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name="♂Gay club♂"))
     await asyncio.sleep(3)
     await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name="♂Gachi♂ remix"))
     await asyncio.sleep(3)

client.run('ODU3NTYxODk4MTgxNzIyMTIy.YNRYwQ.Odc54SADOSA4zPn9ecXa8B3PT1w')
