def km(s):
    if s[-1] == "k":
        s = int(s[:-1]) * 1000
    elif s[-1] == "m":
        s = int(s[:-1]) * 1000000
    try:
        return int(s)
    except:
        print("Invalid value.")
        return


def main():
    c = input("Enter cost of crafting 1 pet (k, m accepted): ")
    e = input("Enter epic pet sell price (k, m accepted): ")
    l = input("Enter leg pet sell price (k, m accepted): ")
    c,e,l = [km(x)for x in [c,e,l]]
    try:
        pl = -((100*(l + 4*e - 5*c))/(l-c))
    except ZeroDivisionError:
        print("The cost of crafting a pet has to be lower than the price of a legendary variant.")
        return

    if pl <= 0:
        print("Guaranteed profit no matter what (on average).")
    elif pl > 0:
        print(f"You would need more than {int(pl)} Pet Luck to make profit on average.")



while __name__ == "__main__":
    print("\n\n")
    main()


"""
(notes)
base chance
20 : 80

E/L = amount the Epic/Leg pets sell for
C = craft cost

lw = 20 * (1+(P/100))
lc = lw / (80+lw)
    = (20 * (1+(P/100))) / (80+(20 * (1+(P/100))))

X = lc*L + (1-lc)*E

to break even
    let n = lc
    nL + (1-n)E = C
    n = (C-E)/(L-E)
    (20 * (1+(P/100))) / (80+(20 * (1+(P/100)))) = (C-E)/(L-E)

    p = -((100*(L + 4*E - 5*C))/(L-C))


craft cost has to be lower than leg price
"""
