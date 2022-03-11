weights = {
  "zombie": {
    "tier1": {"REVENANT_FLESH": 10000},
    "tier2": {"REVENANT_FLESH": 10000, "FOUL_FLESH": 2000, "PESTILENCE_RUNE": 83, "UNDEAD_CATALYST": 250, "REVENANT_CATALYST": 125},
    "tier3": {"REVENANT_FLESH": 10000, "FOUL_FLESH": 2000, "PESTILENCE_RUNE": 83, "UNDEAD_CATALYST": 250, "SMITE_VI_BOOK": 50, "BEHEADED_HORROR": 10, "REVENANT_CATALYST": 125},
    "tier4": {"REVENANT_FLESH": 10000, "FOUL_FLESH": 2000, "PESTILENCE_RUNE": 833, "UNDEAD_CATALYST": 75, "SMITE_VI_BOOK": 100, "BEHEADED_HORROR": 20, "REVENANT_CATALYST": 125, "SNAKE_RUNE": 20, "SCYTHE_BLADE": 7},
    "tier5": {"REVENANT_FLESH": 10000, "FOUL_FLESH": 2000, "PESTILENCE_RUNE": 833, "UNDEAD_CATALYST": 250, "SMITE_VI_BOOK": 100, "BEHEADED_HORROR": 20, "REVENANT_CATALYST": 125, "SNAKE_RUNE": 20, "SCYTHE_BLADE": 15, "SHARD_OF_THE_SHREDDED": 8, "WARDEN_HEART": 2, "REVENANT_VISCERA": 2000, "SMITE_VII_BOOK": 7}
  },
  "spider": {
    "tier1": {"TARANTULA_WEB": 10000},
    "tier2": {"TARANTULA_WEB": 10000, "TOXIC_ARROW_POISON": 1800, "BITE_RUNE": 83},
    "tier3": {"TARANTULA_WEB": 10000, "TOXIC_ARROW_POISON": 1800, "BITE_RUNE": 333, "SPIDER_CATALYST": 250, "BANE_OF_ARTHROPODS_VI_BOOK": 50, "FLY_SWATTER": 10, "TARANTULA_TALISMAN": 10},
    "tier4": {"TARANTULA_WEB": 10000, "TOXIC_ARROW_POISON": 1800, "BITE_RUNE": 833, "SPIDER_CATALYST": 75, "BANE_OF_ARTHROPODS_VI_BOOK": 100, "FLY_SWATTER": 20, "TARANTULA_TALISMAN": 20, "DIGESTED_MOSQUITO": 7}
  },
  "wolf": {
    "tier1": {"WOLF_TOOTH": 10000},
    "tier2": {"WOLF_TOOTH": 10000, "HAMSTER_WHEEL": 2000, "SPIRIT_RUNE": 83},
    "tier3": {"WOLF_TOOTH": 10000, "HAMSTER_WHEEL": 2000, "SPIRIT_RUNE": 333, "CRITICAL_VI_BOOK": 50, "RED_CLAW_EGG": 5},
    "tier4": {"WOLF_TOOTH": 10000, "HAMSTER_WHEEL": 2000, "SPIRIT_RUNE": 833, "CRITICAL_VI_BOOK": 100, "RED_CLAW_EGG": 15, "COUTURE_RUNE": 30, "OVERFLUX_CAPACITOR": 5, "GRIZZLY_BAIT": 7}
  },
  "enderman": {
    "tier1": {"NULL_SPHERE": 10000},
    "tier2": {"NULL_SPHERE": 10000, "TWILIGHT_ARROW_POISON": 1800, "SUMMONING_EYE": 80},
    "tier3": {"NULL_SPHERE": 10000, "TWILIGHT_ARROW_POISON": 1800, "ENDERSNAKE_RUNE": 333, "SUMMONING_EYE": 80, "MANA_STEAL_I_BOOK": 600, "TRANSMISSION_TUNER": 300, "NULL_ATOM": 500},
    "tier4": {"NULL_SPHERE": 10000, "TWILIGHT_ARROW_POISON": 1800, "ENDERSNAKE_RUNE": 800, "SUMMONING_EYE": 80, "MANA_STEAL_I_BOOK": 600, "TRANSMISSION_TUNER": 300, "NULL_ATOM": 700, "POCKET_ESPRESSO_MACHINE": 55, "SMARTY_PANTS_I_BOOK": 250, "END_RUNE": 100, "HANDY_BLOOD_CHALICE": 25, "SINFUL_DICE": 65, "EXCEEDINGLY_RARE_ENDER_ARTIFACT_UPGRADER": 4, "ENDERMAN_PET_SKIN": 25, "ETHERWARP_MERGER": 60, "JUDGEMENT_CORE": 8, "ENCHANT_RUNE": 7, "ENDER_SLAYER_VII_BOOK": 2}
  }
}



guaranteed = ["REVENANT_FLESH", "TARANTULA_WEB", "WOLF_TOOTH", "NULL_SPHERE"]

extra = ["PESTILENCE_RUNE", "SNAKE_RUNE", "BITE_RUNE", "SPIRIT_RUNE", "COUTURE_RUNE", "ENDERSNAKE_RUNE", "END_RUNE", "ENDERMAN_PET_SKIN", "ENCHANT_RUNE"]

non_mf = [*guaranteed, *extra, "TOXIC_ARROW_POISON", "FOUL_FLESH", "REVENANT_VISCERA", "HAMSTER_WHEEL", "TWILIGHT_ARROW_POISON"]

fancy1 = {"zombie": "Revenant Horror", "spider": "Tarantula Broodfather", "wolf": "Sven Packmaster", "enderman": "Voidgloom Seraph"}

fancy2 = {
  "REVENANT_FLESH": "Revenant Flesh", "FOUL_FLESH": "Foul Flesh", "PESTILENCE_RUNE": "Pestilence Rune", "UNDEAD_CATALYST": "Undead Catalyst", "SMITE_VI_BOOK": "Smite VI Book", "BEHEADED_HORROR": "Beheaded Horror", "REVENANT_CATALYST": "Revenant Catalyst", "SNAKE_RUNE": "Snake Rune", "SCYTHE_BLADE": "Scythe Blade", "SHARD_OF_THE_SHREDDED": "Shard of the Shredded", "WARDEN_HEART": "Warden Heart", "REVENANT_VISCERA": "Revenant Viscera", "SMITE_VII_BOOK": "Smite VII Book",
  "TARANTULA_WEB": "Tarantula Web", "TOXIC_ARROW_POISON": "Toxic Arrow Poison", "BITE_RUNE": "Bite Rune", "SPIDER_CATALYST": "Spider Catalyst", "BANE_OF_ARTHROPODS_VI_BOOK": "Bane Of Arthropods VI Book", "FLY_SWATTER": "Fly Swatter", "TARANTULA_TALISMAN": "Tarantula Talisman", "DIGESTED_MOSQUITO": "Digested Mosquito",
  "WOLF_TOOTH": "Wolf Tooth", "HAMSTER_WHEEL": "Hamster Wheel", "SPIRIT_RUNE": "Spirit Rune", "CRITICAL_VI_BOOK": "Critical VI Book", "RED_CLAW_EGG": "Red Claw Egg", "COUTURE_RUNE": "Couture Rune", "OVERFLUX_CAPACITOR": "Overflux Capacitor", "GRIZZLY_BAIT": "Grizzly Bait",
  "NULL_SPHERE": "Null Sphere", "TWILIGHT_ARROW_POISON": "Twilight Arrow Poison", "ENDERSNAKE_RUNE": "Endersnake Rune", "SUMMONING_EYE": "Summoning Eye", "MANA_STEAL_I_BOOK": "Mana Steal I Book", "TRANSMISSION_TUNER": "Transmission Tuner", "NULL_ATOM": "Null Atom", "POCKET_ESPRESSO_MACHINE": "Pocket Espresso Machine", "SMARTY_PANTS_I_BOOK": "Smarty Pants I Book", "END_RUNE": "End Rune", "HANDY_BLOOD_CHALICE": "Handy Blood Chalice", "SINFUL_DICE": "Sinful Dice", "EXCEEDINGLY_RARE_ENDER_ARTIFACT_UPGRADER": "Exceedingly Rare Ender Artifact Upgrader", "ENDERMAN_PET_SKIN": "Enderman Pet Skin", "ETHERWARP_MERGER": "Etherwarp Merger", "JUDGEMENT_CORE": "Judgement Core", "ENCHANT_RUNE": "Enchant Rune", "ENDER_SLAYER_VII_BOOK": "Ender Slayer VII Book"
}



def main(s):
  print(s)
  mf = input("Enter Magic Find\n> ")
  try:
    mf = int(mf)
  except:
    main("Invalid Magic Find.\n\n")

  slayer = input("\nEnter slayer type (zombie/spider/wolf/enderman)\n> ")
  if slayer not in weights.keys():
    main("Invalid slayer type.\n\n")
  tiers = weights[slayer]

  tier = input("\nEnter slayer boss tier (1-4, 1-5 if zombie)\n> ")
  try:
    drops = tiers[f"tier{tier}"]
  except:
    main("Invalid slayer boss tier.\n\n")

  new_weights = {}
  for drop in drops:
    if drop in non_mf:
      new_weights[drop] = drops[drop]
    else:
      new_weights[drop] = drops[drop] * (1 + (mf / 100))

  total = sum(new_weights.values())
  t_no_ex = total - sum([new_weights[x]for x in new_weights if x in extra])

  m = f"\nT{tier} {fancy1[slayer]} Drops{''if mf==0else f' (+{mf} Magic Find)'}\n"
  for drop in new_weights:
    if drop not in extra:
      if drop not in guaranteed:
        m += f"  {fancy2[drop]}: {round(100 * new_weights[drop] / t_no_ex, 6)}%\n"
      else:
        m += f"  {fancy2[drop]}: 100%\n"
    elif drop in extra:
      m += f"  {fancy2[drop]}: {round(100 * new_weights[drop] / (t_no_ex + new_weights[drop]), 6)}%\n"

  main(f"{m}\n\n")



while __name__ == "__main__":
  main("\n\n")
