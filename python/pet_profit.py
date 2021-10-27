def km(s):
  if s[-1] == "k":
    s = int(s[:-1]) * 1000
  elif s[-1] == "m":
    s = int(s[:-1]) * 1000000
  try:
    return int(s)
  except:
    return False


def pet_profit(crafting_price, epic_sell, leg_sell):
  if leg_sell < crafting_price and epic_sell < crafting_price:
    return "ilp"
  loop, iter = True, 0
  while loop:
    pet_luck = iter
    lc = (1 + (pet_luck / 100)) * 20
    leg_pet = lc / (80 + lc)
    epic_pet = 1 - leg_pet
    gain = leg_pet * leg_sell + epic_pet * epic_sell
    profit = gain - crafting_price
    if profit < 0:
      iter += 1
      #print(f"DEBUG: Pet Luck: {pet_luck} ||| Profit: {profit}")
    else:
      loop = False
      return pet_luck


def main():
  print("(k/m suffixes allowed)")
  c = input("Enter cost of crafting 1 pet: ")
  e = input("Enter epic pet sell price: ")
  l = input("Enter leg pet sell price: ")
  c,e,l = [km(x)for x in [c,e,l]]
  if not all([c,e,l]):
    print("Invalid arguments.")
    return

  pl = pet_profit(c, e, l)
  if pl == "ilp":
    print("Crafting price must be lower than the sale price either the legendary or epic variant.")
    return
  if pl == 0:
    print("Guaranteed profit no matter what (on average).")
  elif pl > 0:
    print(f"You would need more than {pl} Pet Luck to make profit on average.")



while __name__ == "__main__":
  print("\n\n")
  main()
