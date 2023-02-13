from nextcord.ext import commands
import nextcord
data = [
  {"Respect": "Veuillez respecter tout membres/éléments du serveur."},
  {"Copier": "Veuillez ne pas copier l'identitée d'un(e) membre du serveur."},
  {"Spam": "Veuillez ne pas spammer les messages dans tout les salons sauf ceux prévu a cette effet."},
  {"Pub": "Veuillez ne pas poster d'invitation dans les salons non fait pour cela et de ne pas envoyer cela en message privés au utilisateurs"}
]
class Rules(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name='règlement', description='Réglement déja tout fait avec une réaction')
  async def rules_slash(self, interaction: nextcord.Interaction):
    embed = nextcord.Embed(title="Règlement", description="merci de respecter le règlement et de cliquer sur la réaction.", color=0xe74c3c)
    for i, j in data.items():
      embed.add_field(name=i, value=j)
    await interaction.response.send_message(embed=embed)

def setup(bot):
  bot.add_cog(Rules(bot))
