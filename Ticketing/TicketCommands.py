from disnake.ext.commands.cog import _cog_special_method

from CustomClasses.CustomBot import CustomClient
from disnake.ext import commands
from coc import utils
import coc
import disnake
import asyncio
from datetime import datetime
import pytz
tiz = pytz.utc
from Ticketing import TicketUtils as ticket_utils

class TicketCommands(commands.Cog):

    def __init__(self, bot: CustomClient):
        self.bot = bot

    @commands.slash_command(name="ticket")
    async def ticket(self, ctx: disnake.ApplicationCommandInteraction):
        pass

    @ticket.sub_command(name="panel")
    async def ticket_panel(self, ctx: disnake.ApplicationCommandInteraction):
        await ctx.response.defer(ephemeral=False)
        embed_json = await ticket_utils.get_embed_json(bot=self.bot,ctx=ctx)
        await ticket_utils.parse_embed_json(json=embed_json, ctx=ctx)
        #await ctx.send()



    async def cog_slash_command_error(self, inter: disnake.ApplicationCommandInteraction, error: Exception):
        print(error)
