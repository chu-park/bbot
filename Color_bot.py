import discord
from discord.ext import commands
import os

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

client = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)
  
  await client.change_presence(activity=discord.Game(name="대기"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

@client.command()
async def 염색(ctx, *, txt):
  a, b, c = txt.split(".")

  await ctx.channel.send(a)
  await ctx.channel.send(b)
  await ctx.channel.send(c)

  query_txt_1 = a
  query_txt_2 = b
  query_txt_3 = c

  driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
  
  await ctx.channel.send(a)
  await ctx.channel.send(b)
  await ctx.channel.send(c)

  driver.get("https://harp.fantazm.net/dye")
  time.sleep(2)
  await ctx.channel.send(driver.page_source)

  

client.run(os.environ['token'])