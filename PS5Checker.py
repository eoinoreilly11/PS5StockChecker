import requests
import bs4 as bs
import time
import discord
from discord.ext import commands

client = commands.Bot(command_prefix =  '!')

@client.event
async def on_ready():
    print("Bot Ready")

TOKEN = 'BOT_TOKEN'
imgURL = 'https://i.guim.co.uk/img/media/f58aa676496e9eaba611000477f28d0232fd91eb/0_165_3378_2027/master/3378.jpg?width=620&quality=45&auto=format&fit=max&dpr=2&s=e8c5338394932059caf20ba2516be828'

@client.command(pass_context=True)
async def go(ctx):
    winnerG = 0
    winnerS = 0

    while 1:
        
        #GameStop
        urlGS = 'https://www.gamestop.ie/PlayStation%205/Games/72504/playstation-5-console'
        content = requests.get(urlGS)
        soup = bs.BeautifulSoup(content.text, 'lxml')
        stockGS = soup.find("div", {"class": "bigBuyButtons SPNOpenMap"}).find('a').text

        #Smyths
        urlSmyths = 'https://www.smythstoys.com/ie/en-ie/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259'
        content = requests.get(urlSmyths)
        soup = bs.BeautifulSoup(content.text, 'lxml')
        stockSmyths = str(soup.find("form", {"id": "customAddToCartForm"}).find('button'))

        if winnerG == 0:
            if stockGS == 'Out Of Stock':
                print('GS Out Of Stock...')

            else:
                winnerG = 1
                embed = discord.Embed(
                    title = 'PS5 IN STOCK',
                    description = 'GAMESTOP IN STOCK',
                    url = urlGS,
                    color=discord.Color.blue()
                )
                embed.set_thumbnail(url=imgURL)
                await ctx.send(embed=embed)


        if  winnerS == 0:
            if 'js-enable-btn' in stockSmyths:
                winnerS = 1
                embed = discord.Embed(
                    title = 'PS5 IN STOCK',
                    description = 'SMYTHS IN STOCK',
                    url = urlSmyths,
                    color=discord.Color.blue()
                )
                embed.set_thumbnail(url=imgURL)
                await ctx.send(embed=embed)

            else:
                print('Smyths Out of Stock...\n')

            
        if winnerG == 1 and winnerS == 1:
            break
        time.sleep(3)

client.run(TOKEN)
