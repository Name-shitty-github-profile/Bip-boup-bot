from nextcord.ext import commands
import nextcord
from utils import checkperm
class Annonce(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "annonce", description = "Faire une annonce en utilisant le bot.")
  async def Annonce_slash(self, interaction: nextcord.Interaction, content : str = nextcord.SlashOption(name="contenu", description="Le contenu de la commande")):
    if checkperm(interaction.user, ['admin']) is False:
      await interaction.response.send_message("Tu ne peux pas faire cela !", ephemeral=True)
      return
    message = await interaction.channel.send(embed=nextcord.Embed(title="Annonce", description=f"{content}", color=0xf10404))
    await message.add_reaction('✅')
    message = await interaction.channel.send("@everyone")
    await message.delete()
    await interaction.response.send_message("Annonce envoyée !", ephemeral=True)

def setup(bot):
  bot.add_cog(Annonce(bot))
