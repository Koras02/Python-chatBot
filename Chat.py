import discord
import asyncio
import random

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

# 임베드 이미지와 하이퍼 링크 추가


@client.event
async def on_message(message):
    if message.content == "안녕":
        await message.channel.send("안녕!!")

    if message.content == "임베드 이미지":
        embed = discord.Embed(
            # footer 에도 적용
            title='이미지 임베드', description="[내 프사](https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile28.uf.tistory.com%2Fimage%2F99FAE3475C6FDBC734E58D) ", color=0x00ff00)
        # 이미지 불러오기
        # embed.set_thumbnail(
        #     url='https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile28.uf.tistory.com%2Fimage%2F99FAE3475C6FDBC734E58D')
        #  이미지 중간에 넣기
        embed.set_image(
            url='https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile28.uf.tistory.com%2Fimage%2F99FAE3475C6FDBC734E58D')
        await message.channel.send(embed=embed)

    # 랜덤 뽑기
    if message.content == "뽑기":
        ran = random.randint(0, 1)
        if ran == 0:
            d = "꽝"
        if ran == 1:
            d = "당첨"
        await message.channel.send(d)

    # 점심 메뉴
    if message.content == "점심메뉴":
        ran = random.randint(2, 3)
        if ran == 2:
            d = "짜장면"
        if ran == 3:
            d = "짬뽕"
        if ran == 2:
            d = "김밥"
        if ran == 3:
            d = "굶어"
        await message.channel.send(d)

client.run(token)


# pip3 -install pip3 설치해준다.
