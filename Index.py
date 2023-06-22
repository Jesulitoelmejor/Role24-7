import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

@bot.command()
async def roleadd(ctx, user: discord.Member, role_name):
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    
    if role is None:
        await ctx.send(f"No se encontró el rol '{role_name}'.")
        return
    
    await user.add_roles(role)
    await ctx.send(f"Se añadió el rol '{role_name}' al usuario {user.mention}.")

bot.run('MTEyMTM5MTY4NzA1MTI1MTc0Mw.GB-aiC.ouzoZessVDftCqqGC1GklETCoewpdIM73AnjUk')  # Reemplaza 'TOKEN' con tu token de Discord
