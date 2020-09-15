import urllib.request
import json
import sys

global_api_key = ""


start = {
    # "IGN": [foraging, combat, fishing]
}


def get_uuid(ign):
    uuid_link = "https://api.mojang.com/users/profiles/minecraft/"
    resp = urllib.request.urlopen(uuid_link + ign)
    data = resp.read()
    decoded = json.loads(data.decode(resp.info().get_content_charset('utf-8')))
    uuid = decoded["id"]
    return uuid


def get_profiles(uuid, cute_name=None):
    api_link = f"https://api.hypixel.net/skyblock/profiles?key={global_api_key}&uuid="
    resp = urllib.request.urlopen(api_link + uuid)
    data = resp.read()
    data2 = json.loads(data.decode(resp.info().get_content_charset('utf-8')))
    profiles = data2["profiles"]
    singular = True if len(profiles) == 1 else False
    if singular:
        profile = profiles[0]
        stats = profile["members"][uuid]
        cute_name = profile["cute_name"]
        return stats, cute_name
    for profile in profiles:
        if cute_name in profile.values():
            stats = profile["members"][uuid]
    try:
        return stats, cute_name
    except NameError:
        # profile does not have a cute name
        return False


def get_exp(prof_data):
    stats = prof_data
    skills = ["experience_skill_combat", "experience_skill_foraging","experience_skill_fishing"]
    for skill in skills:
        if skill not in stats.keys():
            stats[skill] = 0
    combat_exp = stats["experience_skill_combat"]
    foraging_exp = stats["experience_skill_foraging"]
    fishing_exp = stats["experience_skill_fishing"]
    return foraging_exp, combat_exp, fishing_exp


def main():
    with open("players.txt")as f:
        newline_list = f.read()

    players = {}

    line_list = newline_list.splitlines()
    player_list = [(p.split(" "))for p in line_list]

    for p in player_list:
        if len(p) == 1:
            players[p[0]] = "None"
        elif len(p) == 2:
            players[p[0]] = p[1]

    msg = ""
    scores = {}
    for player in players.keys():
        cute = players[player]
        uuid = get_uuid(player)
        try:
            profile_data, cute = get_profiles(uuid, cute)
        except:
            print(f"{player} - error")
        try:
            fora, comb, fish = get_exp(profile_data)
        except:
            fora, comb, fish = 0,0,0
        fora, comb, fish = [(int(x))for x in (fora, comb, fish)]
        scores[player] = [fora + (comb * 1.5) + (fish * 5), [fora, comb, fish]]

    sort = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for p in sort:
        player, rating = p[0], p[1][0]
        fora,comb,fish = p[1][1]
        start_data = start[player]
        fr = fora - start_data[0]
        cm = comb - start_data[1]
        fs = fish - start_data[2]
        msg += f"{player} - {fr} Foraging XP + {cm} Combat XP + {fs} Fishing XP\n"

    print(msg)

main()
