from typing import Optional
import discord
from discord.ext import commands
from key import token
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
TOKEN = token

@bot.event
async def on_ready():
    print(f'{bot.user} está online')

@bot.command()
async def rolar(ctx):
    await ctx.send("Vamos começar a rolar os dados Cainita. Digite o número de dados a serem lançados:")
    
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        quantidade_dados = await bot.wait_for('message', check=check, timeout=60.0)
        quantidade_dados = int(quantidade_dados.content)

        await ctx.send("Agora, digite o número de dados da Besta:")
        quantidade_fome = await bot.wait_for('message', check=check, timeout=60.0)
        quantidade_fome = int(quantidade_fome.content)

        await ctx.send("Por fim, digite a dificuldade:")
        dificuldade = await bot.wait_for('message', check=check, timeout=60.0)
        dificuldade = int(dificuldade.content)

        await ctx.send("Rolando dados ...")
        resultados_normais = [random.randint(1, 10) for _ in range(quantidade_dados)]
        await ctx.send("Rolando dados da Besta...")
        resultados_fome = [random.randint(1, 10) for _ in range(quantidade_fome)]

        await ctx.send("Calculando sucessos dos dados...")
        sucessos_normais = 0
        for resultado in resultados_normais:
            if resultado >= dificuldade:
                if resultado >= 10:
                    sucessos_normais += 2
                else:
                    sucessos_normais += 1

        await ctx.send("Calculando sucessos dos dados da besta...")
        sucessos_fome = sum(1 for resultado in resultados_fome if resultado >= dificuldade)

        member = ctx.author

        name = member.display_name
        pfp = member.display_avatar

        embed = discord.Embed(title="Resultado dos Dados", color=discord.Color.red())
        embed.set_author(name=f"{name}")
        embed.set_thumbnail(url=f"{pfp}")
        embed.add_field(name="Dados Lançados", value=", ".join(map(str, resultados_normais)), inline=False)
        embed.add_field(name="Dados da Besta Lançados", value=", ".join(map(str, resultados_fome)), inline=False)
        embed.add_field(name="Sucessos (Dados)", value=str(sucessos_normais), inline=False)
        embed.add_field(name="Sucessos (Dados da Besta)", value=str(sucessos_fome), inline=False)
        embed.set_footer(text=f"Requisitado por {ctx.author.display_name}")

        await ctx.send(embed=embed)

    except asyncio.TimeoutError:
        await ctx.send("Tempo limite excedido. Por favor, tente novamente.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Por favor, forneça todos os argumentos necessários.")

bot.run(TOKEN)
