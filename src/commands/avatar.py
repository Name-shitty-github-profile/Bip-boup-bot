from nextcord.ext import commands
import nextcord

class Avatar(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "avatar", description = "Montre l'avatar d'un membre")
  async def Avatar_slash(self, interaction: nextcord.Interaction, member: nextcord.User = nextcord.SlashOption(name="membre", description="La pp de la personne", required=False)):
    if member is False:
      member = interaction.user
    await interaction.response.send_message(embed=nextcord.Embed(title=f"Avatar de {member.name}", color=0x2ecc71).set_image(url = str(member.avatar.url)))

def setup(bot):
  bot.add_cog(Avatar(bot))
