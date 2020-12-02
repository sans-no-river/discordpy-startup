import discord
import sys

# さいころの和を計算する用の関数
from func import  diceroll

TOKEN = 'NzgzNjQ2NzA3NDcyNTMxNDc2.X8dx3g.8Wm-n-oDzkdIKpSauhdllIyuj-s'

client = discord.Client()

@client.event
async def on_ready():
    print('--------------')
    print(client.user.name)
    print(client.user.id)
    print('--------------')
    channel = client.get_channel('747404374585770025')
    await channel.send('準備中')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith("!dice"):
        # 入力された内容を受け取る
        say = message.content 

        # [!dice ]部分を消し、AdBのdで区切ってリスト化する
        order = say.strip('!dice ')
        cnt, mx = list(map(int, order.split('d'))) # さいころの個数と面数
        dice = diceroll(cnt, mx) # 和を計算する関数(後述)
        await message.channel.send(dice[cnt])
        del dice[cnt]

        # さいころの目の総和の内訳を表示する
        await message.channel.send(dice)

client.run(TOKEN)
