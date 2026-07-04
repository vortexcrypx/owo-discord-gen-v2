import discord
from discord.ext import commands
import asyncio
import json
import colorama
from colorama import Fore, Style
import sys
import discordrpc
import time

if sys.version_info >= (3, 14):
    try:
        asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

with open('config.json', 'r') as file:
    data = json.load(file)

token = data['token']
prefix = data['prefix']

intents = discord.Intents.all()

vortex = commands.Bot(command_prefix=prefix, intents=intents, self_bot=True)
@vortex.event
async def on_ready():
    print(Fore.GREEN +"""
██╗░░░██╗░█████╗░██████╗░████████╗███████╗██╗░░██╗░░░███████╗██╗░░██╗███████╗
██║░░░██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝░░░██╔════╝╚██╗██╔╝██╔════╝
╚██╗░██╔╝██║░░██║██████╔╝░░░██║░░░█████╗░░░╚███╔╝░░░░█████╗░░░╚███╔╝░█████╗░░
░╚████╔╝░██║░░██║██╔══██╗░░░██║░░░██╔══╝░░░██╔██╗░░░░██╔══╝░░░██╔██╗░██╔══╝░░
░░╚██╔╝░░╚█████╔╝██║░░██║░░░██║░░░███████╗██╔╝╚██╗██╗███████╗██╔╝╚██╗███████╗
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝╚══════╝╚═╝░░╚═╝╚══════╝""")
    print(Fore.GREEN + f'+ | Logged in as {vortex.user} (ID: {vortex.user.id})')
    print(Fore.GREEN + '+ | Join our Discord: https://discord.gg/G7SXNJB6Qq')
    print('----------------------------------------------------------------')


rpc = discordrpc.RPC(app_id=1522928580492005406)

rpc.set_activity(
      state="CrypZUwU.exe",
      details="Grinding!",
      large_image="crypzuwu",
      large_text="CrypZUwU",
      small_image="crypzpy",
      small_text="CrypZPY",
      buttons=[{"label": "Join our Discord!", "url": "https://discord.gg/G7SXNJB6Qq"}]
        
    )


@vortex.command()
async def ping(ctx):
    latency = vortex.latency
    await ctx.send(f'Pong! {latency*1000:.2f}ms') 


vortex_looping = False

@vortex.command()
async def start(ctx):
    global vortex_looping
    if vortex_looping:
        await ctx.send('Autostart is already running.')
        return
    vortex_looping = True
    while True:
        await ctx.send('**Vortex Farm enabled!** ~ powered by Vortex')
        await asyncio.sleep(1)
        await ctx.send('owo h')
        print("owo h sent")
        await asyncio.sleep(18)
        await ctx.send('owo h')
        print("owo h sent")
        await asyncio.sleep(3)
        await ctx.send('owo b')
        print("owo b sent")
        await asyncio.sleep(2)
        await ctx.send('owo inv')
        print("owo inv sent")
        await asyncio.sleep(3)
        await ctx.send('owo pray')
        print("owo pray sent")
        await asyncio.sleep(10)
        await ctx.send('owo h')
        print("owo h sent")
        await asyncio.sleep(3)
        await ctx.send('owo sell all')
        print("owo sell all sent")
        await asyncio.sleep(16)
        await ctx.send('owo h')
        await asyncio.sleep(19)
        await ctx.send('owo h')
        print("owo h sent")
        await asyncio.sleep(18)
        await ctx.send('owo h')
        print("owo h sent")
        await asyncio.sleep(3)
        await ctx.send('owo b')
        print("owo b sent")
        await asyncio.sleep(2)
        await ctx.send('owo inv')
        print("owo inv sent")
        await asyncio.sleep(5)
        await asyncio.sleep(10)
        await ctx.send('owo h')
        print("owo h sent")
        await asyncio.sleep(3)
        await ctx.send('owo sell all')
        print("owo sell all sent")
        await asyncio.sleep(16)
        await ctx.send('owo h')
        print("owo h sent, looping!")
        await ctx.send('**Vortex Farm cycle complete!** ~ powered by Vortex')
        await asyncio.sleep(240) # 233 seconds 4min
        # first cycle complete, repeat
        await ctx.send('owo h')
        await asyncio.sleep(19)
        await ctx.send('owo h')
        await asyncio.sleep(5)
        await ctx.send('owo b')
        await asyncio.sleep(3)
        await ctx.send('owo inv')
        await asyncio.sleep(13)
        await ctx.send('owo h')
        await asyncio.sleep(3)
        await ctx.send('owo sell all')
        await asyncio.sleep(16)
        await ctx.send('owo h')
        await asyncio.sleep(19)
        await ctx.send('owo h')
        await asyncio.sleep(19)
        await ctx.send('owo h')
        await asyncio.sleep(5)
        await ctx.send('owo b')
        await asyncio.sleep(3)
        await ctx.send('owo inv')
        await asyncio.sleep(13)
        await ctx.send('owo h')
        await asyncio.sleep(3)
        await ctx.send('owo sell all')
        await ctx.send('**Vortex Farm cycle complete!** ~ powered by Vortex')
        await asyncio.sleep(303) # 300 seconds 5min
        # second cycle complete, repeat
        await ctx.send('owo h')
        await asyncio.sleep(16)
        await ctx.send('owo h')
        await asyncio.sleep(2)
        await ctx.send('owo b')
        await asyncio.sleep(5)
        await ctx.send('owo inv')
        await asyncio.sleep(16)
        await ctx.send('owo h')
        await asyncio.sleep(3)
        await ctx.send('owo sell all')
        await asyncio.sleep(19)
        await ctx.send('owo h')
        await asyncio.sleep(19)
        await ctx.send('owo h')
        await asyncio.sleep(16)
        await ctx.send('owo h')
        await asyncio.sleep(2)
        await ctx.send('owo b')
        await asyncio.sleep(5)
        await ctx.send('owo inv')
        await asyncio.sleep(16)
        await ctx.send('owo h')
        await asyncio.sleep(3)
        await ctx.send('owo sell all')
        await asyncio.sleep(19)
        await ctx.send('owo h')
        await ctx.send('**Vortex Farm cycle complete!** ~ powered by Vortex')
        await asyncio.sleep(403) # 400 seconds 6min 40sec
        # third cycle complete, repeat
        await ctx.send('owo h')
        await asyncio.sleep(20)
        await ctx.send('owo h')
        await asyncio.sleep(2)
        await ctx.send('owo b')
        await asyncio.sleep(5)
        await ctx.send('owo inv')
        await asyncio.sleep(2)
        await asyncio.sleep(18)
        await ctx.send('owo h')
        await asyncio.sleep(3)
        await ctx.send('owo sell all')
        await asyncio.sleep(19)
        await ctx.send('owo h')
        await asyncio.sleep(19)
        await ctx.send('owo h')
        await asyncio.sleep(20)
        await ctx.send('owo h')
        await asyncio.sleep(2)
        await ctx.send('owo b')
        await asyncio.sleep(5)
        await ctx.send('owo inv')
        await asyncio.sleep(2)
        await asyncio.sleep(18)
        await ctx.send('owo h')
        await asyncio.sleep(3)
        await ctx.send('owo sell all')
        await asyncio.sleep(19)
        await ctx.send('owo h')
        await ctx.send('**Vortex Farm cycle complete!** ~ powered by Vortex')
        await asyncio.sleep(353) # 350 seconds 5min 50sec
        # fourth cycle complete, repeat
        await ctx.send('owo h')
        await asyncio.sleep(20)
        await ctx.send('owo h')
        await asyncio.sleep(2)
        await ctx.send('owo b')
        await asyncio.sleep(5)
        await ctx.send('owo inv')
        await asyncio.sleep(2)
        await asyncio.sleep(18)
        await ctx.send('owo h')
        await asyncio.sleep(3)
        await ctx.send('owo sell all')
        await asyncio.sleep(19)
        await ctx.send('owo h')
        await asyncio.sleep(19)
        await ctx.send('owo h')
        await asyncio.sleep(20)
        await ctx.send('owo h')
        await asyncio.sleep(2)
        await ctx.send('owo b')
        await asyncio.sleep(5)
        await ctx.send('owo inv')
        await asyncio.sleep(2)
        await asyncio.sleep(18)
        await ctx.send('owo h')
        await asyncio.sleep(3)
        await ctx.send('owo sell all')
        await asyncio.sleep(19)
        await ctx.send('owo h')
        await ctx.send('**Vortex Last cycle complete!**, _**16m 40s break**_ ~ powered by Vortex')
        await asyncio.sleep(1000) # 1000 seconds ~16min 40sec
        # last cycle complete, loop


@vortex.command()
async def stop(ctx):
    global vortex_looping
    if not vortex_looping:
        await ctx.send('**Vortex Farm** is not running.')
        return
    vortex_looping = False
    await ctx.send('**Vortex Farm** has been stopped.')



vortex.run(token, bot=False)
rpc.run()
