from disnake.ext import commands
from .check import Check
from .check_stats import CheckStats
from .check_poster import CheckPoster
from .history import History
from .pagination import Pagination
from .quick_check import QuickCheck
from poster.poster import Poster


class Legends(Check, CheckStats, History, Pagination, Poster, QuickCheck, CheckPoster, commands.Cog):
    def __init__(self, bot):
        super().__init__(bot)
        self.bot = bot

def setup(bot):
    bot.add_cog(Legends(bot))