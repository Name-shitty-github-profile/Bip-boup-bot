from nextcord.ext import commands
import nextcord
from utils import checkperm
from database import add, delete, search

class Join(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "bienvenue", description = "Activer le système de bienvenu sur le serveur")
  async def Join_slash(self, interaction: nextcord.Interaction, channel: nextcord.TextChannel = nextcord.SlashOption(name="salon", description="Le salon que ou tu veux les bienvenues"), status: bool = nextcord.SlashOption(name="status", description="Activer ou non?")):
    if not checkperm(interaction.user, ['admin']):
      await interaction.response.send_message("Tu ne peux pas faire cela !", ephemeral=True)
      return
    if status is None or status is False:
      delete({"_id": interaction.guild.id}, 'join')
      await interaction.response.send_message("Le système de bienvenue n'est plus activé !")
      return  
    add({"_id": interaction.guild.id, "id": channel.id}, 'join')
    await interaction.response.send_message("Le système de bienvenue est activé !")
    await interaction.channel.send("Test en cours d'envoie !")
    await self.bot.get_channel(channel.id).send(embed=nextcord.Embed(title='Bienvenu(e) test !', description=f"Passe un bon moment sur {interaction.guild.name} !", color=0x2ecc71))
    
  @commands.Cog.listener("on_member_join")
  async def Join_systeme(self, member):
    data = search(member.guild.id, 'join')
    if data is None:
      return
    await self.bot.get_channel(data['id']).send(embed=nextcord.Embed(title=f"Bienvenu(e) {member.name} !", description=f"Passe un bon moment sur {member.guild.name} !", color=0x2ecc71))

def setup(bot):
  bot.add_cog(Join(bot))
