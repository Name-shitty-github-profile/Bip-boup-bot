from nextcord.ext import commands
import nextcord
data = [
  'cc',
  'coucou',
  'salut',
  'slt',
  'bjr',
  'bonjour',
  'bon matin'
]
class Coucou(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "coucou", description = "Faire dire coucou au bot")
  async def Coucou_slash(self, interaction: nextcord.Interaction):
    await interaction.response.send_message("Coucou")

  @commands.Cog.listener("on_message")
  async def Salut(self, message):
    content = message.content.lower()
    if any(word in content for word in data):
      await message.add_reaction('👋')

def setup(bot):
  bot.add_cog(Coucou(bot))
