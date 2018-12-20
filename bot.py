import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from itertools import cycle
import json
#import config

TOKEN = 'NTI1MDM5NzUyOTcwMzcxMTA1.DvxjoA.Sx3ZslCRcPn9rPm2ccnkMYd74Uw'

bot = commands.Bot(command_prefix = '$')
#client = commands.Bot(command_prefix = '.')

status = ['Developed By ayo', 'Your Personal Fitness Tracker', 'Use $help for help' ]

async def change_status():
        await bot.wait_until_ready()
        msgs = cycle(status)

        while not bot.is_closed:
            current_status = next(msgs)
            await bot.change_presence(game=discord.Game(name=current_status))
            await asyncio.sleep(3)

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command(pass_context=True)
async def create(ctx):
    fileopen = ctx.message.author.id + ".json"
    file = open(fileopen, "w", encoding="utf-8")
    data = {}
    data["name"] = None
    data["age"] = None
    data["location"] = None
    data["gender"] = None
    data["weight"] =  None
    data["height"] = None
    json.dump(data, file, ensure_ascii=False)
    file.close()
    await bot.say('Profile created!')

@bot.command(pass_context=True)
async def profile(ctx, user: discord.Member):
    fileopen = user.id + ".json"
    file = open(fileopen, "r", encoding="utf-8")
    data = json.load(file)
    name = data["name"]
    age = data["age"]
    location = data["location"]
    gender = data["gender"]
    weight = data["weight"]
    height = data["height"]
    embed = discord.Embed(title="{}#{}'s Profile".format(user.name, user.discriminator), color=0xffffff)
    embed.set_author(name="{}".format(user.name), icon_url=user.avatar_url)
    embed.add_field(name="Name", value=name)
    embed.add_field(name="Age", value=age)
    embed.add_field(name="Location", value=location)
    embed.add_field(name="Gender", value=gender)
    embed.add_field(name="Weight", value=weight)
    embed.add_field(name="Height", value=height)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def name(ctx, *args):
    fileopen = ctx.message.author.id + ".json"
    file = open(fileopen, "r", encoding="utf-8")
    predata = json.load(file)
    prename = predata["name"]
    preage = predata["age"]
    prelocation = predata["location"]
    pregender = predata["gender"]
    preweight = predata["weight"]
    preheight = predata["height"]
    file = open(fileopen, "w", encoding="utf-8")
    data = {}
    data["name"] = " ".join(args).replace("/{}/g", " ")
    data["age"] = preage
    data["location"] = prelocation
    data["gender"] = pregender
    data["weight"] = preweight
    data["height"] = preheight
    json.dump(data, file, ensure_ascii=False)
    file.close()
    await bot.say('Name changed!')

@bot.command(pass_context=True)
async def age(ctx, *args):
    fileopen = ctx.message.author.id + ".json"
    file = open(fileopen, "r", encoding="utf-8")
    predata = json.load(file)
    prename = predata["name"]
    preage = predata["age"]
    prelocation = predata["location"]
    pregender = predata["gender"]
    preweight = predata["weight"]
    preheight = predata["height"]
    file = open(fileopen, "w", encoding="utf-8")
    data = {}
    data["name"] = prename
    data["age"] = " ".join(args).replace("/{}/g", " ")
    data["location"] = prelocation
    data["gender"] = pregender
    data["weight"] = preweight
    data["height"] = preheight
    json.dump(data, file, ensure_ascii=False)
    file.close()
    await bot.say('Age changed!')

@bot.command(pass_context=True)
async def location(ctx, *args):
    fileopen = ctx.message.author.id + ".json"
    file = open(fileopen, "r", encoding="utf-8")
    predata = json.load(file)
    prename = predata["name"]
    preage = predata["age"]
    prelocation = predata["location"]
    pregender = predata["gender"]
    preweight = predata["weight"]
    preheight = predata["height"]
    file = open(fileopen, "w", encoding="utf-8")
    data = {}
    data["name"] = prename
    data["age"] = preage
    data["location"] = " ".join(args).replace("/{}/g", " ")
    data["gender"] = pregender
    data["weight"] = preweight
    data["height"] = preheight
    json.dump(data, file, ensure_ascii=False)
    file.close()
    await bot.say('Location changed!')

@bot.command(pass_context=True)
async def gender(ctx, *args):
    fileopen = ctx.message.author.id + ".json"
    file = open(fileopen, "r", encoding="utf-8")
    predata = json.load(file)
    prename = predata["name"]
    preage = predata["age"]
    prelocation = predata["location"]
    pregender = predata["gender"]
    preweight = predata["weight"]
    preheight = predata["height"]
    file = open(fileopen, "w", encoding="utf-8")
    data = {}
    data["name"] = prename
    data["age"] = preage
    data["location"] = prelocation
    data["gender"] = " ".join(args).replace("/{}/g", " ")
    data["weight"] = preweight
    data["height"] = preheight
    json.dump(data, file, ensure_ascii=False)
    file.close()
    await bot.say('Gender changed!')



@bot.command(pass_context=True)
async def weight(ctx, *args):
    fileopen = ctx.message.author.id + ".json"
    file = open(fileopen, "r", encoding="utf-8")
    predata = json.load(file)
    prename = predata["name"]
    preage = predata["age"]
    prelocation = predata["location"]
    pregender = predata["gender"]
    preweight = predata["weight"]
    preheight = predata["height"]
    file = open(fileopen, "w", encoding="utf-8")
    data = {}
    data["name"] = prename
    data["age"] = preage
    data["location"] = prelocation
    data["gender"] = pregender
    data["weight"] = " ".join(args).replace("/{}/g", " ")
    data["height"] = preheight
    json.dump(data, file, ensure_ascii=False)
    file.close()
    await bot.say('Location changed!')

@bot.command(pass_context=True)
async def height(ctx, *args):
    fileopen = ctx.message.author.id + ".json"
    file = open(fileopen, "r", encoding="utf-8")
    predata = json.load(file)
    prename = predata["name"]
    preage = predata["age"]
    prelocation = predata["location"]
    pregender = predata["gender"]
    preweight = predata["weight"]
    preheight = predata["height"]
    file = open(fileopen, "w", encoding="utf-8")
    data = {}
    data["name"] = prename
    data["age"] = preage
    data["location"] = prelocation
    data["gender"] = pregender
    data["weight"] = preweight
    data["height"] = " ".join(args).replace("/{}/g", " ")
    json.dump(data, file, ensure_ascii=False)
    file.close()
    await bot.say('Height changed!')

#bot.run(config.token)
@bot.command()
async def logout():
    await bot.logout()

bot.loop.create_task(change_status())
bot.run(TOKEN)



"""
@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author,content))

@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '{}: {}'.format(author, content))
"""
"""
@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('.ping'):
        await client.send_message(channel, "pong")

    if message.content.startswith('.echo'):
        msg = message.content.split()
        output = ''
        for word in  msg[1:]:
            output += word
            output += ' '
        await client.send_message(channel, output)


        Varible for user profile
        getuser
        weight = 95

        print = enter your your current weight

        @client.command()
        async def ping():
            await client.say("Pong!")

        @client.command()
        async def echo(*args):
            output = ''
            for word in args:
                output += word
                output += ' '
            await client.say(output)
"""
