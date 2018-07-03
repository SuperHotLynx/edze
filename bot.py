from bs4 import BeautifulSoup
bs = BeautifulSoup
import requests
import discord
from discord.ext import commands

url = "https://edenszero.wikia.com/wiki/Special:Search?query="
TOKEN = ''

client = commands.Bot(command_prefix = ',')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping():
    await client.say('Pong!')


@client.command()
async def wiki(*args):
    output = ''
    for word in args:
        output += word
        output += '+'
    output = url+output
    print(output)
    await client.say(serch(output))





def serch(url):

    print('got url:'+ url)
    htmlC = requests.get(url).content

    results = []
    resultsCount = 0
    bareme = ''


    page1 = bs(htmlC, 'html.parser')

    alinks = page1.find_all('a')

    for eachLink in alinks:

        if 'class' in eachLink.attrs:
            if eachLink['class'][0] == 'result-link':
                results.append(eachLink.get('href'))
                resultsCount = resultsCount+1
                if(resultsCount == 3):
                    break

    for finalresults in results:
        print('trying this::' + finalresults + ': ')
        print('------------------------------------\n')
        htmlC = requests.get(finalresults).content
        page2 = bs(htmlC, 'html.parser')
        sir = page2.find(id="mw-content-text").p.text.lower()

        print('yes here you go:')
        print(sir)
        bareme = sir
        break
    
    print('ssssssssssssssssssssssssssssssssss')
    print(bareme)

    return bareme

client.run(TOKEN)
