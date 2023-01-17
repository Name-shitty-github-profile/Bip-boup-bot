from nextcord.ext import commands
import nextcord

class Ping(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "ping", description = "Te montre le ping du bot.")
  async def Ping_slash(self, interaction: nextcord.Interaction):
    await interaction.response.send_message(embed=nextcord.Embed(title="Pong!", description=f'Ping : {round(self.bot.latency * 1000)} `ms`', color=0x2ecc71))

def setup(bot):
  bot.add_cog(Ping(bot))
