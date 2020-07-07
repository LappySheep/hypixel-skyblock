__credits__ = ["lejittt", "mat / py5"]


import urllib.request
import json
import sys

from init_srw import init_srw

from get_uuid import get_uuid
from get_exp import get_exp
from get_levels import get_levels
from get_levels import skill_exp_table
from get_profiles import get_profiles
from get_profile_count import get_profile_count
from get_banking import get_banking
from manual import manual_calc
from get_nbt import get_nbt

from calcs.calc_skills import calc_skills
from calcs.calc_slayers import calc_slayers
from calcs.calc_minions import calc_minions
from calcs.calc_pets import calc_pets
from calcs.calc_money import calc_money
from calcs.calc_collections import calc_collections
from calcs.calc_nw import calc_nw

from calcs import skill_exp_table

srw_init = False


"""
To-do List:
    - Net Worth (finish)

Minor To-do List:
    - Finish testing armor
    - Add purse to bank if API on.
"""
            



def main(srw):
    custom = input("Custom Values? (0 if yes): ")
    if custom != "0":
        ign = input("Enter IGN: ").strip()
        if ign == "":
            print("No IGN entered.")
            return
        try:
            uuid = get_uuid(ign)
        except json.decoder.JSONDecodeError:
            # IGN does not exist.
            print("Invalid IGN.\n")
            return
        try:
            profile_count = get_profile_count(uuid)
        except TypeError:
            print("This player doesn't appear to have played SkyBlock!\n")
            return
        if profile_count == 1:
            profile_data, cute_name = get_profiles(uuid, None, True)
        else:
            cute_name = input("\nEnter Cute Name: ").strip()
            if cute_name == "":print("No Cute Name entered.")
            try:
                profile_data, cute_name = get_profiles(uuid, cute_name, False)
            except TypeError:
                print("Invalid Cute Name.\n")
                return
        exp = get_exp(profile_data)
        if exp == "NoAPI":
            print("API is not turned on.")
            return
        stat_set = get_levels(exp)
    else:
        stat_set = manual_calc()
        exp = [(skill_exp_table[stat])if index < 8else (stat)for index,stat in enumerate(stat_set)]
        ign,cute_name = "",""
    farm, tame, alch, ench, comb, fora, mine, fish, zombie, spider, wolf = stat_set
    skill_rating, skill_over, sAvg = calc_skills(stat_set, srw, exp)
    slayer_rating, total_slayers = calc_slayers(*stat_set[8:]) # * unpacks list
    if custom == "0":
        crafted_minions = input("Copy-paste minion JSON (empty for none): ")
        if crafted_minions != "":
            minion_rating = calc_minions(crafted_minions)
        else:
            minion_rating = 0
    else:
        try:
            crafted_minions = profile_data["crafted_generators"]
            minion_rating = calc_minions(crafted_minions)
        except KeyError:
            minion_rating = 0
    if custom == "0":
        pet_rating = 0 # todo?
    else:
        try:
            pet_data = profile_data["pets"]
            pet_rating = calc_pets(pet_data)
        except KeyError:
            pet_rating = 0
    if custom == "0":
        try:
            money = int(input("Enter amount of coins: "))
            money_rating = calc_money(money)
        except ValueError:
            money_rating = 0
        bank_api = False
    else:
        result = get_banking(uuid, cute_name)
        if result == "NoAPI":
            bank,bank_api = 0,False
        else:
            bank = result["balance"]
            bank_api = True
        money_rating = calc_money(bank)
    if custom == "0":
        coll_rating = 0 # todo?
        coll_api = False
    else:
        try:
            coll_data = profile_data["collection"]
            coll_rating = calc_collections(coll_data)
            coll_api = True
        except KeyError:
            coll_rating,coll_api = 0,0
    if custom == "0":
        coll_rating,nw_rating,inv_api = 0,0
    else:
        items_list = get_nbt(profile_data)
        try:
            nw_rating = calc_nw(items_list)
            inv_api = True
        except TypeError:
            nw_rating = 0
            inv_api = False
    skill_total = skill_rating + skill_over
    total = sum([skill_total,slayer_rating,minion_rating,pet_rating,money_rating,coll_rating,nw_rating,])

    weight_passes,weight_stages = [10000, 6000, 2500, 1250, 600, 350, 100, 50, 0],["Please stop playing this game", "Far Endgame", "Endgame", "Late-End", "Late Game", "Mid-Late", "Mid Game", "Early Game", "Fresh"]
    for i in range(9):
        if total >= weight_passes[i]:
            weight_stage = weight_stages[i]
            break
    txt = """\n{} - {}\n\nSkills:\n\tFarming: {}\n\tTaming: {}\n\tAlchemy: {}\n\tEnchanting: {}\n\tCombat: {}\n\tForaging: {}\n\tMining: {}\n\tFishing: {}\n\tSkill Average: {}\n\t\tSkill Weight: {}\n\t\tOverflown Skill Weight: {}\n\t\t\t(Skill Total: {})\n\nSlayers:\n\tZombie Slayer: {}\n\tSpider Slayer: {}\n\tWolf Slayer: {}\n\tTotal Slayers: {}\n\t\tSlayer Weight: {}\n\nMinion Weight: {}\nPet Weight: {}\nBank Weight: {} (API: {})\nCollection Weight: {} (API: {})\n\nNet Worth Weight: {} (API: {})\n\nTotal Weight: {}\nStage: {}
""".format(ign, cute_name, farm, tame, alch, ench, comb, fora, mine, fish, sAvg, "%.3f"%(skill_rating), "%.3f"%(skill_over), "%.3f"%(skill_total), zombie, spider, wolf, total_slayers, "%.3f"%(slayer_rating), "%.3f"%(minion_rating), "%.3f"%(pet_rating), "%.3f"%(money_rating), ("ON"if bank_api else "OFF"), "%.3f"%(coll_rating), ("ON"if coll_api else "OFF"), "%.3f"%(nw_rating), ("ON"if inv_api else "OFF"), "%.3f"%(total), weight_stage)
    print(txt+"\n\n")
while __name__ == "__main__":
    if not srw_init:srw = init_srw()
    main(srw)
