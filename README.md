```

import asyncio, os, time, aiohttp
import aiohttp
from pyrogram import filters
from Raxhub import Raxhub as papaRax
from RaxMUSIC import app

@app.on_message(filters.command("Raxhub"))
async def Raxhub(_, message):
    text = message.text[len("/Raxhub") :]
    papaRax(f"{text}").save(f"Raxhub_{message.from_user.id}.png")
    await message.reply_photo(f"Raxhub_{message.from_user.id}.png")
    os.remove(f"Raxhub_{message.from_user.id}.png")

```
```
sh pip install Raxhub

```




# RaxHUB 


![Project Image](https://github.com/akshayxt/Raxhub/blob/main/out.png)

