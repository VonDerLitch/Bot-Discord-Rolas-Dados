from typing import Optional
import discord
from discord.ext import commands
from key import token
import random


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
TOKEN = token


@client.event
async def on_ready():
    print(f'{client.user} está online')


@client.event
async def on_ready():
    print('Bot conectado como {0.user}'.format(client))


@client.event
async def on_ready():
    print('Bot conectado como {0.user}'.format(client))


@client.event
async def on_ready():
    print('Bot conectado como {0.user}'.format(client))


@client.event
async def on_ready():
    print('Bot conectado como {0.user}'.format(client))


@client.event
async def on_ready():
    print('Bot conectado como {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!rolar'):
        try:
            # Enviar mensagem interativa para solicitar os valores
            await message.channel.send("Digite o número de dados a serem lançados:")
            quantidade_dados = await aguardar_resposta(message)

            await message.channel.send("Digite o número de dados de fome:")
            quantidade_fome = await aguardar_resposta(message)

            await message.channel.send("Digite a dificuldade:")
            dificuldade = await aguardar_resposta(message)

            # Converter os valores para inteiros
            quantidade_dados = int(quantidade_dados)
            quantidade_fome = int(quantidade_fome)
            dificuldade = int(dificuldade)

            # Rolar os dados
            resultados_normais = [random.randint(1, 10) for _ in range(quantidade_dados)]
            resultados_fome = [random.randint(1, 10) for _ in range(quantidade_fome)]

            # Contar os sucessos dos dados normais
            sucessos_normais = 0
            for resultado in resultados_normais:
                if resultado >= dificuldade:
                    if resultado >= 10:
                        sucessos_normais += 2
                    else:
                        sucessos_normais += 1

            # Contar os sucessos dos dados de fome
            sucessos_fome = sum(1 for resultado in resultados_fome if resultado >= dificuldade)

            # Enviar os resultados para o canal do Discord
            resposta = f"Resultados dos dados normais: {', '.join(map(str, resultados_normais))}\n"
            resposta += f"Sucessos nos dados normais: {sucessos_normais}\n\n"
            resposta += f"Resultados dos dados de fome: {', '.join(map(str, resultados_fome))}\n"
            resposta += f"Sucessos nos dados de fome: {sucessos_fome}"
            await message.channel.send(resposta)

        except (IndexError, ValueError):
            await message.channel.send('Uso correto: !rolar')


async def aguardar_resposta(message):
    def check(m):
        return m.author == message.author and m.channel == message.channel

    resposta = await client.wait_for('message', check=check)
    return resposta.content



client.run(token)
