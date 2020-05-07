import urllib.request
import json

""" # can add this if you want - we do not have full list of values yet
rock = [2500, 7500, 20000]
dolphin = [250, 750, 2500]
"""

def main():
    api_key = input("Enter API key: ")
    username = input("Enter IGN: ")
    
    s = "https://api.hypixel.net/"

    api_link = "{2}player?key={0}&name={1}".format(api_key, username, s)

    resp = urllib.request.urlopen(api_link)
    data = resp.read()
    rB = json.loads(data.decode(resp.info().get_content_charset('utf-8')))
    
    profile_list = rB["player"]["stats"]["SkyBlock"]["profiles"]

    prof = {}
    for profile in profile_list:
        cn = profile_list[profile]["cute_name"]
        prof[cn] = profile

    cute_name = input("Enter the cute name of your profile (e.g. Pear): ")
    if cute_name not in prof.keys():
        print("Cute name/profile name not available.")
        return

    id = prof[cute_name]

    link2 = "{0}skyblock/profile?key={1}&profile={2}".format(s, api_key, id)

    resp2 = urllib.request.urlopen(link2)
    data2 = resp2.read()
    rC = json.loads(data2.decode(resp2.info().get_content_charset('utf-8')))

    stats = rC["profile"]["members"][id]["stats"]

    n1 = stats["pet_milestone_ores_mined"]
    n2 = stats["pet_milestone_sea_creatures_killed"]

    print("Mined ores: {0}\nSea Creatures Killed: {1}\n\n".format(n1,n2))



while __name__ == "__main__":
    main()
    
