import nextcord
from nextcord.ext import commands
from utils import checkperm

class Ban(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "ban", description = "ban un membre")
  async def ban_slash(self, interaction: nextcord.Interaction, member: nextcord.User = nextcord.SlashOption(name="membre", description="Le membre à bannir"), reason: str = nextcord.SlashOption(name="raison", description="La raison du ban", required=False)):
    if not checkperm(interaction.user, ['ban']):
      await interaction.response.send_message("Tu ne peux pas faire cela !", ephemeral=True)
      return
    if reason is None:
      reason: str = f"L'utilisateur {member} ({member.id}) s'est fait bannir par {interaction.user.name}"
    else:
      reason: str = f"L'utilisateur {member} ({member.id}) s'est fait bannir par {interaction.user.name}, Pour : {reason}"
    if interaction.user.id == member.id:
      await interaction.response.send_message(content="Tu ne peux pas te bannir toi même !", ephemeral=True)
      return
    try:
      await member.ban(reason=reason)
    except:
      msg: str = f"Je n'ai pas pu bannir {member.name}.\nMalheureusement je n'ai pas assez de permission pour faire cela !"
      await interaction.response.send_message(content=msg, ephemeral=True)
      return
    await interaction.response.send_message(embed=nextcord.Embed(title=f"Ban de {member.name}", description=reason, color = 0xe74c3c))

def setup(bot):
  bot.add_cog(Ban(bot))
