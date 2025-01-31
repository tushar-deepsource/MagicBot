import coc

from Assets.emojiDictionary import emojiDictionary
from Assets.levelEmojis import levelEmojis, maxLevelEmojis
from collections import defaultdict
from utils.discord_utils import fetch_emoji
from utils.constants import DARK_ELIXIR, SUPER_TROOPS

async def superTroops(player, asArray=False):
    troops = player.troop_cls
    troops = player.troops

    boostedTroops = []

    for x in range(len(troops)):
        troop = troops[x]
        if (troop.is_active):
            # print (troop.name)
            boostedTroops.append(troop.name)

    if asArray:
        return boostedTroops

    return str(boostedTroops)


def heros(bot, player: coc.Player):
    def get_emoji(hero: coc.Hero):
        color = "blue"
        if hero.level == hero.get_max_level_for_townhall(townhall=player.town_hall):
            color = "gold"
        return bot.get_number_emoji(color=color, number=hero.level)

    hero_string = [f"{emojiDictionary(hero.name)}{get_emoji(hero)}" for hero in player.heroes if hero.is_home_base]

    if not hero_string:
        return None

    return "".join(hero_string)


def spells(player, bot=None):
    spells = player.spell_cls
    spells = player.spells
    if (spells == []):
        return None
    spellList = ""
    levelList = ""

    for x in range(len(spells)):
        theSpells = coc.SPELL_ORDER
        # print(str(regTroop))
        spell = spells[x]
        if spell.name in theSpells:
            if (spell.name == "Poison Spell"):
                spellList += "\n" + levelList + "\n"
                levelList = ""
            spellList += f"{emojiDictionary(spell.name)} "
            if spell.level == spell.max_level:
                levelList += maxLevelEmojis(spell.level)
            else:
                levelList += levelEmojis(spell.level)
            if spell.level <= 10:
                levelList += " "

    spellList += "\n" + levelList + "\n"

    # print(heroList)
    # print(troopList)
    return spellList


def troops(player, bot=None):
    troops = player.troop_cls
    troops = player.troops
    if (troops == []):
        return None
    troopList = ""
    levelList = ""

    z = 0
    for x in range(len(troops)):
        troop = troops[x]
        if (troop.name not in DARK_ELIXIR) and (troop.is_home_base) and (troop.name not in coc.SIEGE_MACHINE_ORDER) and (troop.name not in SUPER_TROOPS):
            z += 1
            troopList += emojiDictionary(troop.name) + " "
            if troop.level == troop.max_level:
                levelList += maxLevelEmojis(troop.level)
            else:
                levelList += levelEmojis(troop.level)
            if troop.level <= 11:
                levelList += " "

            if (z != 0 and z % 6 == 0):
                troopList += "\n" + levelList + "\n"
                levelList = ""

    troopList += "\n" + levelList + "\n"

    return troopList


def deTroops(player, bot=None):
    troops = player.troop_cls
    troops = player.troops
    if (troops == []):
        return None
    troopList = ""
    levelList = ""

    z = 0
    notDe = False
    for x in range(len(troops)):
        regTroop = coc.HOME_TROOP_ORDER
        troop = troops[x]
        if (notDe == False) and (troop.name in DARK_ELIXIR) and (troop.is_home_base) and (troop.name not in coc.SIEGE_MACHINE_ORDER):
            z += 1
            troopList += emojiDictionary(troop.name) + " "
            if troop.level == troop.max_level:
                levelList += maxLevelEmojis(troop.level)
            else:
                levelList += levelEmojis(troop.level)

            if troop.level <= 11:
                levelList += " "
            # print(str(z))
            if (z >= 0 and z % 5 == 0):
                troopList += "\n" + levelList + "\n"
                levelList = ""

    troopList += "\n" + levelList + "\n"

    return troopList


def siegeMachines(player, bot=None):
    sieges = player.troop_cls
    sieges = player.siege_machines
    if (sieges == []):
        return None
    siegeList = ""
    levelList = ""

    z = 0
    for x in range(len(sieges)):
        siegeL = coc.SIEGE_MACHINE_ORDER
        # print(str(regTroop))
        siege = sieges[x]
        if siege.name in siegeL:
            z += 1
            siegeList += emojiDictionary(siege.name) + " "
            if siege.level == siege.max_level:
                levelList += maxLevelEmojis(siege.level)
            else:
                levelList += levelEmojis(siege.level)

            if siege.level <= 10:
                levelList += " "

    siegeList += "\n" + levelList

    # print(heroList)
    # print(troopList)
    return siegeList


def heroPets(bot,player: coc.Player):
    if not player.pets:
        return None

    def get_emoji(pet: coc.Pet):
        color = "blue"
        if pet.level == pet.max_level:
            color = "gold"
        return bot.get_number_emoji(color=color, number=pet.level)

    pet_string = ""
    for count, pet in enumerate(player.pets):
        pet_string += f"{emojiDictionary(pet.name)}{get_emoji(pet)}"
        if count == 3:
            pet_string += "\n"

    return pet_string


def profileSuperTroops(player):
    troops = player.troops
    boostedTroops = ""

    for x in range(len(troops)):
        troop = troops[x]
        if troop.is_active:
            emoji = emojiDictionary(troop.name)
            boostedTroops += f"{emoji} {troop.name}" + "\n"

    if (len(boostedTroops) > 0):
        boostedTroops = f"\n**Super Troops:**\n{boostedTroops}"
    else:
        boostedTroops = ""
    return boostedTroops


def clan_th_comp(clan_members):
    thcount = defaultdict(int)

    for player in clan_members:
        thcount[player.town_hall] += 1

    th_comp_string = ""
    for th_level, th_count in sorted(thcount.items(), reverse=True):
        th_emoji = fetch_emoji(th_level)
        th_comp_string += f"{th_emoji}`{th_count}` "

    return th_comp_string


def clan_super_troop_comp(clan_members):
    super_troop_comp_dict = defaultdict(int)
    for player in clan_members:
        for troop in player.troops:
            if troop.is_active:
                super_troop_comp_dict[troop.name] += 1

    return_string = ""
    for troop, count in super_troop_comp_dict.items():
        super_troop_emoji = fetch_emoji(emoji_name=troop)
        return_string += f"{super_troop_emoji}`x{count} `"

    if return_string == "":
        return_string = "None"

    return return_string


def leagueAndTrophies(player):
    emoji = ""
    league = str(player.league)
    # print(league)

    if (league == "Bronze League III"):
        emoji = "<:BronzeLeagueIII:601611929311510528>"
    elif (league == "Bronze League II"):
        emoji = "<:BronzeLeagueII:601611942850986014>"
    elif (league == "Bronze League I"):
        emoji = "<:BronzeLeagueI:601611950228635648>"
    elif (league == "Silver League III"):
        emoji = "<:SilverLeagueIII:601611958067920906>"
    elif (league == "Silver League II"):
        emoji = "<:SilverLeagueII:601611965550428160>"
    elif (league == "Silver League I"):
        emoji = "<:SilverLeagueI:601611974849331222>"
    elif (league == "Gold League III"):
        emoji = "<:GoldLeagueIII:601611988992262144>"
    elif (league == "Gold League II"):
        emoji = "<:GoldLeagueII:601611996290613249>"
    elif (league == "Gold League I"):
        emoji = "<:GoldLeagueI:601612010492526592>"
    elif (league == "Crystal League III"):
        emoji = "<:CrystalLeagueIII:601612021472952330>"
    elif (league == "Crystal League II"):
        emoji = "<:CrystalLeagueII:601612033976434698>"
    elif (league == "Crystal League I"):
        emoji = "<:CrystalLeagueI:601612045359775746>"
    elif (league == "Master League III"):
        emoji = "<:MasterLeagueIII:601612064913621002>"
    elif (league == "Master League II"):
        emoji = "<:MasterLeagueII:601612075474616399>"
    elif (league == "Master League I"):
        emoji = "<:MasterLeagueI:601612085327036436>"
    elif (league == "Champion League III"):
        emoji = "<:ChampionLeagueIII:601612099226959892>"
    elif (league == "Champion League II"):
        emoji = "<:ChampionLeagueII:601612113345249290>"
    elif (league == "Champion League I"):
        emoji = "<:ChampionLeagueI:601612124447440912>"
    elif (league == "Titan League III"):
        emoji = "<:TitanLeagueIII:601612137491726374>"
    elif (league == "Titan League II"):
        emoji = "<:TitanLeagueII:601612148325744640>"
    elif (league == "Titan League I"):
        emoji = "<:TitanLeagueI:601612159327141888>"
    elif (league == "Legend League"):
        emoji = "<:LegendLeague:601612163169255436>"
    else:
        emoji = "<:Unranked:601618883853680653>"

    return emoji + str(player.trophies)


def league_emoji(player):
    league = str(player.league)

    if league == "Bronze League I":
        return "<:BronzeLeagueI:601611950228635648>"
    elif league == "Bronze League II":
        return "<:BronzeLeagueII:601611942850986014>"
    elif league == "Bronze League III":
        return "<:BronzeLeagueIII:601611929311510528>"
    elif league == "Champion League I":
        return "<:ChampionLeagueI:601612124447440912>"
    elif league == "Champion League II":
        return "<:ChampionLeagueII:601612113345249290>"
    elif league == "Champion League III":
        return "<:ChampionLeagueIII:601612099226959892>"
    elif league == "Crystal League I":
        return "<:CrystalLeagueI:601612045359775746>"
    elif league == "Crystal League II":
        return "<:CrystalLeagueII:601612033976434698>"
    elif league == "Crystal League III":
        return "<:CrystalLeagueIII:601612021472952330>"
    elif league == "Gold League I":
        return "<:GoldLeagueI:601612010492526592>"
    elif league == "Gold League II":
        return "<:GoldLeagueII:601611996290613249>"
    elif league == "Gold League III":
        return "<:GoldLeagueIII:601611988992262144>"
    elif league == "Legend League":
        return "<:LegendLeague:601612163169255436>"
    elif league == "Master League I":
        return "<:MasterLeagueI:601612085327036436>"
    elif league == "Master League II":
        return "<:MasterLeagueII:601612075474616399>"
    elif league == "Master League III":
        return "<:MasterLeagueIII:601612064913621002>"
    elif league == "Silver League I":
        return "<:SilverLeagueI:601611974849331222>"
    elif league == "Silver League II":
        return "<:SilverLeagueII:601611965550428160>"
    elif league == "Silver League III":
        return "<:SilverLeagueIII:601611958067920906>"
    elif league == "Titan League I":
        return "<:TitanLeagueI:601612159327141888>"
    elif league == "Titan League II":
        return "<:TitanLeagueII:601612148325744640>"
    elif league == "Titan League III":
        return "<:TitanLeagueIII:601612137491726374>"
    else:
        return "<:Unranked:601618883853680653>"


def league_to_emoji(league: str):

    if league == "Bronze League I":
        return "<:BronzeLeagueI:601611950228635648>"
    elif league == "Bronze League II":
        return "<:BronzeLeagueII:601611942850986014>"
    elif league == "Bronze League III":
        return "<:BronzeLeagueIII:601611929311510528>"
    elif league == "Champion League I":
        return "<:ChampionLeagueI:601612124447440912>"
    elif league == "Champion League II":
        return "<:ChampionLeagueII:601612113345249290>"
    elif league == "Champion League III":
        return "<:ChampionLeagueIII:601612099226959892>"
    elif league == "Crystal League I":
        return "<:CrystalLeagueI:601612045359775746>"
    elif league == "Crystal League II":
        return "<:CrystalLeagueII:601612033976434698>"
    elif league == "Crystal League III":
        return "<:CrystalLeagueIII:601612021472952330>"
    elif league == "Gold League I":
        return "<:GoldLeagueI:601612010492526592>"
    elif league == "Gold League II":
        return "<:GoldLeagueII:601611996290613249>"
    elif league == "Gold League III":
        return "<:GoldLeagueIII:601611988992262144>"
    elif league == "Legend League":
        return "<:LegendLeague:601612163169255436>"
    elif league == "Master League I":
        return "<:MasterLeagueI:601612085327036436>"
    elif league == "Master League II":
        return "<:MasterLeagueII:601612075474616399>"
    elif league == "Master League III":
        return "<:MasterLeagueIII:601612064913621002>"
    elif league == "Silver League I":
        return "<:SilverLeagueI:601611974849331222>"
    elif league == "Silver League II":
        return "<:SilverLeagueII:601611965550428160>"
    elif league == "Silver League III":
        return "<:SilverLeagueIII:601611958067920906>"
    elif league == "Titan League I":
        return "<:TitanLeagueI:601612159327141888>"
    elif league == "Titan League II":
        return "<:TitanLeagueII:601612148325744640>"
    elif league == "Titan League III":
        return "<:TitanLeagueIII:601612137491726374>"
    elif "Wood" in league:
        return "<:wood_league:1109716152709566524>"
    elif "Clay" in league:
        return "<:clay_league:1109716160561291274>"
    elif "Stone" in league:
        return "<:stone_league:1109716159126843403>"
    elif "Copper" in league:
        return "<:copper_league:1109716157440720966>"
    elif "Brass" in league:
        return "<:brass_league:1109716155876249620>"
    elif "Iron" in league:
        return "<:iron_league:1109716154257264670>"
    elif "Steel" in league:
        return "<:steel_league:1109716168375279616>"
    elif "Titanium" in league:
        return "<:titanium_league:1109716170208198686>"
    elif "Platinum" in league:
        return "<:platinum_league:1109716172330512384>"
    elif "Emerald" in league:
        return "<:emerald_league:1109716179121094707>"
    elif "Ruby" in league:
        return "<:ruby_league:1109716183269265501>"
    elif "Diamond" in league:
        return "<:diamond_league:1109716180983369768>"
    else:
        return "<:Unranked:601618883853680653>"


def cwl_league_emojis(league):

    if (league == "Bronze League III"):
        emoji = "<:BronzeLeagueIII:601611929311510528>"
    elif (league == "Bronze League II"):
        emoji = "<:BronzeLeagueII:601611942850986014>"
    elif (league == "Bronze League I"):
        emoji = "<:BronzeLeagueI:601611950228635648>"
    elif (league == "Silver League III"):
        emoji = "<:SilverLeagueIII:601611958067920906>"
    elif (league == "Silver League II"):
        emoji = "<:SilverLeagueII:601611965550428160>"
    elif (league == "Silver League I"):
        emoji = "<:SilverLeagueI:601611974849331222>"
    elif (league == "Gold League III"):
        emoji = "<:GoldLeagueIII:601611988992262144>"
    elif (league == "Gold League II"):
        emoji = "<:GoldLeagueII:601611996290613249>"
    elif (league == "Gold League I"):
        emoji = "<:GoldLeagueI:601612010492526592>"
    elif (league == "Crystal League III"):
        emoji = "<:CrystalLeagueIII:601612021472952330>"
    elif (league == "Crystal League II"):
        emoji = "<:CrystalLeagueII:601612033976434698>"
    elif (league == "Crystal League I"):
        emoji = "<:CrystalLeagueI:601612045359775746>"
    elif (league == "Master League III"):
        emoji = "<:MasterLeagueIII:601612064913621002>"
    elif (league == "Master League II"):
        emoji = "<:MasterLeagueII:601612075474616399>"
    elif (league == "Master League I"):
        emoji = "<:MasterLeagueI:601612085327036436>"
    elif (league == "Champion League III"):
        emoji = "<:ChampionLeagueIII:601612099226959892>"
    elif (league == "Champion League II"):
        emoji = "<:ChampionLeagueII:601612113345249290>"
    elif (league == "Champion League I"):
        emoji = "<:ChampionLeagueI:601612124447440912>"
    elif (league == "Titan League III"):
        emoji = "<:TitanLeagueIII:601612137491726374>"
    elif (league == "Titan League II"):
        emoji = "<:TitanLeagueII:601612148325744640>"
    elif (league == "Titan League I"):
        emoji = "<:TitanLeagueI:601612159327141888>"
    elif (league == "Legend League"):
        emoji = "<:LegendLeague:601612163169255436>"
    else:
        emoji = "<:Unranked:601618883853680653>"

    return emoji







