from nextcord.ext import commands
import nextcord
from utils import checkperm
class AddRoles(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "addrole", description = "Ajoute un role a un membre.")
  async def addrole_slash(self, interaction: nextcord.Interaction, role : nextcord.Role = nextcord.SlashOption(name="role", description="Le role que tu veux ajouter au membre"), member: nextcord.Member = nextcord.SlashOption(name="membre", description="Le membre auquel tu veux ajouter le role")):
    if checkperm(interaction.user, ['admin']) is False:
      await interaction.response.send_message("Tu ne peux pas faire cela !", ephemeral=True)
      return
    try:
      await member.add_roles(role)
    except:
      await interaction.response.send_message("Je ne peux pas faire cela !", ephemeral=True)
    await interaction.response.send_message(f"Ajout du role {role.name} à {member.name}")

def setup(bot):
  bot.add_cog(AddRoles(bot))
