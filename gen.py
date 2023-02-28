#leaking code bcuz i didnt got payout from ethan of this
import requests
from telethon import TelegramClient, events
from discord.ext import commands
import discord
import random
import datetime
import aiohttp
import os
import json
import asyncio
#put ur api id and hash
api_id = ""

api_hash = ""

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='+', intents=intents)

with open('settings.json', 'r') as f:
    settings = json.load(f)
# i will not leak extrap and bin checker code as i have not planned yet if want that code come to discord.gg/adultstars
bot.remove_command("help")
@bot.command()
async def help(ctx):
       
          embed = discord.Embed(color=0x2f3136)
          embed.set_author(name="Zero V1 MENU")
          embed.set_footer(text="Zero Checker V1 || Made by Infinity??..#2784")
          embed.set_thumbnail(url='https://media.discordapp.net/attachments/879250270176018482/885439670765387776/qxNZR3p3_400x400.jpg?width=300&height=300')
          embed.add_field(name="help", value="```Shows this menu```", inline=False)

          embed.add_field(name="extrap", value="```Extrap Your B!n```", inline=False)

          embed.add_field(name="bin", value="```Shows The B!n Info```", inline=False)
          embed.add_field(name="botinfo", value="```Shows Information about the bot```", inline=False)
          embed.add_field(name="receive", value="```Scrap Cc And Send Where receive cmd is used```", inline=False)
          embed.add_field(name="Important Links", value="[Support Server](https://discord.gg/scrapper)", inline=False)
          await ctx.send(embed=embed)



@bot.command()
async def receive(ctx, channel_id:str):
   session_name = f"session_{ctx.guild.id}_{channel_id}"
   if os.path.isfile(f"{session_name}.session"):
    client = TelegramClient(session_name, api_id, api_hash)
   else:
    client = TelegramClient(session_name, api_id, api_hash, )

   await client.start()

   @client.on(events.NewMessage(chats=(channel_id)))
   async def my_event_handler(event):
    message = event.message.message
    embed = discord.Embed(title="Scrapped CC",description=message,color=0x0000FF)
    embed.set_author(name="Made By Infinity??..")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/857714045251878972/1075655465058443274/69f482612753e4c139c5fb96ddce5680.gif")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1078917686475640852/1079699572697337856/SPOILER_IMG_20230227_151030_946.jpg")
    await ctx.send(embed=embed)

   await client.run_until_disconnected()


bot.run('')
