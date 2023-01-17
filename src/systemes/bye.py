from nextcord.ext import commands
import nextcord
from database import add, delete, search

class Bye(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "aurevoir", description = "Activer le système de aurevoir sur le serveur")
  async def Leave_slash(self, interaction: nextcord.Interaction, channel: nextcord.TextChannel = nextcord.SlashOption(name="salon", description="Le salon que ou tu veux les aurevoirs"), status: bool = nextcord.SlashOption(name="status", description="Activer ou non?")):
    if status is None or status is False:
      delete({"_id": interaction.guild.id}, 'bye')
      await interaction.response.send_message("Le système de bienvenue n'est plus activé !")
      return  
    add({"_id": interaction.guild.id, "id": channel.id}, 'bye')
    await interaction.response.send_message("Le système de aurevoir est activé !")
    await interaction.channel.send("Test en cours d'envoie !")
    await self.bot.get_channel(channel.id).send(embed=nextcord.Embed(title='Aurevoir test !', description=f"J'espère que tu as passer un bon momment sur {interaction.guild.name} !", color=0x2ecc71))
    
  @commands.Cog.listener("on_member_leave")
  async def Leave_systeme(self, member):
    data = search(member.guild.id, 'bye')
    if data is None: return
    await self.bot.get_channel(data['id']).send(embed=nextcord.Embed(title=f"Aurevoir {member.name} !", description=f"J'espère que tu as passer un bon momment sur {member.guild.name} !", color=0x2ecc71))

def setup(bot):
  bot.add_cog(Bye(bot))
