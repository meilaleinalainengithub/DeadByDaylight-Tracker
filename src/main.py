import requests, discord, os, time, datetime, classes
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv('.env')

Survivors = classes.Survivors()
Killers = classes.Killers()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=';', intents=intents)

def format_time_difference(time_difference):
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days} Days, {hours} Hours, {minutes} Minutes, {seconds} Seconds"

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
    next_reset = format_time_difference(next_time_difference)

    embed = discord.Embed(
        title=f"Rank Reset - {time.strftime('%m/%d/%H:%M:%S')}",
        description="NOTE: This could be wrong, ChatGPT helped with the math so :/",
        color=discord.Color.dark_grey()
    )

    embed.add_field(name="**Last Reset:**", value=f"{last_reset} ago", inline=False)
    embed.add_field(name="**Next Reset:**", value=f"In {next_reset}", inline=False)

    await ctx.send(embed=embed)

@bot.command(name="randomperk")
async def randomperk(ctx, role: str, amount: int, exclude: list = None):
    embedSurvior = discord.Embed(
            title=f"Random Perks, Survivor - {time.strftime('%m/%d/%H:%M:%S')}",
            color=discord.Color.dark_grey())

    embedKiller = discord.Embed(
            title=f"Random Perks, Killer - {time.strftime('%m/%d/%H:%M:%S')}",
            color=discord.Color.dark_grey())
    
    if role.lower() == "survivor":
        if amount > 4 or amount < 0:
            await ctx.send("Please select an amount within 1-4.")

        perks = Survivors.randomizePerk(amount=amount, exclude=exclude)
        for i in range(amount):
            embedSurvior.add_field(name=f"Perk{i}: ", value=perks[i-1])

    elif role.lower() == "killer":
        pass

    else:
        await ctx.send("Invalid Role. Please select 'killer' or 'survivor'.")

@bot.command(name="randomcharacter")
async def randomcharacter(ctx, role: str, exclude: list = None):
    embedSurvior = discord.Embed(
            title=f"Random Survivor - {time.strftime('%m/%d/%H:%M:%S')}",
            color=discord.Color.dark_grey())

    embedKiller = discord.Embed(
            title=f"Random Killer - {time.strftime('%m/%d/%H:%M:%S')}",
            color=discord.Color.dark_grey())
    
    if role.lower() == "survivor":
        survivor = Survivors.randomizeSurvivor(exclude=exclude)
        embedSurvior.add_field(name="Survivor:", value=survivor, inline=False)
        await ctx.send(embed=embedSurvior)

    elif role.lower() == "killer":
        pass

    else:
        await ctx.send("Please enter a valid role. Survivor/Killer")

bot.run(os.getenv('DISCORD_TOKEN'))
