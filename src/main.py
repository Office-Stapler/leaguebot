import discord, re, os, os.path, random, json, requests
from discord.ext import commands

import LConst, LCommands, src.LClasses as LClasses

intents = discord.Intents.default()
intents.members = True
intents.message_content = True


client = commands.Bot(command_prefix = '+', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} logged in')
    print(client.user.id)
    print('-------------')

# finds champion info 
@client.command('fchamp', description = 'Finds basic champion info')
async def fchamp(ctx, *, name):
    champion = LClasses.Champion(name)
    about = LCommands.fChampInfo(champion)
    if not champion.is_valid:
        await ctx.send('Champion not found, please make sure spelling is correct')
        return
    e = discord.Embed(
        title = f'About {champion.data["title"]}',
        colour = discord.Colour.blue()
    )
    e.set_thumbnail(url=champion.get_splash_screen_image())
    for i in list(about.keys())[1:]:
        string = '\n'.join([x for x in about[i]])
        e.add_field(name = i, value = string, inline=False)
    await ctx.send(embed = e)

# @client.command('fskin', description = '')
# async def fskin(ctx, skin = None, *, champ = None):
#     try:
#         n = int(skin)
#         url = LCommands.fSkin(champ, n)
#         if url is None:
#             await ctx.send('Please pick a valid range, use "+listskins" for the list of skins')
#             return
#         await ctx.send(file=discord.File(url))
#     except:
#         print(skin)
#         await ctx.send("Proper usage is {number} {champion}, please double check you're correct")

        
# @client.command('listskin')
# async def listskin(ctx, *, name = None):
#     nchamp = LCommands.fSkin(str(name))
#     if nchamp == None:
#         await ctx.send('Please enter a valid champion')
#         return
#     await ctx.send(nchamp)

# @client.command('abilities')
# async def abilities(ctx, *, champ):
#     champ = LCommands.fAbilities(champ)
#     if champ == []:
#         await ctx.send('Champion not found, usage is +listskin {champion}')
#         return
#     e = discord.Embed(
#         title = f'Passive: {champ.info[12]["name"]}',
#         colour = discord.Colour.dark_green()
#     )
#     file = discord.File(f'data/maindata/img/passive/{champ.info[12]["image"]["full"]}', filename='image.png')
#     e.add_field(name = 'Description', value=champ.info[12]['description'])
#     e.set_thumbnail(url='attachment://image.png')
#     await ctx.send(file=file, embed = e)
#     for i in champ.info[11]:
#         e = discord.Embed(
#             title = i['name'],
#             colour = discord.Color.dark_green()
#         )
#         i['description'] = re.sub('<.*?>', '',  i['description'])
#         file = discord.File(f'data/maindata/img/spell/{i["id"]}.png', filename='image.png')
#         e.set_thumbnail(url="attachment://image.png")
#         e.add_field(name = 'Description', value = i['description'], inline=False)
#         e.add_field(name = 'Cooldown / Level', value = i['cooldownBurn'], inline=False)
#         e.add_field(name = 'Cost / Level', value = i['cost'], inline=False)
#         await ctx.send(file=file, embed = e)


# @client.command('ranchamp')
# async def ranchamp(ctx):
#     Dir = 'data/maindata/champion/'
#     list_champs = os.listdir(Dir)
#     ran = random.randint(0, len(list_champs))
#     m = 0
#     for i in list_champs: 
#         if m == ran:
#             champ = LClasses.champion(str(i).replace('.json', ''))
#             await ctx.send(file=discord.File(champ.getImage()))
#             await ctx.send(champ.name)
#             break
#         m += 1

# @client.command('freechamps')
# async def freechamps(ctx):
#     champs = json.loads(requests.get(LConst.CHAMPION_ROTATION_URL + f'?api_key={LConst.APIKey}').text)
#     embed = discord.Embed(
#         title = 'Free Champion Rotations',
#         colour = discord.Colour.blue(),
#     )
#     free_champs_normal = list(map(LCommands.findNamebyId, champs['freeChampionIds']))
#     free_champs_noob = list(map(LCommands.findNamebyId, champs['freeChampionIdsForNewPlayers']))
#     embed.add_field(name='Free Champions for Regular Players', value=free_champs_normal)
#     embed.add_field(name='Free Champions for Players < level 10', value=free_champs_noob, inline=False)

#     await ctx.send(embed=embed)


# @client.command('summonerinfo')
# async def summonerinfo(ctx, *, name):
#     summoner = LClasses.summoner(name)
#     print(summoner.details)
#     await ctx.send(summoner.details["name"], file=discord.File(summoner.icon))

# @client.command('rmatch')
# async def rmatch(ctx, *, name):
#     summoner = LClasses.summoner(name)
#     print(summoner.details)
#     matches = summoner.find_most_recent_match()
#     print(matches['participantIdentities'])
#     await ctx.send('Done..')
client.run(LConst.DISCORD_TOKEN)