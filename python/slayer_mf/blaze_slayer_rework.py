__version__ = "1.2.3"


weights = {
 "blaze": {
  "tier1": {"DERELICT_ASHE": 10000},

  "tier2": {"DERELICT_ASHE": 10000, "WISPS_ICE_FLAVORED_SPLASH_POTION": 500, "BUNDLE_OF_MAGMA_ARROWS": 1500, "MANA_DISINTEGRATOR": 700, "SCORCHED_BOOKS": 400, "KELVIN_INVERTER": 250, "BLAZE_ROD_DISTILLATE": 900, "GLOWSTONE_DISTILLATE": 900, "MAGMA_CREAM_DISTILLATE": 900, "NETHER_WART_DISTILLATE": 900, "GABAGOOL_DISTILLATE": 500,
  "CINDERED_INVERTER": 250,
  "INFERNO_EDGE": 150
  },

  "tier3": {"DERELICT_ASHE": 10000, "LAVATEARS_RUNE": 200, "WISPS_ICE_FLAVORED_SPLASH_POTION": 500, "BUNDLE_OF_MAGMA_ARROWS": 1500, "MANA_DISINTEGRATOR": 700, "SCORCHED_BOOKS": 400, "KELVIN_INVERTER": 250, "BLAZE_ROD_DISTILLATE": 900, "GLOWSTONE_DISTILLATE": 900, "MAGMA_CREAM_DISTILLATE": 900, "NETHER_WART_DISTILLATE": 900, "GABAGOOL_DISTILLATE": 500, "SCORCHED_POWER_CRYSTAL": 600, "ARCHFIEND_DICE": 200,
  "CINDERED_INVERTER": 250,
  "INFERNO_EDGE": 300,
  "INFERNO_VERTEX": 50,
  "INFERNUM_GEMSTONE": 40,
  "FROSTFIRE_GEMSTONE": 40
  },

  "tier4": {"DERELICT_ASHE": 10000, "LAVATEARS_RUNE": 450, "WISPS_ICE_FLAVORED_SPLASH_POTION": 500, "BUNDLE_OF_MAGMA_ARROWS": 1500, "MANA_DISINTEGRATOR": 700, "SCORCHED_BOOKS": 400, "KELVIN_INVERTER": 250, "BLAZE_ROD_DISTILLATE": 900, "GLOWSTONE_DISTILLATE": 900, "MAGMA_CREAM_DISTILLATE": 900, "NETHER_WART_DISTILLATE": 900, "GABAGOOL_DISTILLATE": 500, "SCORCHED_POWER_CRYSTAL": 600, "ARCHFIEND_DICE": 200, "FIRE_ASPECT_III_BOOK": 250, "FIERY_BURST_RUNE": 40, "FLAWED_OPAL_GEMSTONE": 550, "DUPLEX_I_BOOK": 350, "HIGH_CLASS_ARCHFIEND_DICE": 50, "WILSONS_ENGINEERING_PLANS": 20, "SUBZERO_INVERTER": 10,
  "CINDERED_INVERTER": 250,
  "INFERNAL_INVERTER": 10,
  "INFERNO_EDGE": 500,
  "INFERNO_VERTEX": 125,
  "INFERNUM_GEMSTONE": 100,
  "FROSTFIRE_GEMSTONE": 100,
  "INFERNO_APEX": 10,
  "REVITALISED_FUSION_CORE": 4
  }
 }
}



guaranteed = ["DERELICT_ASHE"]

extra = ["LAVATEARS_RUNE", "FIERY_BURST_RUNE", "HIGH_CLASS_ARCHFIEND_DICE"]

non_mf = [*guaranteed, "BUNDLE_OF_MAGMA_ARROWS"]

fancy1 = {"blaze": "Inferno Demonlord"}

fancy2 = {
 "DERELICT_ASHE": "Derelict Ashe", "LAVATEARS_RUNE": "Lavatears Rune", "WISPS_ICE_FLAVORED_SPLASH_POTION": "Wisp's Ice-Flavored I Splash Potion", "BUNDLE_OF_MAGMA_ARROWS": "Bundle of Magma Arrows", "MANA_DISINTEGRATOR": "Mana Disintegrator", "SCORCHED_BOOKS": "Scorched Books", "KELVIN_INVERTER": "Kelvin Inverter", "BLAZE_ROD_DISTILLATE": "Blaze Rod Distillate", "GLOWSTONE_DISTILLATE": "Glowstone Distillate", "MAGMA_CREAM_DISTILLATE": "Magma Cream Distillate", "NETHER_WART_DISTILLATE": "Nether Wart Distillate", "GABAGOOL_DISTILLATE": "Gabagool Distillate", "SCORCHED_POWER_CRYSTAL": "Scorched Power Crystal", "ARCHFIEND_DICE": "Archfiend Dice", "FIRE_ASPECT_III_BOOK": "Fire Aspect III Book", "FIERY_BURST_RUNE": "Fiery Burst Rune", "FLAWED_OPAL_GEMSTONE": "Flawed Opal Gemstone", "DUPLEX_I_BOOK": "Duplex I", "HIGH_CLASS_ARCHFIEND_DICE": "High Class Archfiend Dice", "WILSONS_ENGINEERING_PLANS": "Wilson's Engineering Plans", "SUBZERO_INVERTER": "Subzero Inverter",
 "CINDERED_INVERTER": "Cindered Inverter",
 "INFERNAL_INVERTER": "Infernal Inverter",
 "INFERNUM_GEMSTONE": "Infernum Gemstone",
 "FROSTFIRE_GEMSTONE": "Frostfire Gemstone",
 "INFERNO_EDGE": "Inferno Edge",
 "INFERNO_VERTEX": "Inferno Vertex",
 "INFERNO_APEX": "Inferno Apex",
 "REVITALISED_FUSION_CORE": "Revitalised Fusion Core"
}

thresholds = {"blaze": 56}

variations = {
 "inferno":"blaze", "demon":"blaze", "demonlord":"blaze", "b":"blaze"
}



def dynamic_round(v):
 N,D,F,R=*str(v).split("."),float,round;I=[D.index(x)+1if x in D else 99for x in[f"{z1}{z2}"for z1 in"456"for z2 in"12890"]]
 if any(g!=99for g in I):v=F(f"{N}.{D[:min(I)]}")
 return R(v,4)

def sometimes(n):return int(n)if int(n)==n else round(n, 10)



def main(s):
 print(f"{s}\nUse a semi-colon followed by the inputs\n(space separated) in order to skip steps.\n")
 skip = False
 mf = input("Enter Magic Find\n> ")
 try:
  mf = int(mf)
 except:
  try:
   if mf[0] != ";": raise Exception
   mf,slayer,tier=mf[1:].split(" ")
   mf = int(mf)
   skip = True
  except:
   main("Invalid Magic Find.\n\n")

 if not skip:
  slayer = input("\nEnter slayer type (blaze)\n> ")
 if slayer not in weights.keys():
  if slayer not in variations.keys():
   main("Invalid slayer type.\n\n")
  else:
   slayer = variations[slayer]
 tiers = weights[slayer]

 if not skip:
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
 threshold = thresholds[slayer]
 for drop in new_weights:
  if drop not in extra:
   if drop not in guaranteed:
    C,D = new_weights[drop],t_no_ex
    X = 100 * new_weights[drop] / t_no_ex
    m2 = f"  {fancy2[drop]}: {round(X, 6)}%"
    m += m2
    if len(m2) < threshold:
     m += " "*(threshold-len(m2))
    m += f"(~1/{dynamic_round(100/X)})        ({sometimes(C)}/{sometimes(D)})\n"
   else:
    m += f"  {fancy2[drop]}: 100%\n"
  elif drop in extra:
   C2,D2 = new_weights[drop],(t_no_ex + new_weights[drop])
   X2 = 100 * new_weights[drop] / (t_no_ex + new_weights[drop])
   m2 = f"  {fancy2[drop]}: {round(X2, 6)}%"
   m += m2
   if len(m2) < threshold:
    m += " "*(threshold-len(m2))
   m += f"(~1/{dynamic_round(100/X2)})        ({sometimes(C2)}/{sometimes(D2)})\n"

 main(f"{m}\n\n")



while __name__ == "__main__":
 main("\n\n")