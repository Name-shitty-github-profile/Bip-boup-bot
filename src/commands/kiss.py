from nextcord.ext import commands
import nextcord
import random
kisslist = [
  'https://media.tenor.com/images/924c9665eeb727e21a6e6a401e60183b/tenor.gif',
  'https://www.bing.com/images/search?view=detailV2&ccid=72GPJezI&id=3F12D3A5F00273F7BAF2A785DC48642059F88811&thid=OIP.72GPJezIzjW2QXADzWEFNQEsB-&mediaurl=https%3a%2f%2fdata.whicdn.com%2fimages%2f46937221%2foriginal.gif&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.ef618f25ecc8ce35b6417003cd610535%3frik%3dEYj4WSBkSNyFpw%26pid%3dImgRaw%26r%3d0&exph=210&expw=500&q=+gif+anime+kiss&simid=607996975068481444&FORM=IRPRST&ck=70A0C4A62E64F8DA0CDE8DB007A37475&selectedIndex=130&ajaxhist=0&ajaxserp=0',
  'https://th.bing.com/th/id/R.07324d30c494b00d3fbfe67bef50f99f?rik=MZES8Lr9PMvANA&pid=ImgRaw&r=0',
  'https://th.bing.com/th/id/R.4278241e44a1abc9506e85ee5920d20d?rik=%2bTX1XPyiSG9j6g&pid=ImgRaw&r=0',
  'https://gifimage.net/wp-content/uploads/2017/09/anime-kiss-gif-1.gif',
  'https://cdn.weeb.sh/images/H1a42auvb.gif',
  'https://cdn.weeb.sh/images/ByoCoT_vW.gif',
  'https://cdn.weeb.sh/images/HkZyXs3A-.gif',
  'https://cdn.weeb.sh/images/B1NwJg9Jz.gif',
  'https://cdn.weeb.sh/images/r1mcJlFVz.gif',
  'https://cdn.weeb.sh/images/B12LhT_Pb.gif',
  'https://cdn.weeb.sh/images/SJrBZrMBz.gif',
  'https://cdn.weeb.sh/images/HJmunTOw-.gif',
  'https://tenor.com/view/tonikaku-kawaii-tonikaku-kawaii-tonikawa-over-the-moon-for-you-gif-18959319',
  'https://tenor.com/view/kiss-tonikaku-kawaii-tonikawa-over-the-moon-for-you-tonikawa-tonikaku-gif-22051950'
]
class Kiss(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "kiss", description = "Embrasse une personne")
  async def Kiss_slash(self, interaction: nextcord.Interaction, member: nextcord.User = nextcord.SlashOption(name="membre", description="La personne que tu veux embrasser.")):
    if member.id == interaction.user.id:
      await interaction.response.send_message(embed=nextcord.Embed(title="Attend attend... 👀", description="comment tu veux faire pour te faire un bisou à toi même O_O?", color=0xf10404))
      return
    await interaction.response.send_message(embed=nextcord.Embed(title=f"{interaction.user.name} embrasse {member.name}", color=0xf10404).set_image(url=f'{random.choice(kisslist)}'))

def setup(bot):
  bot.add_cog(Kiss(bot))
