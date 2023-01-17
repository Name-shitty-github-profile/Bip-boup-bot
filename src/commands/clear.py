import nextcord
from nextcord.ext import commands
from utils import checkperm
import asyncio

class Purge(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name='purge', description='Supprimer des messages')
  async def purge_slash(self,interaction: nextcord.Interaction, limit: int = nextcord.SlashOption(name="limite", description="La limite de messages")):
    if checkperm(interaction.user, ['manage']) is False:
      await interaction.response.send_message("Tu n'a pas les perms pour faire cela !", ephemeral=True)
      return
    await interaction.channel.purge(limit=limit)
    msg = await interaction.send(embed=nextcord.Embed(title="suppression de message", description=f"{limit} messages effacés par {interaction.user.mention}", color=0xFF0000))
    await asyncio.sleep(4)
    await msg.delete()

  @nextcord.slash_command(name='clear', description='Supprimer des messages')
  async def clear_slash(self,interaction: nextcord.Interaction, limit: int = nextcord.SlashOption(name="limite", description="La limite de messages")):
    if checkperm(interaction.user, ['manage']) is False:
      await interaction.response.send_message("Tu n'a pas les perms pour faire cela !", ephemeral=True)
      return
    await interaction.channel.purge(limit=limit)
    msg = await interaction.send(embed=nextcord.Embed(title="suppression de message", description=f"{limit} messages effacés par {interaction.user.mention}", color=0xFF0000))
    await asyncio.sleep(4)
    await msg.delete()


def setup(bot):
  bot.add_cog(Purge(bot))
