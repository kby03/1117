import discord
import requests
import json

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if "!" in message.content:
        if message.content.startswith('!유저조회'):
            if "$" in message.content:
                userName = message.content.split("$")[1]
                userDate = getUserDate(userName)

                e = discord.Embed(title=userDate["userName"])
                e.set_author(name="유저 조회 결과")
                e.set_thumbnail(url=userDate["userImage"])

                for item in userDate["result"]:
                    Game = item["ChampName"] + " - " + item["GameResult"]
                    KDA = item["Kill"] + " / " + item["Death"] + " / " + item["assist"]
                    e.add_field(name=Game, value=KDA, inline=False)
                await message.channel.send(embed=e)

            else:
                await message.channel.send('값이 잘못 요청되었습니다.')
                await message.channel.send('!유저조회$<유저명>')
        else:
            await message.channel.send('명확한 명령어가 아닙니다.')

def getUserDate(userName):
    response = requests.get("http://3964bf147c56.ngrok.io?name="+userName)
    json_val = response.json()
    return json_val

client.run('token')