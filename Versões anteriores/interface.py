import discord
from discord.ext import commands
from key import token

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

async def on_ready():
    print("Bot está online")


@bot.command()
async def embed(ctx, member:discord.Member = None):
    if member == None:
        member = ctx.author
    
    name = member.display_name
    pfp = member.display_avatar

    embed = discord.Embed(title = "A noite Comanda", description="Os dados foram lançados", color = discord.Color.red())
    embed.set_author(name=f"{name}")
    embed.set_thumbnail(url=f"{pfp}")
    embed.add_field(name="Dados", value="Dados")
    embed.add_field(name="Fome", value="Fome", inline=True)
    embed.add_field(name="Dificuldade", value="Dificuldade", inline=True)
    embed.set_footer(text=f"{name} teste")

    await ctx.send(embed=embed)
    

bot.run(token)