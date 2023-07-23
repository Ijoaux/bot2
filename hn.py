import discord
import random
import asyncio

from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot !')

@bot.command()
async def advice(ctx):
    await ctx.send(f'!To_start, !To_do')

@bot.command()
async def To_start (ctx):
    await ctx.send(f'Mengurangi penggunaan plastik')

@bot.command()
async def To_do(ctx):
    await ctx.send(
        "-Memilah sampah\n"
        "-Membawa Kantong Belanja Sendiri\n"
        "-Hindari Membeli Makanan dan Minuman Kemasan Plastik\n"
    )


bot.run("MTEzMjQ4Mzc1MzMzMjE5NTM1OA.GTX4Iy.oXTNCyD-GnnkyMMOFstKNrrxBC1xwO2fGccc28")