import os
import csv
import random

import discord
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()
TOKEN = os.getenv("BOT_KEY_SBOT")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

with open('skyrim_dialogue.csv') as csvfile:
    data = list(csv.reader(csvfile))

sentiment_pipeline = pipeline("sentiment-analysis")


@client.event
async def on_ready():
    print(f'{client.user} has connected to discord')


@client.event
async def on_message(message):
    if str(client.user.id) in message.content:
        rsp = data[random.randint(0, len(data))]
        print(rsp[0])
        msg = [message.content]
        print(sentiment_pipeline(msg))
        await message.channel.send(rsp[0])
    else:
        return


client.run(TOKEN)



