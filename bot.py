import discord
from discord.ext import commands, tasks
import motion_detection
from datetime import datetime

TOKEN = "ODU2MDEyMzY4MDMzODczOTQx.YM61pA.xildexP8zYlnU3xcGlXr3k5yTRI"

help_message = """```
arm - Turn on security notifications
disarm - Turn off security notifications
info - shows this command
status - show bot status
update - send photo of what the camera sees
```"""

armed = "disarmed"

client = commands.Bot(command_prefix="$")


@client.event
async def on_ready():
    detect_motion.start()
    print("Bot logged in")


@client.command()
async def info(ctx):
    await ctx.send(help_message)


@client.command()
async def update(ctx):
    motion_detection.update()
    await ctx.send("Current view outside the house (Looks great huh)", file=discord.File("current_image.jpg"))


@client.command()
async def arm(ctx):
    global armed
    armed = "armed"
    await ctx.send("ARMED")


@client.command()
async def disarm(ctx):
    global armed
    armed = "disarmed"
    await ctx.send("DISARMED")

@client.command()
async def status(ctx):
    await ctx.send("Security system is currently {}\nTime: {}".format(armed, datetime.now()))


@tasks.loop(seconds=3)
async def detect_motion():
    channel = client.get_channel(856220951472635964)
    if motion_detection.Main() and armed == "armed":
        await channel.send("POSSIBLE INTRUDER ALERT")


client.run(TOKEN)
