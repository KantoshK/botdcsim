import random

import discord

import locale
import time

"""if __name__ == '__main__':
    bot.run_discord_bot()"""

#-----------------------------------------------

TOKEN = 'ODE0MjM4MjY2NzkzNzg3Mzk0.GCz9-R.Diy8X7cRcOY6RLGnnNug_81tMirnJQMRW5j_EY'

async def send_message(message, user_message, is_private):
    try:
        response = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception:
        #print("Kullanıcı komut yazmadı. Normal mesaj yazdı.")
        return None

def run_discord_bot():
    TOKEN = 'ODE0MjM4MjY2NzkzNzg3Mzk0.GCz9-R.Diy8X7cRcOY6RLGnnNug_81tMirnJQMRW5j_EY'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} su anda calisiyor")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        locale.setlocale(locale.LC_ALL, 'turkish')
        zaman = time.strftime('%c')

        print(f"({zaman} / Channel: {channel}) {username}: {user_message}")

        """if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:"""
        await send_message(message, user_message, is_private=False)

    client.run(TOKEN)

#-----------------------------------------------------------

def get_response(message: str) -> str:
    meydan_list = []
    with open("meydan.txt", "r", encoding="UTF-8") as dosya:
        meydanlar = dosya.readlines()
        for meydan in meydanlar:
            meydan_list.append(meydan.replace("\n",""))

        meydan_sec1 = random.choice(meydan_list)
        meydan_sec2 = random.choice(meydan_list)

        while meydan_sec1 == meydan_sec2:
            meydan_sec2 = random.choice(meydan_list)

    prefix = "!"
    p_message = message.lower()

    if p_message.startswith(prefix):

        if p_message == f'{prefix}komutlar':
            return 'Prefix: -- (Komutların başına -- yazılır)\n--rota_oner: İç hatlardan bir uçuş rotası önerir.'

        elif p_message == f'{prefix}merhaba':
            return 'Heyyy!'

        elif p_message == f'{prefix}help':
            return 'Yardım geldi!'
        
        elif p_message == f'{prefix}deneme':
            return 'deneme'
        
        #deneme

        elif p_message == f'{prefix}rotaoner':
            return f'{meydan_sec1}  >>>  {meydan_sec2}'

        elif p_message == f'{prefix}rotaoner-fm':
            while meydan_sec2 == meydan_list[0]:
                meydan_sec2 = random.choice(meydan_list)
            return f'İstanbul Havalimanı (LTFM)  >>>  {meydan_sec2}'

        elif p_message == f'{prefix}rotaoner-ac':
            while meydan_sec2 == meydan_list[1]:
                meydan_sec2 = random.choice(meydan_list)
            return f'Ankara Esenboğa Havalimanı (LTAC)  >>>  {meydan_sec2}'

        elif p_message == f'{prefix}rotaoner-fj':
            while meydan_sec2 == meydan_list[15]:
                meydan_sec2 = random.choice(meydan_list)
            return f'İstanbul Sabiha Gökçen Havalimanı (LTFJ)  >>>  {meydan_sec2}'

        elif p_message == f'{prefix}rotaoner-bj':
            while meydan_sec2 == meydan_list[16]:
                meydan_sec2 = random.choice(meydan_list)
            return f'İzmir Adnan Menderes Havalimanı (LTBJ)  >>>  {meydan_sec2}'

        return 'Böyle bir komut yok'

if __name__ == '__main__':
    run_discord_bot()
