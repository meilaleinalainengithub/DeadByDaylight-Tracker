import requests, discord, os, time, datetime, classes
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
load_dotenv('.env')

Survivors = classes.Survivors()
Killers = classes.Killers()

bot = commands.Bot(command_prefix=';', intents=discord.Intents.all())

@bot.event
async def on_ready():
    e = await bot.tree.sync()
    print(e)

@bot.tree.command(name="help", description="Helps You... read the name")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Dead By Daylight Tracker",
        description='''**Commands**\n
        >>> /help - Sends this message.\n/shrine - Shows the current Shrine of Secrets.\n/reset - Shows the time until the next and since the last rank reset.\n/randomperk(role, amount, exclude?) - Returns (amount) random perks from the role chosen excluding the chosen characters.\n/randomcharacter(role, exclude?) - Returns a random character from the role chosen excluding the chosen characters''',
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

@bot.tree.command(name="randomperk", description="idk man gives you a random character")
async def randomperk(interaction: discord.Interaction, role: str, amount: int, exclude: str = None):
    if role.lower() == "survivor" or role.lower() == "killer":
        embed = discord.Embed(
            title=f"Random Perks, {role.capitalize()} - {time.strftime('%m/%d/%H:%M:%S')}",
            color=discord.Color.dark_grey())

        if int(amount) > 4 or int(amount) < 0:  
            await interaction.response.send_message("Please select an amount within 1-4.")

        if role.lower() == "survivor":
            perks, characters = Survivors.randomizePerk(amount=int(amount), exclude=exclude)      
        elif role.lower() == "killer":
            perks, characters = Killers.randomizePerk(amount=int(amount), exclude=exclude)
            
        for i in range(int(amount)):
            embed.add_field(name=f"Perk {i+1}: ", value=f'{perks[i-1]} - {characters[i-1]}', inline=False)
        await interaction.response.send_message(embed=embed)

    else:
        await interaction.response.send_message("Invalid Role. Please select 'killer' or 'survivor'.")

@bot.tree.command(name="randomcharacter", description="idk man gives you a random character")
async def randomcharacter(interaction: discord.Interaction, role: str, exclude: str = None):
    if role.lower() == "survivor":
        embed = discord.Embed(
            title=f"Random {role.capitalize()} - {time.strftime('%m/%d/%H:%M:%S')}",
            color=discord.Color.dark_grey())
        
        if role.lower() == "survivor":
            character = Survivors.randomizeSurvivor(exclude=exclude)
        elif role.lower() == "killer":
            character = Killers.randomizeKiller(exclude=exclude)

        embed.add_field(name=f"{role.capitalize()}:", value=character, inline=False)
        await interaction.response.send_message(embed=embed)

    else:
        await interaction.response.send_message("Please enter a valid role. Survivor/Killer")

bot.run(os.getenv('DISCORD_TOKEN'))
