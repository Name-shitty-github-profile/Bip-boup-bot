from nextcord.ext import commands
import nextcord
class Status(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener("on_ready")
  async def status(self):
    await self.bot.change_presence(activity=nextcord.Game(name="Comment puis-je vous aider?"))

def setup(bot):
  bot.add_cog(Status(bot))
