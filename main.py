import discord
from discord import Status
from keep_alive import keep_alive
voice = '929348909304782848' # put channel id here
client = discord.Client(self_bot =True)
@client.event
async def on_ready():
    channel = await client.fetch_channel(voice)
    if channel != None:
        try:
            await channel.connect(reconnect=True)
            print("connected ✅")
        except :
            print("can't connect to that channle ❎")
        try:
            await channel.guild.change_voice_state(channel=channel, self_mute = True, self_deaf=True)
        except:
            print("can't make u mute and defean ❎")
    else: 
        print("can't find that channle ❎")
    await client.change_presence(status=Status.invisible)
    print(f"{client.user} : joined : {channel} / now your status is invisible")
keep_alive()
client.run("ODk1NTc0MDMxODkyMzY5NDUw.YdmCew.QZdwJW-ZYh2qI9K4Sl20T6tUlHc")


