import requests, discord, os, time, datetime, classes
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands
load_dotenv('.env')

# FUCKED UP SHIT:
# - NON- SLASH COMMANDS
# - SLASH COMMANDS
# - I HAVE 2 CLIENTS
# - MATH

Survivors = classes.Survivors()
Killers = classes.Killers()

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=';', intents=intents, client=client)
cmds = app_commands.CommandTree(client=client)

def format_time_difference(time_difference):
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days} Days, {hours} Hours, {minutes} Minutes, {seconds} Seconds"

@client.event
async def on_ready():
    await cmds.sync(guild=discord.Object(id=1198070162432200865))
    print("ready")

@bot.command(name="helpme")
async def helpme(ctx):
    embed = discord.Embed(
        title="Dead By Daylight Tracker",
        description='''**Commands**\n
        >>> ;helpme - Sends this message.\n;shrine - Shows the current Shrine of Secrets.\n;reset - Shows the time until the next and since the last rank reset.\n;randomperk(role, amount, excule?) - Returns (amount) random perks from the role chosen excluding the chosen characters.\n''',

        color=discord.Colour.dark_grey()
    )

    await ctx.send(embed=embed)

@bot.command(name="shrine")
async def shrine(ctx):
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

        await ctx.send(embed=embed)
    else:
        print("IT DIDNT WORK FUCKER")

@bot.command(name="reset")
async def reset(ctx):
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

    await ctx.send(embed=embed)

@bot.command(name="randomperk")
async def randomperk(ctx, role: str, amount: str, exclude: list = None):
    if role.lower() == "survivor":
        embedSurvior = discord.Embed(
            title=f"Random Perks, Survivor - {time.strftime('%m/%d/%H:%M:%S')}",
            color=discord.Color.dark_grey())

        if int(amount) > 4 or int(amount) < 0:
            await ctx.send("Please select an amount within 1-4.")

        perks = Survivors.randomizePerk(amount=int(amount), exclude=exclude)
        for i in range(int(amount)):
            embedSurvior.add_field(name=f"Perk{i}: ", value=perks[i-1])

        await ctx.send(embed=embedSurvior)

    elif role.lower() == "killer":
        embedKiller = discord.Embed(
            title=f"Random Perks, Killer - {time.strftime('%m/%d/%H:%M:%S')}",
            color=discord.Color.dark_grey())
        
        if int(amount) > 4 or int(amount) < 0:
            await ctx.send("Please select an amount within 1-4.")

        perks = Killers.randomizePerk(amount=int(amount), exclude=exclude)
        for i in range(int(amount)):
            embedKiller.add_field(name=f"Perk{i}: ", value=perks[i-1])

        await ctx.send(embed=embedKiller)

    else:
        await ctx.send("Invalid Role. Please select 'killer' or 'survivor'.")

@bot.command(name="randomcharacter")
async def randomcharacter(ctx, role: str, exclude: list = None):
    if role.lower() == "survivor":
        embedSurvior = discord.Embed(
            title=f"Random Survivor - {time.strftime('%m/%d/%H:%M:%S')}",
            color=discord.Color.dark_grey())
        
        survivor = Survivors.randomizeSurvivor(exclude=exclude)
        embedSurvior.add_field(name="Survivor:", value=survivor, inline=False)
        await ctx.send(embed=embedSurvior)

    elif role.lower() == "killer":
        embedKiller = discord.Embed(
            title=f"Random Killer - {time.strftime('%m/%d/%H:%M:%S')}",
            color=discord.Color.dark_grey())

        killer = Killers.randomizeKiller(exclude=exclude)
        embedKiller.add_field(name="Killer:", value=killer, inline=False)
        await ctx.send(embed=embedKiller)

    else:
        await ctx.send("Please enter a valid role. Survivor/Killer")

@cmds.command(name="test", description="description") 
async def test(interaction: discord.Interaction):    
    await interaction.response.send_message("command")

client.run(os.getenv('DISCORD_TOKEN'))
