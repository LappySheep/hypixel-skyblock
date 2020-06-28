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
    pl = int(((400 / (l/e - 1)) - 100) // 1)

    print("You would need {} Pet Luck to break even, or {} Pet Luck to make profit.".format(pl, pl+1))if pl>0else print("You break even no matter what.")



while __name__ == "__main__":
    print("\n\n")
    main()
