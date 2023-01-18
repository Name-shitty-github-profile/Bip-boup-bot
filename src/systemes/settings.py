from nextcord.ext import commands
import nextcord
from database import search
from utils import checkperm
data = {
  'join': "bienvenu(e)",
  'bye': 'aurevoir',
  'antibot': 'antibot'
}
class Settings(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "settings", description = "Te montre les paramêtres du bot.")
  async def Settings_slash(self, interaction: nextcord.Interaction):
    if not checkperm(interaction.user, ['admin']):
      await interaction.response.send_message("Tu ne peux pas faire cela !", ephemeral=True)
      return
    embed = nextcord.Embed(title=f'Paramêtres de {interaction.guild.name}', color=0x3498db)
    for i, j in data.items():
      embed.add_field(name=f"Système de {j}", value='✅ Actif' if search(interaction.guild.id, i) else '❌ Inatif')
    await interaction.response.send_message(embed=embed)

def setup(bot):
  bot.add_cog(Settings(bot))
