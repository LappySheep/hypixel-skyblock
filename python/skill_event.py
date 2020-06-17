import urllib.request
import json
import sys

def get_api(link, api_get):
    resp = urllib.request.urlopen(link + api_get)
    data = resp.read()
    decoded = json.loads(data.decode(resp.info().get_content_charset('utf-8')))

    return decoded

def get_exp(prof_data): # just copied, cba to change
    # only joking, i changed it slightly - returns dict
    stats = prof_data

    # set to 0 if it doesn't exist
    skills = ["experience_skill_farming", "experience_skill_foraging", "experience_skill_fishing"]

    for skill in skills:
        if skill not in stats.keys():
            stats[skill] = 0

    farming_exp = stats["experience_skill_farming"]
    # taming_exp = stats["experience_skill_taming"]
    # alchemy_exp = stats["experience_skill_alchemy"]
    # enchanting_exp = stats["experience_skill_enchanting"]
    # combat_exp = stats["experience_skill_combat"]
    foraging_exp = stats["experience_skill_foraging"]
    # mining_exp = stats["experience_skill_mining"]
    fishing_exp = stats["experience_skill_fishing"]

    exp_temp = [farming_exp, foraging_exp, fishing_exp]

    n, exp = ["farming_exp", "foraging_exp", "fishing_exp"], {}

    for m in n:
        exp[m] = exp_temp[n.index(m)]

    return exp

def main():
    igns = []
    loop = True
    while loop:
        ign = input("Enter IGN (q to stop): ").strip()
        if ign == "":
            print("No IGN entered.")
            loop = True
        elif ign == "q":
            print("List of names: {}".format(igns))
            loop = False
        else:
            igns.append(ign)

    uuid_link = "https://api.mojang.com/users/profiles/minecraft/"
    players = {}

    for ign in igns:
        try:
            decoded = get_api(uuid_link, ign)
            uuid = decoded["id"]
            players[ign] = uuid
        except json.decoder.JSONDecodeError:
            print("{} is not a valid ign".format(ign))

    api_link = "https://api.hypixel.net/skyblock/profiles?key=[YOUR_API_KEY]&uuid="
    players_exp = {}

    for player in [*players.keys()]:
        try:
            decoded = get_api(api_link,players[player])
            profiles = decoded["profiles"]
            profile_count = len(profiles)
        except:
            # player has not played SkyBlock before and/or wiped.
            print("{} doesn't appear to have played SkyBlock!\n".format(player))
            continue

        singular = False
        if profile_count == 1:
            cute_name = None
            singular = True
        else:
            cute_name = input("\nEnter Cute Name of {}: ".format(player).strip())
            if cute_name == "":
                print("No Cute Name entered.")

        if singular:
            profile = profiles[0]
            stats = profile["members"][players[player]]
            cute_name = profile["cute_name"]

        for profile in profiles:
            if cute_name in profile.values():
                stats = profile["members"][players[player]]
        exp = get_exp(stats)
        players_exp[player] = exp

    for player in players_exp:
        print("{} - {} farming, {} foraging, {} fishing".format(
            player,
            *[(int(x))for x in [*players_exp[player].values()]]
        ))





while __name__ == "__main__":
    main()
