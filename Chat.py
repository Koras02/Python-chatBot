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

#  기본작성 끝

# 메세지 답하는 기능 추가


@client.event
async def on_message(message):
    if message.content == "그렇구만":
        await message.channel.send("하하하하!")

    if message.content == "누구냐고":
        await message.channel.send("누구긴 누구야!! 너지!")

    if message.content == "내일 점심 뭐먹을까??":
        await message.channel.send("소금듬뿍 들어간 돼지고기 김치주먹밥을 추천할께 친구야!!")

#  임베드 이미지 추가
    if message.content == "임베드 한잔 추가":
        embed = discord.Embed(
            title="알겠습니다", description="다른 거 필요하시면 불러주세용", color=0x00ff00)
        embed.add_field(name="지금 무엇을 상상하신건가 자네??", value="하지마??", inline=True)
        embed.add_field(name="지금 무엇을 상상하신건가 자네?? (2스택)",
                        value="하지마?? (2스택)", inline=True)
        embed.set_footer(text="무엇을 원하는지는 당신이 알아서 맞춰봐")
        await message.channel.send(embed=embed)

client.run(token)


# pip3 -install pip3 설치해준다.
