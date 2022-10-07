import discord
from discord.ext import commands
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

  #await ctx.channel.send(a)
  #await ctx.channel.send(b)
  #await ctx.channel.send(c)

  query_txt_1 = a
  query_txt_2 = b
  query_txt_3 = c

  path = (r"C:\Users\sa485\OneDrive\Desktop\test\chromedriver.exe")
  driver = webdriver.Chrome(path)

  driver.get("https://harp.fantazm.net/dye")
  time.sleep(2)

  element_1 = driver.find_element(By.NAME, "searchDyeColor1")
  element_2 = driver.find_element(By.NAME, "searchDyeColor2")
  element_3 = driver.find_element(By.NAME, "searchDyeColor3")

  driver.find_element(By.NAME, "searchDyeColor1").click()
  element_1.send_keys(query_txt_1)
  element_1.send_keys(Keys.TAB)
  element_2.send_keys(query_txt_2)
  element_2.send_keys(Keys.TAB)
  element_3.send_keys(query_txt_3)

  driver.find_element(By.ID, "searchAmpulBtn").click()
  time.sleep(1)
  driver.find_element(By.XPATH, '//*[@id="sResult"]/div[1]/div[1]/span/i').click()
  time.sleep(1)

  color_txt = driver.find_element(By.XPATH, '//*[@id="plusResult"]/div[1]/div[1]/div/div/span')

  txt_xpath_1 = driver.find_element(By.XPATH, '//*[@id="plusResult"]/div[1]/div[2]/div/h6')
  txt_xpath_2 = driver.find_element(By.XPATH, '//*[@id="plusResult"]/div[1]/div[2]/div/div')

  temperature_xpath = driver.find_element(By.XPATH, '//*[@id="btothetop"]/div[3]/div[3]/div/h4')

  color_ = color_txt.text
  temperature = temperature_xpath.text
  txt_1 = txt_xpath_1.text
  txt_2 = txt_xpath_2.text

  embed=discord.Embed(title=color_, description="", color=temperature)
  embed.set_footer(text=txt_1 + ('\n') + txt_2)
  await ctx.send(embed=embed)

client.run(os.environ['token'])