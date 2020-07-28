import urllib.request
import json

pets = [
    "RABBIT", "CHICKEN", "BEE", "ELEPHANT",
    "PIG",
    "SHEEP", "PARROT", "JELLYFISH",
    "GUARDIAN", "WOLF", "ENDERMAN", "PIGMAN",
    "BLAZE", "HORSE", "JERRY", "PHOENIX",
    "MAGMA_CUBE", "TIGER", "SNOWMAN", "TURTLE",
    "ENDER_DRAGON", "SPIDER", "GHOUL", "SKELETON",
    "ZOMBIE", "GOLEM", "HOUND", "TARANTULA",
    "BLACK_CAT", "SKELETON_HORSE",
    "MONKEY", "OCELOT", "LION", "GIRAFFE"
    "ENDERMITE", "SILVERFISH", "ROCK", "BAT",
    "WITHER_SKELETON",
    "SQUID", "FLYING_FISH", "BLUE_WHALE", "DOLPHIN",
    "BABY_YETI",
]


def get_info():

    with open("ign.txt", "r")as f:
        ign = f.read()
    with open("profile_name.txt", "r")as f:
        cute_name = f.read()
    with open("api_key.txt", "r")as f:
        api_key = f.read()
    with open("pet.txt", "r")as f:
        pet_to_track = f.read()

    return ign, cute_name, api_key, pet_to_track


def get_uuid(ign):
    uuid_link = "https://api.mojang.com/users/profiles/minecraft/"

    resp = urllib.request.urlopen(uuid_link + ign)
    data = resp.read()
    decoded = json.loads(data.decode(resp.info().get_content_charset('utf-8')))
    uuid = decoded["id"]

    return uuid


def main():
    ign, cute_name, api_key, pet_to_track = get_info()
    uuid = get_uuid(ign)

    api_link = """https://api.hypixel.net/skyblock/profiles\
?key={}&uuid=""".format(api_key)

    resp = urllib.request.urlopen(api_link + uuid)
    data = resp.read()
    data2 = json.loads(data.decode(resp.info().get_content_charset('utf-8')))
    profiles = data2["profiles"]

    if len(profiles) == 1:
        profile = profiles[0]
        profile_data = profile["members"][uuid]

    for profile in profiles:
        if cute_name in profile.values():
            profile_data = profile["members"][uuid]

    pet_data = profile_data["pets"]
    for indiv_pet in pet_data:
        pet = indiv_pet["type"]
        if pet == pet_to_track:
            print("{}: {} EXP".format(pet.lower().title(), indiv_pet["exp"]))

    return


while __name__ == "__main__":
    s = input("\n\nEnter '0' when you want to track pet xp: ")
    if s == "0":
        main()
