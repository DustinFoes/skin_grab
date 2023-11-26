import discord, os, colored, traceback
from discord.ext import commands
from dotenv import load_dotenv

# create a bot instance to be used for slash commands
Intents: discord.Intents = discord.Intents.all() # ALL intents are not required, but makes it easier to add features later on
Activity: discord.Activity = discord.Activity(type=discord.ActivityType.watching, name="CSkins")
bot: commands.Bot = commands.Bot(activity=Activity, intents=Intents)

# // AUTOMATIC LOADING COGS //
for file in os.listdir("./example_bot/cogs"):
    if file.endswith(".py"):
        try: bot.load_extension(f"cogs.{file[:-3]}")
        
        except Exception as Error: 
            print(f"{colored.fg('#ff0000')} Error whilst Starting up {file[:-3]} Cog: {Error}")
            print(traceback.format_exc())

# // ON BOT READY: DELIVER STARTUP MESSAGE & START TASKS //
@bot.event  
async def on_ready() -> None:
    print(f"--------------------------------------\n{bot.user} is ready and online!\n--------------------------------------")
    print(f'-------------------------------------------------------\nSuccessfully Established a Connection to the Database\n-------------------------------------------------------')


# // RUN THE BOT //
load_dotenv()
bot.run(os.getenv("TOKEN"))