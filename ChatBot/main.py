# -*- coding: utf-8 -*-

import constant as c
import discord
import os

client = discord.Client()

@client.event
# 起動時に反応する
async def on_ready(): 
    # ログイン通知
    print('ログインしました')

@client.event
# サーバに誰かが新しく入ってきたときに反応する
async def on_member_join(member):
    # 挨拶と説明
    channel = member.guild.system_channel
    text = "輪講サーバへ！さぁ皆も早く ChatBot 作るんだ！"
    embed = discord.Embed(title="ようこそ！", description = text, color=0xeee657)
    await channel.send(embed=embed)
    # 新人さんにGESTタグの付与
    role = discord.utils.get(member.guild.roles, name='M1')
    await member.add_roles(role)

@client.event
# 何かしら発言があったときに反応する
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # サーバ側から終了できないので必須
    if message.content == '/もう帰っていいよ':
        await message.channel.send('お疲れさまー')
        print('ログアウトしました')
        await client.logout()

    # こんな感じで定型文を吐ける
    if message.content == '/ふくろう':
        await message.channel.send('ふくろうはいいぞ')
    if message.content == '/なんかしゃべって':
        await message.channel.send('無茶ぶりがすぎる')
    if message.content == 'おはよう':
        await message.channel.send('おはよう')
    
# TOKEN = "" # ここにトークン書いてね
# client.run(TOKEN)
client.run(c.TOKEN)