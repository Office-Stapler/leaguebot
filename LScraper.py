import discord
import discord.permissions
from discord.ext import commands
import random
import subprocess
import requests, bs4
import youtube_dl
import os
import json

import League_Constants as LConsts
import Face_Recognition_Test
from Commands import moduleRandom

token = 'NTcwNTQ3MDA1NDA4MTQ5NTA0.XXzrFA.Ms5h9tU_ZgqDvkkxNaO2WCMUF80'
client = commands.Bot(command_prefix = '+')

@client.event
async def on_ready():
    print('Logged in as ')
    print(client.user.name)
    print(client.user.id)
    print('-------------')
    await client.change_presence(activity = discord.Game(name = 'Trying to live'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.lower()
    if msg.startswith("im"):
        await message.channel.send(f'Hi {message.content[3:]}, I\'m Stapler-San')
        return
    elif msg.startswith('i\'m'):
        await message.channel.send(f'Hi {message.content[4:]}, I\'m Stapler-san!')
        return
    print(f'{message.author} just said {message.content}')
    await client.process_commands(message)

@client.command()
async def coinflip(ctx):
    await ctx.send(moduleRandom.coinflip())

@client.command(aliases=['8ball'])
async def mball(ctx, *, question = None):
    if question is None:
        await ctx.send('Please enter a question for the magic 8ball to answer!')
        return
    if '?' not in question:
        question += '?'
    e = discord.Embed(title = question,
                      description = f'{moduleRandom.mball()}',
                      colour = discord.Colour.blue())
    await ctx.send(embed = e)
    print(f'{ctx.message.author} asked the magic 8ball {question.title()}')

@client.command()
async def purge(ctx, amount = 10):
    # if ctx.message.author
    max = int(amount)
    print(f'{ctx.message.author} purged {max} number of messages')
    await ctx.channel.purge(limit = max + 1)

@client.command()
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    await ctx.send(f'{member.avatar_url}')
    print(f'{ctx.message.author} wanted the avatar of {member}')

@client.command()
async def ranint(ctx, first, last):
    try:
        num1 = int(first)
        num2 = int(last)
    except ValueError:
        await ctx.send('Please enter valid INTEGERS')
    await ctx.send(random.randint(num1,num2))

@client.command()
async def ran(ctx, * , to_rand = None):
    if to_rand is None:
        await ctx.send('ERROR, PLEASE ENTER ARGUMENTS TO RANDOM!')
    else:
        List = to_rand.split(' ')
        rand = List[random.randint(0, len(List) - 1)]
        await ctx.send(rand.title())

@client.command()
async def aboutSummoner(ctx, summonerName):
    URL = f'{LConsts.summoner_url}{summonerName}?api_key={LConsts.APIKey}'
    response = requests.get(URL)
    dictionary = json.loads(response.text)
    id = dictionary['id']
    
    await ctx.send(dictionary['summonerLevel'])




def findNamebyId(champid, champions):
    for i in champions['data']:
        if champid == int(champions['data'][i]['key']):
            return champions['data'][i]['name']

def getSummonerURL(summonerName):
    return f'{LConsts.summoner_url}{summonerName}?api_key={LConsts.APIKey}'

@client.command()
async def masteryChestsAlready(ctx, summonerName):
    URL = getSummonerURL(summonerName)
    response = requests.get(URL)
    summoner = json.loads(response.text)
    championURL = requests.get('http://ddragon.leagueoflegends.com/cdn/9.21.1/data/en_US/champion.json')
    champions = json.loads(championURL.text)
    id = summoner['id']
    URL = f'{LConsts.chest_url}{id}?api_key={LConsts.APIKey}'
    response = requests.get(URL)
    dictionary = json.loads(response.text)
    j = 0
    chests = []
    for i in dictionary:
        if dictionary[j]['chestGranted']:
            champid = int(dictionary[j]['championId'])
            chests.append(findNamebyId(champid, champions))
        j += 1
    e = discord.Embed(title = f"Champions {summonerName} got a hextech chest with",
                      description = '\n'.join(chests),
                      colour = discord.Colour.blue())
    await ctx.send(ctx.message.author.mention, embed = e)

@client.command()
async def rankedInfo(ctx, summonerName):
    URL = getSummonerURL(summonerName)
    response = requests.get(URL)
    dictionary = json.loads(response.text)
    id = dictionary['id']
    URL = f'{LConsts.league_summoner_url}{id}?api_key={LConsts.APIKey}'
    response = requests.get(URL)
    dictionary = json.loads(response.text)
    aboutSummoner = []
    j = 0
    while j < len(dictionary):
        for i in dictionary[j]:
            aboutSummoner.append(i)
            aboutSummoner.append(dictionary[j][i])
        j += 1
    summonerInfo = ""
    j = 0
    check = 0
    for i in aboutSummoner:
        if str(i) in ['leagueId', 'summonerId', 'summonerName']:
            check = 1
            continue
        if check:
            check = 0
            continue
        if j == 0:
            summonerInfo += str(i).capitalize() + ': \n'
            j += 1
        elif j == 1:
            j = 0
            summonerInfo += str(i) + '\n'
    
    e = discord.Embed(title = f'About {summonerName}',
                      description = summonerInfo,
                      colour = discord.Colour.blue())
    await ctx.send(ctx.message.author.mention, embed = e)

@client.command()
async def redeye(ctx, URL = None):
    file_name = 'image_something.jpg'
    able = Face_Recognition_Test.make_Evil(URL, file_name)
    if able:
        await ctx.send(file=discord.File(file_name))
        os.remove(file_name)
    else:
        await ctx.send('Please enter a valid URL')
                        

@client.command()
async def quit(ctx):
    await client.logout()
    await client.close()

client.run(token)