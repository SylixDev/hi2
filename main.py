import discord
import asyncio
import random
import time

client = discord.Client()

responses = [
    "Hey, what's up? How's your day going?",
    "Did you know? Elephants can't jump! 🐘",
    "Okay, your turn! Tell me a joke! 😁",
    "Why did the chicken join a band? Because it had drumsticks! 🐔🥁",
    "I'm just here, vibing... Tell me a fun fact!",
    "I think I need more coffee! ☕",
]

crash_out_messages = [
    "YOUR A FUCKING CHEZ MONSTER IMA CRASHOUT",
    "KYS U FUCKING NIGGER",
    "DIE DIE DIE DIE DIE SKIDS ARE FUCKING NIGGERS KYS KYS KYS",
    "HOLY FUCK YOU LOOK LIKE MY LEFT NUT NIGGA",
    "HEY HEY HEY NIGGA KYS KYS SLIT UR THROAT",
]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    while True:
        channel = client.get_channel(1302745300007387261)
        await channel.send(random.choice(responses))
        await asyncio.sleep(2)
        await channel.send(random.choice(crash_out_messages))
        await asyncio.sleep(15)

client.run('MTMwMjc0NTYwMTkzMDMwMTUxMQ.GcrbDO.YNUTnlRsTHveHgzb_nj0Du9y0cCRCtktBDusJI')
