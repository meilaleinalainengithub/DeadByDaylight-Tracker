import requests, discord, os, time, datetime, classes
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
load_dotenv('.env')

# FUCKED UP SHIT:
# - PARAMETERS ARE FUCKED
# - MATH

Survivors = classes.Survivors()
Killers = classes.Killers()

bot = commands.Bot(command_prefix=';', intents=discord.Intents.all())

def format_time_difference(time_difference):
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days} Days, {hours} Hours, {minutes} Minutes, {seconds} Seconds"

@bot.event
async def on_ready():
    e = await bot.tree.sync()
    print(e)

@bot.tree.command(name="help", description="Helps You... read the name")
async def helpme(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Dead By Daylight Tracker",
        description='''**Commands**\n
        >>> ;helpme - Sends this message.\n;shrine - Shows the current Shrine of Secrets.\n;reset - Shows the time until the next and since the last rank reset.\n;randomperk(role, amount, excule?) - Returns (amount) random perks from the role chosen excluding the chosen characters.\n''',

        color=discord.Colour.dark_grey()
    )

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="shrine", description="Shows current Shrine of Secrets")
async def shrine(interaction: discord.Interaction):
    response = requests.get("https://dbd.tricky.lol/api/shrine")
    if response.status_code == 200:
        data = response.json()
        embed = discord.Embed(
            title=f"Shrine of Secrets: {time.strftime('%m/%d/%H:%M:%S')}",
            description="NOTE: Some perks aren't registered in the API",
            color=discord.Color.dark_grey()
        )

        embed.add_field(name="Shrine ID: ", value=data["id"], inline=True)
        embed.add_field(name="Ends: ", value=datetime.datetime.fromtimestamp(data['end']).strftime('%Y-%m-%d %H:%M:%S'), inline=True)
        embed.add_field(name="Perks:", value="\n\n".join([f"**{perk['id']}**\n**Bloodpoints:** {perk['bloodpoints']},\n**Shards:** {perk['shards']}" for perk in data['perks']]), inline=False)

        await interaction.response.send_message(embed=embed)
    else:
        print("IT DIDNT WORK FUCKER")

@bot.tree.command(name="reset", description="Shows next and past rank reset")
async def reset(interaction: discord.Interaction):
    current_time = datetime.datetime.now()
    last_target_date = datetime.datetime(current_time.year, current_time.month, 13)
    last_time_difference = current_time - last_target_date

    if current_time.day <= 13:
        next_target_date = last_target_date
    else:
        next_target_date = last_target_date.replace(day=13) + datetime.timedelta(days=30)

    next_time_difference = next_target_date - current_time

    last_reset = format_time_difference(last_time_difference)

    embed = discord.Embed(
        title=f"Rank Reset - {time.strftime('%m/%d/%H:%M:%S')}",
        description="NOTE: This could be wrong, ChatGPT helped with the math so :/",
        color=discord.Color.dark_grey()
    )

    embed.add_field(name="**Last Reset:**", value=f"{last_reset} ago", inline=False)
    embed.add_field(name="**Next Reset:**", value=f"CURRENTLY FUCKED CUS I CANT TO MATH", inline=False)

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="randomperk", description="idk man gives you a random character")
async def randomperk(interaction: discord.Interaction, role: str, amount: int, exclude: str = None):
    if role.lower() == "survivor":
        embedSurvior = discord.Embed(
            title=f"Random Perks, Survivor - {time.strftime('%m/%d/%H:%M:%S')}",
            color=discord.Color.dark_grey())

        if int(amount) > 4 or int(amount) < 0:  
            await interaction.response.send_message("Please select an amount within 1-4.")

        perks, character = Survivors.randomizePerk(amount=int(amount), exclude=exclude)
        for i in range(int(amount)):
            embedSurvior.add_field(name=f"Perk {i+1}: ", value=f'{perks[i-1]} - {character}', inline=False)

        await interaction.response.send_message(embed=embedSurvior)

    elif role.lower() == "killer":
        embedKiller = discord.Embed(
            title=f"Random Perks, Killer - {time.strftime('%m/%d/%H:%M:%S')}",
            color=discord.Color.dark_grey())
        
        if int(amount) > 4 or int(amount) < 0:
            await interaction.response.send_message("Please select an amount within 1-4.")

        perks, character = Killers.randomizePerk(amount=int(amount), exclude=exclude)
        for i in range(int(amount)):
            embedKiller.add_field(name=f"Perk {i+1}: ", value=f'{perks[i-1]} - {character}', inline=False)

        await interaction.response.send_message(embed=embedKiller)

    else:
        await interaction.response.send_message("Invalid Role. Please select 'killer' or 'survivor'.")

@bot.tree.command(name="randomcharacter", description="idk man gives you a random character")
async def randomcharacter(interaction: discord.Interaction, role: str, exclude: str = None):
    if role.lower() == "survivor":
        embedSurvior = discord.Embed(
            title=f"Random Survivor - {time.strftime('%m/%d/%H:%M:%S')}",
            color=discord.Color.dark_grey())
        
        survivor = Survivors.randomizeSurvivor(exclude=exclude)
        embedSurvior.add_field(name="Survivor:", value=survivor, inline=False)
        await interaction.response.send_message(embed=embedSurvior)

    elif role.lower() == "killer":
        embedKiller = discord.Embed(
            title=f"Random Killer - {time.strftime('%m/%d/%H:%M:%S')}",
            color=discord.Color.dark_grey())

        killer = Killers.randomizeKiller(exclude=exclude)
        embedKiller.add_field(name="Killer:", value=killer, inline=False)
        await interaction.response.send_message(embed=embedKiller)

    else:
        await interaction.response.send_message("Please enter a valid role. Survivor/Killer")

bot.run(os.getenv('DISCORD_TOKEN'))
