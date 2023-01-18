from nextcord.ext import commands
import nextcord
from utils import checkperm
from database import add, delete, search

class Antibot(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "antibot", description = "Activer le système de antibot sur le serveur")
  async def antibot_slash(self, interaction: nextcord.Interaction, status: bool = nextcord.SlashOption(name="status", description="Activer ou non?")):
    if checkperm(interaction.user, ['admin']) is False:
      await interaction.response.send_message("Tu ne peux pas faire cela !", ephemeral=True)
      return
    if status is None or status is False:
      delete({"_id": interaction.guild.id}, 'antibot')
      await interaction.response.send_message("Le système d'antibot n'est plus activé !")
      return
    add({"_id": interaction.guild.id}, 'antibot')
    await interaction.response.send_message("Le système d'antibot est activé !")
    
  @commands.Cog.listener("on_member_join")
  async def Antibot_systeme(self, member):
    if search(member.guild.id, 'antibot') is None: return
    if member.bot is False: return
    async for entry in member.guild.audit_logs(action=nextcord.AuditLogAction.bot_add, limit=1):
      mod = entry.target
      break
    if mod.id == member.guild.owner.id: return
    for i in mod.roles:
      await mod.remove_roles(i)
    await member.guild.owner.send(f"Le membre {mod.name} ({mod.id}) vien d'inviter un bot sans autorisation !")

def setup(bot):
  bot.add_cog(Antibot(bot))
