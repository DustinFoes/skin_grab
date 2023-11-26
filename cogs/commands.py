import asyncio
import traceback
import discord
from skins import *
from weapons import *
import json
from discord.ext import commands


# Load skins.json
with open('skins/skins.json', encoding="utf-8") as f:
    skin_list = json.load(f)
    # create a list of all the skin names
    skins_list = list(skin_list.values())



class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Create a command called "getskin" that takes a skin name or ID as an argument
    @discord.slash_command(name="getskin", description="Get a skin by name or ID")
    async def getskin(
        self,
        ctx,
        skin_id: discord.Option(str, description="Enter a skin ID", required=False, default=None),
        skin_name: discord.Option(str, description="Enter a skin name", required=False, default=None),
    ):
        print(type(skin_name))
        if skin_name is not None:
            # create an embed containing the skin name and ID
            embed = discord.Embed(title=getskin(skin_name), description=skin_name, color=0x00ff00)
            embed.set_footer(text="Skin Finder by DustinFoes")

            await ctx.respond(embed=embed)


        elif skin_id is not None:
            print(skin_id)
            # create an embed containing the skin name and ID
            embed = discord.Embed(title=f"Skin Name: {skin_id}", description=f"SkinID: {getskin(skin_id)}", color=0x00ff00)
            embed.set_footer(text="Skin Finder by DustinFoes")
            # send the embed
            await ctx.respond(embed=embed)

        else:
            await ctx.respond("This is awkward...\nIt appears you didn't enter a valid skin...")


def setup(bot):
    bot.add_cog(Commands(bot))