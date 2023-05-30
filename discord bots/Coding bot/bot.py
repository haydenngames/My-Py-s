import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# Create an instance of the bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user.name}')

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot
bot.run('MTExMjc4NTI3Mzk0MDYxNTE4OA.GfwV6b.Kw1_POzFM7ZkizRmMc3D4QE8T3Sj50N7z7KZ_0')
