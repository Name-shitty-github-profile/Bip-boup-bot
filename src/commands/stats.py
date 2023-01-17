from nextcord.ext import commands
import nextcord

class Stats(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "stats", description = "Te montre les stats du bot.")
  async def Stats_slash(self, interaction: nextcord.Interaction):
    channel_count = user_count = 0
    for guild in self.bot.guilds:
      user_count += len(guild.members)
      channel_count += len(guild.channels)
    await interaction.response.send_message(embed=nextcord.Embed(title="Stats", description=f'Serveurs : {len(self.bot.guilds)}\nUtilisateurs : {user_count}\nSalons : {channel_count}', color=0x2ecc71))

def setup(bot):
  bot.add_cog(Stats(bot))
