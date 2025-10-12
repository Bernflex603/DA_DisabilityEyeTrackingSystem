# This example requires the 'message_content' intent.

import discord
from dc_pickOption import *
from tkinter import *
import threading

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    for channel in client.get_all_channels():
        if channel.name == 'bot_interact':
            await channel.send("Hello world")

@client.event
async def on_message(message):
    if message.author == client.user:
       return
    else:
        response = pickOption(message.content)
        await message.channel.send(response)


client.run('MTMwMjk5OTg1MDA0ODAzMjc5OA.GanYkH.i9Q8gN0WyZ6eibNpg5hCndKvLTmPzEoB7GT1zI')

 
def onClick1():
    print("clicked Option1")
   
def onClick2():
    print("clicked Option2") 
 
master = Tk()
Button(master, text='Option1',width=33, height=20, bg="azure", command=onClick1).grid(row=0, column=0)
Label(master, text='Neutral',width=33, height=20).grid(row=0, column=1)
Button(master, text='Option2',width=33, height=20, bg="beige", command=onClick2).grid(row=0, column=2)
mainloop()
            