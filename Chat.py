import discord
import asyncio

client = discord.Client()

# 디스코드 bot 코드
token = "ODE4ODUxOTAxODc3MTI1MTUz.YEeFQg.BWfVybKcLKpP5NM-gb9Rljfdhvc"


# 나머지 이미지 코드
@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 연결 되었습니다.')
    game = discord.Game('봇이 활동중에 표시 될 이름')
    await client.change_presence(status=discord.Status.online, activity=game)

client.run(token)
#  기본작성 끝

# pip3 -install
