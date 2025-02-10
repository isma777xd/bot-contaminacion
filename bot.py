mport discord
from discord.ext import commands
import os,random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command()
async def on_ready():
    await ctx.send(f"Hola,soy un bot {bot.user}!")

@bot.command()
async def paw(ctx):
    await ctx.send(gen_pass(10))

bot.run("Token")
