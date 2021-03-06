import discord
from discord.ext import commands 
import json
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption
import asyncio
from asyncio import sleep
import requests
from PIL import Image, ImageFont, ImageDraw
from discord import File
import io
import random
import os, csv, random, discord, asyncio, requests, json, traceback
from discord.ext import commands
from dotenv import load_dotenv
import discord
import youtube_dl
import os
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import json
import os
import asyncio
import time
import random
from discord import Game
import math, time
import sympy
import numpy
import sqlite3 #модуль sqlite
import discord #модуль discord api
from discord.ext import commands #необходимый класс для обработки команд
from tabulate import tabulate #удобный модуль для рисования таблиц
import json


conn = sqlite3.connect("Discord.db") # или :memory:
cursor = conn.cursor()





bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())
bot.remove_command( 'help' )



@bot.event
async def on_ready():
   DiscordComponents(bot)
print("Бот успешно подключился!")


@bot.command()
async def user(ctx,member:discord.Member = None, guild: discord.Guild = None):
    if member == None:
        emb = discord.Embed(title="Информация о пользователе:", colour = discord.Color.purple())
        emb.add_field(name="Имя: ", value=ctx.message.author.name,inline=False)
        t = ctx.message.author.status
        if t == discord.Status.online:
            d = " В сети"

        t = ctx.message.author.status
        if t == discord.Status.offline:
            d = " Не в сети"

        t = ctx.message.author.status
        if t == discord.Status.idle:
            d = " Не активен"

        t = ctx.message.author.status
        if t == discord.Status.dnd:
            d = " Не беспокоить"

        emb.add_field(name="Статус:", value=d,inline=False)
        emb.add_field(name="Пользовательский статус:", value=ctx.message.author.activity,inline=False)
        emb.add_field(name="Роли:", value=f"{ctx.message.author.top_role.mention}",inline=False)
        emb.add_field(name="Дата создания:", value=ctx.message.author.created_at.strftime("%#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)
        emb.set_footer(text="Windows Assistent © 2021 All rights are sniffed ")
    else:
        emb = discord.Embed(title="Информация о пользователе:", colour = discord.Color.purple())
        emb.add_field(name="Имя:", value=member.display_name,inline=False)
        t = member.status
        if t == discord.Status.online:
            d = " В сети"

        t = member.status
        if t == discord.Status.offline:
            d = " Не в сети"

        t = member.status
        if t == discord.Status.idle:
            d = " Не активен"

        t = member.status
        if t == discord.Status.dnd:
            d = " Не беспокоить"
        emb.add_field(name="Статус:", value=d,inline=False)
        emb.add_field(name="Пользовательский статус:", value=member.activity,inline=False)
        emb.add_field(name="Роли:", value=f"{member.top_role.mention}",inline=False)
        emb.add_field(name="Дата создания:", value=member.created_at.strftime("%#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_footer(text="Windows Assistent © 2021 All rights are sniffed ")
        await ctx.send(embed = emb)

        
        
@bot.command()
async def a(ctx):
   await ctx.send(
    embed = discord.Embed(title = "", description = '''
    Узнайте больше про игру "Phazmofobia!"
    '''),

   components=[
            Select(
                placeholder="Выберете пункт!",
                options=[
                    SelectOption(label="📋 Information", value="1"),

                   SelectOption(label="🛡️ Карты", value="2"),
                   SelectOption(label="🏆 Уровни сложности", value="3"),
                   SelectOption(label="В разработке", value="4"),
                   SelectOption(label="😊 Виды призраков", value="5"),
                ],
                custom_id="select1",
            )
        ]
   )


@bot.command()
async def rules(ctx):
    await ctx.send(
      embed=discord.Embed(title="Правила:", timestamp = ctx.message.created_at,    description = '''
      [1.0] Основные принципы и положение I.
1.1. [Находясь на сервере, вы подтверждаете знание правил и обязуетесь их соблюдать, соглашаясь с тем, что незнание не освобождает от ответственности. В противном случае рискуете получить наказание за нарушение любого из описанных ниже пунктов]
1.2. [Вы должны всегда уважать интересы и увлечения участников на сервере]
1.3. [Любое поведение, которое будет расценено нашими модераторами как неадекватное, способствующее созданию некого отвращения от нахождения в чате (сюда также входит обилие матов), будет наказываться в строгом порядке]
1.4. [Правила в любой момент могут быть изменены/дополнены без предупреждений]
[1.0] Основные принципы и положение II.
1.5. [Администрация является гарантом проекта. Она действует в интересах его целостности и сохранности. Это значит, что в случае вашего препятствования развитию любого сегмента деятельности каталога (общение, партнёрская деятельность, командная деятельность и пр.), администраторы оставляют за собой право наложения ряда ограничений (санкций) против вас и вашего проекта, если сочтёт ваши действия неправомерными и вредоносными]
1.6. [Запрещён обход наказаний и злоупотребление (абуз) правилами любыми доступными способами]
1.7. [Запрещены конфликты любой тяжести на нашем сервере. Мы уважаем интересы и увлечения всех пользователей и будем в жёстком порядке пресекать любые, даже самые мелкие попытки вызвать конфликт на почве чего-либо. Относитесь с уважением к себе и пользователям, с которыми вы коммуницируете]
[2.0] Правила общения в голосовом чате.
2.1. [Запрещено шуметь, дуть в микрофон]
2.2. [Запрещено ретранслировать музыку в микрофон без разрешения на то остальных участников разговора]
2.3. [Дополнительно запрещено нарушение следующих правил: 1.2, 1.6, 3.1, 3.2, 3.3, 3.5, 3.7, 3.8, 3.9, 4.1, 4.2, 4.7, 4.9]
[3.0] Правила общения и поведения I.
[*]3.1. [Запрещены оскорбления, унижения, угрозы, преследование, травля, аморальное поведение (в т.ч. разговоры на темы характера 18+) в отношении пользователей.]
[*]3.2. [Запрещен розжиг политических, религиозных или других конфликтов, межнациональной ненависти(сюда так же входят слова по типу "хохол, москаль" и пр.). Запрещена пропаганда фашизма, нацизма и пр.]
[*]3.3. [Запрещено вводить пользователей сервера в заблуждение, подстрекать, провоцировать, клеветать, шантажировать, попрошайничать]
3.4. [Запрещен спам, флуд, оффтоп, злоупотребление КАПСОМ и всё связанное с этим]
3.5. [Критиковать пользователей, наш сервер [!], или партнерские можно только объективно и по обоснованным причинам]
[3.0] Правила общения и поведения II.
3.6. [Запрещено упоминание человека/людей без веских причин и намеренное злоупотребление системой ответов для обхода данного правила (проверка возможности пинговать не является веской причиной)]
[!]3.7. [Запрещена любая реклама (за исключением отдельно предусмотренной правилами и пользовательского статуса)]
3.8. [Запрещен шок контент, контент 18+ [!], который распространяется без согласия пользователя и не в NSFW-каналах]
[*]3.9. [Запрещено создавать, организовывать и устраивать бунты, интриги против проекта или же его пользователей, проводить открытые или неявные агитации в личных интересах]
3.10. [Запрещено использование: транслита, средств шифровки сообщений, других языков (включая использование созвучных слов с других языков), картинок — для обхода правил или шуток над администрацией проекта]
[4.0] Правила личного характера I.
[~]4.1. [Запрещено переносить конфликты c проекта на другие сервера с целью его эскалации и продолжения, особенно касается случаев унижения и травли пользователей каталога]
4.2. [Запрещено любое грубиянство в отношении пользователей сервера (в особенности только что присоединившихся), которое может побудить покинуть проект (например: на пользовательское "привет" отвечать "пока"; на вопрос, кто ответственен за оформление партнёрства, отвечать "никто" и т.п.)]
4.3. [Запрещены никнеймы, аватары и статусы содержащие в себе: оскорбления, пропаганду фашизма/нацизма, призывы к суициду, травле определенной личности, фишинговые ссылки, ссылки ведущие на сервера сомнительного содержания (хакерство, терроризм, кибербуллинг, краши или ддос серверов Discord и пр.)]
4.4. [Запрещен любой никнейм и/или аватар, что копирует чью-либо личность или же является крайне схожим]
[4.0] Правила личного характера II.
4.5. [Запрещен любой никнейм, что не упоминается стандартными функциями Discord (без режима разработчика)]
4.6. [Запрещено оскорблять проэкт]
[!]4.7. [Запрещается рейдить (например: набегать на сервер  с целью диверсировать их деятельность), крашить (например: внедряться и ломать сервер изнутри), скамить (например: обманывать с целью получения выгоды, шантажировать пользователей или сервер)]
4.8. [Запрещено подделывать доказательства]
4.9. [Запрещен флуд, спам]
Дополнительные моменты:
Без обозначения — работает исключительно на проекте Каталог Серверов.
* — дополнительно работает в личных сообщениях, если ситуация, которая описана в соответствующем пункте, произошла на каталоге серверов и в последствии была перенесена в личные сообщения.
! — условное обозначение, значащее, что данное правило работает везде, где только можно.

     ''' )
    )
   
    




@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def clear(ctx, amount=1, limit_amount=1):
    await ctx.channel.purge(limit=amount+1)
    await ctx.channel.purge(limit=limit_amount)
    author = ctx.message.author
    await ctx.send(
      embed = discord.Embed(title = 'Очистка:', description = f'{author} удалил {amount} сообщений!', colour = discord.Color.purple())
    )


@bot.command (pass_context = True)
@commands.has_permissions( administrator = True)
async def mute1(ctx,member:discord.Member,time:int,reason):
    channel = bot.get_channel (758393130755162123)
    mute = discord.utils.get(ctx.message.guild.roles, name = 'mute')
    lol = discord.Embed(title = 'В муте. Говорить не может!' )
    lol.add_field(name = 'Модератор/админ', value = ctx.message.author.mention, inline = False)
    lol.add_field(name = 'Нарушитель', value = member.mention, inline = False)
    lol.add_field(name= 'Причина', value = reason, inline = False)
    lol.add_field (name = 'Время', value = time, inline = False)
    await member.add_roles (mute)
    await channel.send (embed = lol )
    await asyncio.sleep(time * 60)
    await member.remove_roles (mute)

@bot.command()
async def t(ctx):
    await ctx.send(
      embed=discord.Embed(title = 'Набор в Команду <:emg1:894163315331309599>', description = '''Открыт набор в состав команды на должность <@&897535752085315645> 
`Примечания:`
• <@&897535752085315645>  — человек, отвечающий за партнёрства (заключение и обновление).
• Чтобы подать заявку, необходимо правильно заполнить и отослать следующую анкету:
Анкета:
1. Упоминание самого себя.
2. Ваше полное имя. 
3. Готовы ли вы, в случае чего, пройти проверку в голосовом формате? 
4. Опыт работы. 
5. Ваш часовой пояс. 

Пример:
1. @Windows
2. Вася.
3. Готов.
4. Опыта не имеется.
5. МСК
`Ответственный за набор:`
 <@708035084288131205>
      '''
      )
    )


@bot.command()
async def test(ctx):
    await ctx.send(
      embed=discord.Embed(title =
'Прогресс: <:emoji_2:897548529608818779><:emoji_4:897548597191655514><:emoji_4:897548597191655514><:emoji_4:897548597191655514><:emoji_4:897548597191655514><:emoji_4:897548597191655514><:emoji_6:897548715416494131> ')
    )
   

@bot.command()
async def test1(ctx):
    await ctx.send(
      embed=discord.Embed(title =
'Прогресс: <:emoji_2:897548529608818779><:emoji_3:897548568271933532><:emoji_4:897548597191655514><:emoji_4:897548597191655514><:emoji_4:897548597191655514><:emoji_4:897548597191655514><:emoji_6:897548715416494131> ')
    )
   

@bot.command()
async def test2(ctx):
    await ctx.send(
      embed=discord.Embed(title =
'Прогресс: <:emoji_2:897548529608818779><:emoji_3:897548568271933532><:emoji_3:897548568271933532><:emoji_4:897548597191655514><:emoji_4:897548597191655514><:emoji_4:897548597191655514><:emoji_6:897548715416494131> ')
    )
   

@bot.command()
async def test3(ctx):
    await ctx.send(
      embed=discord.Embed(title =
'Прогресс: <:emoji_2:897548529608818779><:emoji_3:897548568271933532><:emoji_3:897548568271933532><:emoji_3:897548568271933532><:emoji_4:897548597191655514><:emoji_4:897548597191655514><:emoji_6:897548715416494131> ')
    )
   

@bot.command()
async def test4(ctx):
    await ctx.send(
      embed=discord.Embed(title =
'Прогресс: <:emoji_2:897548529608818779><:emoji_3:897548568271933532><:emoji_3:897548568271933532><:emoji_3:897548568271933532><:emoji_3:897548568271933532><:emoji_4:897548597191655514><:emoji_6:897548715416494131> ')
    )
   

@bot.command()
async def test5(ctx):
    await ctx.send(
      embed=discord.Embed(title =
'Прогресс: <:emoji_2:897548529608818779><:emoji_3:897548568271933532><:emoji_3:897548568271933532><:emoji_3:897548568271933532><:emoji_3:897548568271933532><:emoji_4:897548597191655514><:emoji_5:897548685548871680> ')
    )






bot.run("Nzg5ODAwNzMzMzI3MjI4OTM5.X93VQA.5709tgbEaWnwwxrGE0XGc2S9QTU")