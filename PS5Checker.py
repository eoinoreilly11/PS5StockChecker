import requests
import bs4 as bs
import time
import discord
from discord.ext import commands

client = commands.Bot(command_prefix =  '!')

@client.event
async def on_ready():
    print("Bot Ready")

TOKEN = 'Nzk4MjUxNDk1MjQwNzYxMzc1.X_yTow.ywoTAZVSkY76K9A9PokUoNbg1cE'
imgURL = 'https://i.guim.co.uk/img/media/f58aa676496e9eaba611000477f28d0232fd91eb/0_165_3378_2027/master/3378.jpg?width=620&quality=45&auto=format&fit=max&dpr=2&s=e8c5338394932059caf20ba2516be828'

@client.command(pass_context=True)
async def go(ctx):
    winner  = 0

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

        if stockGS == 'Out Of Stock':
            print('GS Out Of Stock\n')

        else:
            winner = 1
            embed = discord.Embed(
                title = 'PS5 IN STOCK',
                description = 'GAMESTOP IN STOCK',
                url = urlGS,
                color=discord.Color.blue()
            )
            embed.set_thumbnail(url=imgURL)
            await ctx.send(embed=embed)

        if stockSmyths[53:66] == 'js-enable-btn':
            winner = 1
            embed = discord.Embed(
                title = 'PS5 IN STOCK',
                description = 'SMYTHS IN STOCK',
                url = urlSmyths,
                color=discord.Color.blue()
            )
            embed.set_thumbnail(url=imgURL)
            await ctx.send(embed=embed)

        else:
            print('Smyths Out of Stock\n')

            
        if winner == 1:
            break
        time.sleep(30)

client.run(TOKEN)
