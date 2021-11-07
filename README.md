<h1 align="center">Welcome to Alt_Account_Client 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <img src="https://img.shields.io/badge/pyhton-3.9.7-blue" />
  <img src="https://img.shields.io/badge/author-Kumarozh-lightgrey" />
</p>

> A source code for your discord account to make it online or join a voice channel 

## Prerequisites

- python >=3.9.7

## Install

```sh
pip install -r requirment.txt
```

## Usage

```sh
python main.py
```

## Code

```python 
import discord
from discord import status 
token = 'token'
voice = 'id' 
client = discord.Client(self_bot =True)
@client.event
async def on_ready():
    channel = await client.fetch_channel(voice1)
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
client.run(f"{token}")
```

## Author

👤 **Kumarozh**

* GitHub: [@Kumarozh](https://github.com/Kumarozh)
* Discord: [@◤ wagner 𝐑𝗈мaη𝐜𝐞](https://discordapp.com/users/867431299673620500/)

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2021 [Kumarozh](https://github.com/Kumarozh).<br />
This project is [MIT](https://en.wikipedia.org/wiki/MIT_License) licensed.
