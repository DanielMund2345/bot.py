import discord

from emoji import *


# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} se unió {discord.utils.format_dt(member.joined_at)}')
@client.event
async def on_ready():
    print(f'Bienvenido, estoy en discord como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hola'):
        await message.channel.send("Hola amigo")
    elif message.content.startswith('adiós'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('genera una contraseña:'):
        await message.channel.send(gen_pass(8))
    elif message.content.startswith('¿Cuál es tu nombre?') or message.content.startswith('¿Cual es tu nombre?'):
        await message.channel.send("Mund 😁")
    elif message.content.startswith("genera un emoji"):
        await message.channel.send(gen_emodji())
    elif message.content.startswith("1234"):
        await message.channel.send("Accediste al usuario Daniel: DanielMund2345")
    elif message.content.startswith("Bolivia"):
        await message.channel.send("Bolivia es un país fascinante en el corazón de América del Sur. Y llena de historia española")
    elif message.content.startswith("Buscame la cancion 1"):
       await message.channel.send("https://www.bing.com/ck/a?!&&p=9837e60e9c03ba05JmltdHM9MTcyNjc5MDQwMCZpZ3VpZD0xMWZiMTUxZC0yNmE1LTZmNDEtMGVlZC0wMWM4MjcxYzZlZDMmaW5zaWQ9NTUwMA&ptn=3&ver=2&hsh=3&fclid=11fb151d-26a5-6f41-0eed-01c8271c6ed3&psq=enlace+de+youtube+endgame+waterflame&u=a1aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g_dj1vcUJDT2x5Y1JEaw&ntb=1")
    elif message.content.startswith("Buscame la imagen 1"):
        await message.channel.send("https://th.bing.com/th?id=OIP.xKdegcrk7HvRPEPWWB74sAHaFe&w=290&h=215&c=8&rs=1&qlt=90&o=6&dpr=1.1&pid=3.1&rm=2")
    elif message.content.startswith("coin"):
        image_url, message_text = flip_coin()
        await message.channel.send(message_text)
        await message.channel.send(image_url)
    else:
        await message.channel.send(message.content)

client.run("MTI4NDMwMDAxMzYyMjUyNjA1NA.GLAYQF.tP6PvatE4phM8qA0CzLaJSc_DjPedGn1mqzB7k")
