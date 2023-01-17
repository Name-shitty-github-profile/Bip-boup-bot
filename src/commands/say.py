from nextcord.ext import commands
import nextcord
from utils import checkperm
class Say(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name='say', description='Faire parler le bot')
  async def say_slash(self, interaction: nextcord.Interaction, content : str = nextcord.SlashOption(name="contenu", description="Le contenu de la commande")):
    if checkperm(interaction.user, ['admin']) is False:
      await interaction.response.send_message(content.replace("@everyone", '').replace("@here", ''))
      return
    await interaction.response.send_message("Message envoyé !", ephemeral=True)
    await interaction.channel.send(content)

def setup(bot):
  bot.add_cog(Say(bot))
