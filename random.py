#DISCORD
import discord
from discord.ext import commands

#RANDOM
import random
from random import randint

#COG SETUP
class plexi:
    def __init__(self, bot):
        self.bot = bot
    
    #COMMAND
    @commands.command()
    async def random(self, ctx, choice: str = None, num1: int = None, num2: int = None):
      try:
        if choice == 'below':
          random_choice = random.randint(0, num1)
          embed = discord.Embed(
              colour = discord.Colour.blurple()
          )
          embed.set_author(name='RANDOM')
          embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/478598485172813832/488303039074140180/image0.gif')
          embed.add_field(name=f'Choice -> `{choice}`', value='** **', inline=False)
          embed.add_field(name=f'Input -> `{num1}`', value='** **', inline=False)
          embed.add_field(name=f'Random number -> `{random_choice}`', value='** **', inline=False)
          embed.set_footer(text=f'For {ctx.author.name}', icon_url=ctx.author.avatar_url)
          await ctx.send(embed=embed)
        elif choice == "above":
          abo = (num1+999999999)
          random_choice = random.randint(num1, abo)
          eabove = discord.Embed(
              colour = discord.Colour.blurple()
          )
          eabove.set_author(name='RANDOM')
          eabove.set_thumbnail(url='https://cdn.discordapp.com/attachments/478598485172813832/488303039074140180/image0.gif')
          eabove.add_field(name=f'Choice -> `{choice}`', value='** **', inline=False)
          eabove.add_field(name=f'Input -> `{num1}`', value='** **', inline=False)
          eabove.add_field(name=f'Random number -> `{random_choice}`', value='** **', inline=False)
          eabove.set_footer(text=f'For {ctx.author.name}', icon_url=ctx.author.avatar_url)
          await ctx.send(embed=eabove)
        elif choice == "between":
            if num2 != None or num1 != None:
                if num1 < 0 or num2 < 0:
                    await ctx.send(':x: Please provide a posotive number')
                else:
                    if num1 < num2:
                      random_choice = random.randint(num1, num2)
                      ebetween = discord.Embed(
                          colour = discord.Colour.blurple()
                      )
                      ebetween.set_author(name='RANDOM')
                      ebetween.set_thumbnail(url='https://cdn.discordapp.com/attachments/478598485172813832/488303039074140180/image0.gif')
                      ebetween.add_field(name=f'Choice -> `{choice}`', value='** **', inline=False)
                      ebetween.add_field(name=f'Input -> `{num1}`, `{num2}`', value='** **', inline=False)
                      ebetween.add_field(name=f'Random number -> `{random_choice}`', value='** **', inline=False)
                      ebetween.set_footer(text=f'For {ctx.author.name}', icon_url=ctx.author.avatar_url)
                      await ctx.send(embed=ebetween)
                    
                    else:
                      random_choice = random.randint(num2, num1)
                      ebetween_swap = discord.Embed(
                          colour = discord.Colour.blurple()
                      )
                      ebetween_swap.set_author(name='RANDOM')
                      ebetween_swap.set_thumbnail(url='https://cdn.discordapp.com/attachments/478598485172813832/488303039074140180/image0.gif')
                      ebetween_swap.add_field(name=f'Choice -> `{choice}`', value='** **', inline=False)
                      ebetween_swap.add_field(name=f'Input -> `{num1}`, `{num2}`', value='** **', inline=False)
                      ebetween_swap.add_field(name=f'Random number -> `{random_choice}`', value='** **', inline=False)
                      ebetween_swap.set_footer(text=f'For {ctx.author.name}', icon_url=ctx.author.avatar_url)
                      await ctx.send(embed=ebetween_swap)
          else:
            await ctx.send(':x: Need 2 numbers!')
        elif choice == "float":
          random_choice1 = random.randint(0, 10000)
          random_choice2 = random.randint(0, 1000)
          efloat = discord.Embed(
              colour = discord.Colour.blurple()
          )
          efloat.set_author(name='RANDOM')
          efloat.set_thumbnail(url='https://cdn.discordapp.com/attachments/478598485172813832/488303039074140180/image0.gif')
          efloat.add_field(name=f'Choice -> `{choice}`', value='** **', inline=False)
          efloat.add_field(name=f'Input -> `not needed`', value='** **', inline=False)
          efloat.add_field(name=f'Random number -> `{random_choice1}.{random_choice2}`', value='** **', inline=False)
          efloat.set_footer(text=f'For {ctx.author.name}', icon_url=ctx.author.avatar_url)
          await ctx.send(embed=efloat)
        elif choice == 'negative':
          ran_choice = random.randint(0, 100000)
          random_choice = f"-{ran_choice}"
          enegative = discord.Embed(
              colour = discord.Colour.blurple()
          )
          enegative.set_author(name='RANDOM')
          enegative.set_thumbnail(url='https://cdn.discordapp.com/attachments/478598485172813832/488303039074140180/image0.gif')
          enegative.add_field(name=f'Choice -> `{choice}`', value='** **', inline=False)
          enegative.add_field(name=f'Input -> `not needed`', value='** **', inline=False)
          enegative.add_field(name=f'Random number -> `{random_choice}`', value='** **', inline=False)
          enegative.set_footer(text=f'For {ctx.author.name}', icon_url=ctx.author.avatar_url)
          await ctx.send(embed=enegative)
        elif choice == None:
          eusage = discord.Embed(
              colour = discord.Colour.blurple()
          )
          eusage.set_author(name='Random')
          eusage.set_thumbnail(url='https://cdn.discordapp.com/attachments/478598485172813832/488303039074140180/image0.gif')
          eusage.add_field(name='Choice -> `none`', value='Displaying usage.', inline=False)
          eusage.add_field(name='List of choices:', value='`above`, `below`, `between`, `float`, `negative`', inline=False)
          eusage.add_field(name='Examples:', value='`ffrandom above 10`, `ffrandom below 10`, `ffrandom between 10 20`, `ffrandom float`, `ffrandom negative`', inline=False)
          await ctx.send(embed=eusage)
        else:
          await ctx.send(':x: I do not understand that choice. Say `ffrandom` for a list!')
      except Exception as e:
        await ctx.send(e)
          
def setup(bot):
    bot.add_cog(plexi(bot))
