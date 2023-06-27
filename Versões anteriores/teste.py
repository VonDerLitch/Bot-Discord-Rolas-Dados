from typing import Optional
import discord
from discord.ext import commands
from key import token
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
TOKEN = token

@bot.event
async def on_ready():
    print(f'{bot.user} está online')

@bot.command()
async def rolar(ctx, quantidade_dados: int, quantidade_fome: int, dificuldade: int):
    resultados_normais = [random.randint(1, 10) for _ in range(quantidade_dados)]
    resultados_fome = [random.randint(1, 10) for _ in range(quantidade_fome)]

    sucessos_normais = 0
    for resultado in resultados_normais:
        if resultado >= dificuldade:
            if resultado >= 10:
                sucessos_normais += 2
            else:
                sucessos_normais += 1

    sucessos_fome = sum(1 for resultado in resultados_fome if resultado >= dificuldade)

    embed = discord.Embed(title="Resultado dos Dados", color=discord.Color.red())
    embed.add_field(name="Dados Normais", value=", ".join(map(str, resultados_normais)), inline=False)
    embed.add_field(name="Dados de Fome", value=", ".join(map(str, resultados_fome)), inline=False)
    embed.add_field(name="Sucessos (Dados Normais)", value=str(sucessos_normais), inline=False)
    embed.add_field(name="Sucessos (Dados de Fome)", value=str(sucessos_fome), inline=False)
    embed.set_footer(text=f"Requisitado por {ctx.author.display_name}")

    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Por favor, forneça todos os argumentos necessários.")

bot.run(TOKEN)
