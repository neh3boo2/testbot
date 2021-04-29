import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("지원봇")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
   if message.content.startswith("안녕"):
       await message.channel.send("asdasd")

client.run("ODM0NDYyMzM5OTM1ODk1NTc1.YIBPnQ.-8edaYFP8dAiS-OY66kGcjPkPQU")
